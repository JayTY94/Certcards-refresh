




1
Hasura and GraphQL
GraphQL — An open-source query language for APIs plus a runtime that fulfills those queries. Created at Facebook, open-sourced in 2015. The "graph" refers to how data connects (users → posts → comments), which you can traverse in one request.







2
Hasura and GraphQL
Single endpoint — Unlike REST (many URLs like /users, /posts/10/comments), GraphQL exposes one endpoint (typically /graphql). You don't pick a URL; you send a query describing the data you want.







3
Hasura and GraphQL
Over-fetching & under-fetching — REST's core pain. Over-fetching = getting fields you don't need; under-fetching = having to make extra calls for missing data. GraphQL fixes both: the client requests exactly the fields it wants — no more, no less.







4
Hasura and GraphQL
Query — A read operation (the "GET" equivalent). Fetches data without changing it.
Mutation — A write operation: create, update, or delete (the "POST/PUT/DELETE" equivalent). Memory hook: read = query, write = mutation.








5
Hasura and GraphQL
Subscription — A live, persistent connection that pushes real-time updates to the client whenever data changes (chat messages, live dashboards). No need to keep re-asking.







6
Hasura and GraphQL
Schema — The strongly-typed contract of the API: every type, field, and operation it supports. Because it's typed, tools can validate and auto-complete queries before they run.







7
Hasura and GraphQL
Resolver — The function behind a schema field that actually fetches or computes that field's data when a query runs. Hand-built GraphQL servers require writing one per field (a lot of work — which is why Hasura exists).







8
Hasura and GraphQL
Query variables — The safe way to pass dynamic values (a search term, an ID) into a query: declare a variable and pass the value separately, instead of concatenating it into a string. Reusable and injection-safe.







9
Hasura and GraphQL
Fragment — A reusable, named set of fields you can drop into multiple queries to avoid repeating yourself.







10
Hasura and GraphQL
Introspection — GraphQL APIs are self-describing: a client can ask the API to describe its own schema. Powers auto-complete and live docs. Often disabled in production for security.







11
Hasura and GraphQL
REST vs. GraphQL (request style) — REST uses multiple resource endpoints; GraphQL uses a single endpoint with a query describing the data. REST shape is fixed by the server; GraphQL shape is chosen by the client.







12
Hasura and GraphQL
Error handling — GraphQL usually returns HTTP 200 even on errors, placing an errors array in the response body. A single response can be partially successful. Watch out: status-code-only monitoring can miss GraphQL errors.







13
Hasura and GraphQL
Versioning — GraphQL avoids /v1 → /v2 URL versioning. Instead you add new fields and deprecate old ones, so the API evolves continuously without breaking existing clients. "Deprecate, don't break."







14
Hasura and GraphQL
Caching tradeoff — A genuine downside of the single endpoint: standard HTTP-level caching is harder than with REST (REST can cache per-URL easily).







15
Hasura and GraphQL
N+1 query problem — Fetch a list of N items, then run one extra query per item (1 + N queries). A classic performance trap, solved by batching (e.g., DataLoader, or Hasura's query compiler).







16
Hasura and GraphQL
Query-depth security risk — Because clients craft their own queries, a deeply nested/expensive query could overload the server. Mitigated with depth limits and query-cost analysis.







17
Hasura and GraphQL
Hasura — An engine that connects to your database and auto-generates a full GraphQL API (queries, mutations, subscriptions) with little or no code. It writes the resolvers for you, eliminating most back-end boilerplate.







18
Hasura and GraphQL
PostgreSQL — Hasura's home-turf database ("Postgres"). It started Postgres-focused and now supports several other databases too.







19
Hasura and GraphQL
Aggregate fields — When Hasura tracks a table, it auto-generates aggregates: counts, sums, averages, mins, and maxes (plus filtering, ordering, pagination).







20
Hasura and GraphQL
Row-level permissions — Restrict which records a role can see (e.g., "only rows where user_id = the logged-in user"). Enforced server-side by Hasura, not the browser.







21
Hasura and GraphQL
Column-level permissions — Restrict which fields a role can see (e.g., hide salary). Hasura strips the column server-side before data leaves — never rely on the front-end to hide it.







22
Hasura and GraphQL
Column-level permissions — Restrict which fields a role can see (e.g., hide salary). Hasura strips the column server-side before data leaves — never rely on the front-end to hide it.







23
Hasura and GraphQL
Actions — Add custom business logic beyond basic CRUD (charge a card, send an email). An Action exposes a custom operation that calls your own handler, surfaced in the same API.







24
Hasura and GraphQL
Event Triggers — Server-side automation: when a row is inserted/updated/deleted, Hasura calls an external webhook. "When this changes, go do that."







25
Hasura and GraphQL
Authentication (JWT) — Hasura commonly identifies a user and role by validating a JWT and reading its claims. The role then drives row/column permissions.







26
Hasura and GraphQL
Authentication (JWT) — Hasura commonly identifies a user and role by validating a JWT and reading its claims. The role then drives row/column permissions.







27
Hasura and GraphQL
Subscription vs. Event Trigger — A subscription pushes live data to a client (front-end listening). An Event Trigger fires server-side automation (calls a webhook) on data changes.







28
Hasura and GraphQL
Row-level vs. Column-level permissions — Row-level = which records; Column-level = which fields. Together they form Hasura's security backbone.







29
Hasura and GraphQL
Action vs. Remote schema — An Action adds your custom logic as a new operation. A Remote schema merges an existing external API into Hasura's schema.







30
Hasura and GraphQL






31
Hasura and GraphQL






32
Hasura and GraphQL






33
Hasura and GraphQL






34
Hasura and GraphQL






35
Hasura and GraphQL






36
Hasura and GraphQL






37
Hasura and GraphQL






38
Hasura and GraphQL






39
Hasura and GraphQL






40
Hasura and GraphQL






41
Hasura and GraphQL






42
Hasura and GraphQL






43
Hasura and GraphQL






44
Hasura and GraphQL






45
Hasura and GraphQL






46
Hasura and GraphQL






47
Hasura and GraphQL






48
Hasura and GraphQL






49
Hasura and GraphQL






50
Hasura and GraphQL






