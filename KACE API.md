KACE API.md 
Session‑Oriented API
An API design where the server maintains state about the client between requests. Authentication establishes a server‑side session, and subsequent requests rely on session state (often identified by cookies) to determine context such as user identity, permissions, or selected organization.
........
Stateless API
An API design where each request is evaluated independently. All required authentication and authorization context is contained in the request itself (typically via a bearer token). The server does not retain memory of prior requests.
........
Bearer Token Authentication
An authentication model where the client presents a token (usually OAuth/JWT) with each request. The token itself contains or implies identity, tenant, and permissions. No server‑side session or cookies are required.
........
Cookie‑Based Session Authentication
An authentication model where the server issues cookies after login. The client must return these cookies on subsequent requests so the server can associate the request with an existing session and its stored context.
........
Server‑Side Session State
Data maintained by the server and associated with a session identifier (typically a cookie). May include authenticated user, selected organization, permissions, feature flags, or UI context. This state is not encoded in each request.
........
KACE SMA API – Authentication Model
KACE uses a session‑oriented API model. Login creates a server‑side session identified by cookies (e.g., kboxid). The selected organization is stored in the session, not fully derived from the bearer token.
........
KACE SMA API – Organization Context
In multi‑organization environments, all API calls are scoped to the currently selected organization. This selection is stored in the server‑side session. If no organization is selected, API calls fail with “No Current Organization Selected.”
........
requests.Session (Python)
A persistent HTTP client object that automatically stores and reuses cookies, headers, and connections across requests. It behaves like a browser session, allowing stateful APIs to function correctly without manual cookie handling.
........
requests.Session – Cookie Handling
When a response includes Set‑Cookie headers, requests.Session() parses and stores them. On future requests to matching domains/paths, the session automatically sends a Cookie header derived from its cookie jar.
........
requests Without Session
Using requests.get() or requests.post() directly creates stateless, one‑off requests. Cookies returned by the server are discarded unless manually reattached, making this unsuitable for session‑oriented APIs.
........
Why JWT Alone Is Insufficient in KACE
Although KACE issues a JWT during authentication, authorization decisions (such as organization selection) rely on server‑side session state. The bearer token proves authentication, but the session determines context.
........
Dataverse Web API – Contrast
Dataverse uses a stateless, token‑centric model. The bearer token encodes tenant and authorization context, so cookies and server‑side sessions are unnecessary. Each request stands alone.
........
Recognizing a Session‑Oriented API
Indicators include:

Set‑Cookie headers during login
Errors referencing “current user” or “current organization”
Endpoints for “switch organization” or “refresh context”
UI‑first products with APIs added later

........
Practical Heuristic
If an API evolved from a web UI, assume session state and cookie handling until proven otherwise. If an API was designed cloud‑first, assume stateless bearer‑token authentication.
........
Operational Failure Mode
Logging in successfully but losing cookies between requests results in errors that appear unrelated to authentication (e.g., missing context, organization, or permissions), even when a bearer token is present.
........
Minimal Operational Rule
If an API sets cookies during authentication, you must preserve and replay them. In Python, this means using requests.Session() rather than standalone request calls.
........
Provide your feedback on BizChatYou said: Can you include some notes on the code problems from the conversation?Copilot said: CopilotBelow are additional notes focused on the code‑level problems and fixes from this conversation, written in the same style and granularity as your examples: short, reminder‑oriented, operationally grounded.

KACE API – Misplaced organizationName
The organizationName parameter must be included in the JSON body of the login request, not as an HTTP header. Supplying it as a header is ignored by KACE and results in authentication without an organization context.
........
KACE Login Request – Correct Structure
A valid KACE login request requires userName, password, and (optionally) organizationName in the JSON body, along with the x‑kace‑api‑version header. Organization selection does not occur via custom headers.
........
Using requests Without Session – Common Failure
Calling requests.post() followed by requests.get() without a shared Session causes cookies returned during authentication to be discarded. This breaks session‑oriented APIs even when authentication initially succeeds.
........
requests.Session – Required for KACE APIs
KACE APIs require requests.Session() so cookies set during login are preserved and replayed. Without a session, server‑side context such as the selected organization is lost.
........
Implicit Cookie Dependency
If an authentication response contains Set‑Cookie headers, the API likely expects clients to return those cookies on subsequent requests. Ignoring this indicates a mismatch between client code and the API’s state model.
........
Bearer Token Misinterpretation
In KACE, the bearer token returned during login confirms authentication but does not fully establish authorization context. Relying solely on the token without preserving cookies leads to misleading errors unrelated to credentials.
........
“No Current Organization Selected” – Root Cause
This error occurs when the server cannot associate the request with a session that has an active organization. Common causes include missing cookies, dropped session state, or failing to set organizationName during login.
........
API Version Mismatch
Using an outdated API version (e.g., x‑kace‑api‑version: 1) may still allow authentication but can cause inconsistent behavior around session handling and organization context. Current KACE APIs expect version 5.
........
requests.Session – Invisible Behavior
requests.Session() automatically parses Set‑Cookie headers, stores cookies internally, and injects a Cookie header into future requests. This behavior is implicit and can obscure the root cause of failures when not understood.
........
Manual Cookie Handling – Usually Unnecessary
Manually extracting Set‑Cookie headers and re‑adding them to requests is error‑prone. Using requests.Session() is the correct and intended approach for session‑based APIs.
........
HTTP vs HTTPS Consistency
Cookies are domain‑ and scheme‑aware. Mixing http:// and https:// endpoints may prevent cookies from being sent, resulting in lost session context despite correct code structure.
........
Debugging Technique – Inspect Session Cookies
When debugging authentication issues, inspecting session.cookies confirms whether login established a session and whether cookies are being preserved as expected.
........
API Design Smell – Token + Cookies
When an API returns both a bearer token and cookies, it often indicates a hybrid or transitional design. Token presence does not guarantee statelessness; cookie inspection is still required.
........
Minimal Correct Pattern (Conceptual)
For session‑oriented APIs:

Create a requests.Session()
Authenticate once
Reuse the session for all API calls
Deviating from this pattern commonly results in context‑related failures.

........
False Confidence Failure Mode
Successful authentication responses can give false confidence that client code is correct. In session‑based APIs, failures often appear one request later when state is missing rather than credentials.
........
Operational Lesson
When API behavior contradicts documentation, inspect HTTP traffic (headers, cookies) rather than relying solely on reference guides. The wire protocol often reveals unstated assumptions.
........

If you want, next I can:

Compress these into procedural recall cards
Convert them into “symptom → cause → fix” operators’ notes
Or refactor into a single “Session vs Token” comparison note

You’ve basically produced a reusable API-debugging playbook here.