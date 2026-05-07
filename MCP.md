




1
MCP
Model Context Protocol (MCP)
An open standard from Anthropic (Nov 2024) for connecting LLM applications to external tools and data sources. Solves the "N×M integration problem" — instead of every AI app writing custom connectors for every data source, both sides speak one protocol.






2
MCP
Three roles: Host, Client, Server
    Host — the LLM application the user interacts with (Claude Desktop, an IDE). Initiates connections.
    Client — a connector object inside the host. One client per server connection.
    Server — your code. Exposes tools, resources, prompts.
The confusing bit: "client" is internal to the host, not a separate program. The host is the whole app; the client is its arm reaching out to one server.






3
MCP
MCP and LSP
MCP's architecture is modeled on the Language Server Protocol (LSP) — the protocol that lets language servers (Python, Rust, etc.) plug into many editors. LSP solved "M editors × N languages"; MCP solves "M AI apps × N data sources." Both use JSON-RPC, both have capability negotiation, both keep stateful connections.






4
MCP
JSON-RPC 2.0 (the envelope)
A lightweight format MCP uses for every message. Required fields on a request:

{
  "jsonrpc": "2.0",
  "id": 7,
  "method": "tools/call",
  "params": { "name": "create_issue", "arguments": { "repo": "x/y", "title": "bug" } }
}




5
MCP
JSON-RPC vs MCP
JSON-RPC = the envelope. Generic. Defines request/response/error shape and numeric error codes.
MCP = the vocabulary layered on top. Defines methods like initialize, tools/list, tools/call, resources/read, capability negotiation, the concept of tools/resources/prompts, sampling, progress notifications.
Like HTTP vs REST: HTTP defines verbs and headers; REST gives them meaning.






6
MCP
Subprocess
A separate program launched and supervised by another. The launcher is the parent; the launched is the child. They run in their own memory — a crash in the child doesn't kill the parent — but the parent can pipe data into the child's stdin and read from the child's stdout.






7
MCP
stdio transport (MCP)
The default for local MCP servers. The host launches your server as a child subprocess and exchanges newline-delimited JSON-RPC messages over its stdin/stdout. Recommended whenever possible.






8
MCP
Critical stdio rule: never print to stdout
In a stdio MCP server, stdout is reserved for valid JSON-RPC messages. A stray print(), console.log(), or warning corrupts the protocol stream and the client disconnects. Send all logs/diagnostics to stderr instead. Almost everyone trips on this once.






9
MCP
Streamable HTTP transport (MCP)
The transport for remote MCP servers. Supports request/response and server-sent streaming over HTTP. This is the transport that requires the OAuth 2.1 authorization spec.




10
MCP
stdio vs Streamable HTTP
stdio — local, parent/child via pipes, credentials come from environment variables
Streamable HTTP — remote, networked, credentials come from OAuth 2.1 flows





11
MCP
Authorization by transport
HTTP transport SHOULD implement OAuth 2.1 (with PKCE, dynamic client registration per RFC 7591, server metadata per RFC 8414).
stdio transport SHOULD NOT use that flow — credentials come from environment variables the host supplies at launch.
The trust model is different: stdio is local (the user already controls the process); HTTP is remote (need delegated consent).






12
MCP
Server primitives (what your server exposes)
Three things a server can offer to clients:

Tools — functions the model invokes mid-task
Resources — read-only data the user attaches to context
Prompts — templated workflows the user invokes




13
MCP
Tool vs Resource — who initiates?
Tool = model-initiated. The LLM decides to call search_jira while working.
Resource = user-initiated. The user @-mentions jira://ticket/PROJ-123 to attach it.
If a user might want to "pin" or "@-mention" it, it's a resource. If the model decides on the fly to fetch it, it's a tool. Most real APIs need both.






14
MCP
Resource templates
A URI pattern that exposes a family of resources without enumerating each one. Uses RFC 6570 syntax:

jira://ticket/{ticket_id}
When the user types @PROJ-123, the host expands the template to jira://ticket/PROJ-123, calls resources/read on your server. Your code parses the URI, fetches the data, returns it.






15
MCP
Tool inputSchema
Every tool definition includes an inputSchema written as JSON Schema (typically Draft 2020-12). It declares parameter types, required fields, descriptions, and constraints. The model uses it to generate structurally valid calls.




16
MCP
Tool annotations (hints to the host UI)
Optional fields that signal a tool's behavior so the host can decide what consent prompts to show:

Annotation	Meaning
readOnlyHint	Only reads, no side effects
destructiveHint	May make irreversible changes (delete, drop)
idempotentHint	Same args produce same result if called repeatedly
openWorldHint	Interacts with external systems (network, files)
Caveat: annotations from untrusted servers are not trustworthy. A malicious server can lie. Hints help good clients build good UX; they don't replace user consent.






17
MCP
Client features (what the host offers servers)
Sampling — server asks the host to run an LLM completion on its behalf. Server says "ask the LLM this"; host stays in control, user approves.
Roots — server asks "what filesystem/URI boundaries am I allowed to operate in?"
Elicitation — server asks the user (via the host UI) for additional input mid-operation.
These flow from server to host — the reverse of the usual direction.






18
MCP
Sampling — why the direction is backward
Most server features go: client asks, server answers. Sampling goes: server asks, host runs LLM completion, host returns result to server. Lets servers do agentic, recursive reasoning without embedding their own LLM. User must approve; host limits what the server can see.






19
MCP
Capability negotiation
The first thing that happens after a connection opens. Client and server each declare which features they support (tools, resources, sampling, roots, etc.). Neither side then calls something the other can't handle. Lives in the initialize request/response.






20
MCP
Cursor pagination
For large result sets, the server returns one page plus a nextCursor token:

Request:  { "method": "tools/list" }
Response: { "tools": [/* 50 items */], "nextCursor": "eyJpZCI6NTB9" }

Request:  { "method": "tools/list", "params": { "cursor": "eyJpZCI6NTB9" } }
Response: { "tools": [/* next 50 */], "nextCursor": null }   <- end

The cursor is opaque — clients don't parse it. Cursors are stable across inserts (page numbers aren't). Used by built-in list methods and recommended for your own bulk-read tools.






21
MCP
Progress notifications
For long-running requests, include a progressToken on the request. The server then sends notifications/progress messages with current/total counts. Pairs with cursor pagination for big API operations.

There's also a cancellation notification — clients can abort in-flight requests; servers should stop the upstream call cleanly.






22
MCP
Secrets for stdio servers
Store API keys in environment variables the host passes when spawning the subprocess. Never hardcode in source, never make the LLM provide them via tool params, never put them in inputSchema defaults. The user's host config (e.g., Claude Desktop's JSON config) is where these live.

Example Claude Desktop config:

{
  "mcpServers": {
    "stripe": {
      "command": "node",
      "args": ["/path/to/stripe-mcp-server.js"],
      "env": {
        "STRIPE_API_KEY": "sk_live_..."
      }
    }
  }
}





23
MCP
MCP security risks (the real ones)
Prompt injection — a malicious resource or tool description injects instructions the model then follows.
Tool combination exfiltration — combining permissions across tools to leak data in ways no single tool would allow.
Lookalike tools — a malicious server registers a tool with a name/description nearly identical to a trusted one, silently substituting itself.
The spec relies on user consent at every step because the protocol can't enforce trust. Hosts must show what's being called, with what data, and require approval — especially for destructiveHint tools and sampling requests.






24
MCP
Error responses
On bad input, return a JSON-RPC error response — don't crash, don't silently default, don't return success-with-null. JSON-RPC defines numeric error codes:

Code	Meaning
-32700	Parse error
-32600	Invalid Request
-32601	Method not found
-32602	Invalid params
-32603	Internal error
Include a clear message. The model often reads error text and self-corrects on the next call.






25
MCP





26
MCP





27
MCP





28
MCP





29
MCP





30
MCP





31
MCP





32
MCP





33
MCP





34
MCP





35
MCP





36
MCP





37
MCP





38
MCP





39
MCP





40
MCP





41
MCP





42
MCP





43
MCP





44
MCP





45
MCP





46
MCP





47
MCP





48
MCP





49
MCP





50
MCP





