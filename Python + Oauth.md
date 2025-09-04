=============
Authorization Code Flow

An OAuth 2.0 process where the user logs in via a browser, and the app receives a temporary code that it can exchange for an access token. This flow is secure because the client secret is never exposed during the initial login.

=============
redirect_uri

The URL where the OAuth provider sends the user after login. It must match the one registered with the provider. In this script, it's `http://localhost:8080/callback`, which points to a local server waiting to catch the redirect.

=============
OAuthHandler (Custom HTTP Request Handler)

A subclass of `http.server.SimpleHTTPRequestHandler` that overrides the `do_GET` method to process incoming HTTP requests. It extracts the authorization code from the URL and initiates the token exchange process.

=============
socketserver.TCPServer

A Python class that creates a simple TCP server. In this script, it listens on `localhost:8080` and uses `OAuthHandler` to handle incoming requests. The server runs inside a context manager to ensure it shuts down cleanly after handling one request.

=============
handle_request()

A method of `TCPServer` that waits for a single incoming request and then processes it using the specified handler class. It’s used here to catch the OAuth redirect containing the authorization code.

=============
urllib.parse.urlparse / parse_qs

Functions used to break down the incoming URL and extract query parameters. In this case, they’re used to retrieve the `code` value from the redirect URL.

=============
base64.b64encode

Encodes the client ID and secret into a base64 string for use in the `Authorization` header. This is required by the OAuth token endpoint to authenticate the client during the token exchange.

=============
requests.post

Sends an HTTP POST request to the token endpoint with the authorization code and client credentials. If successful, it returns a JSON object containing the access token and other OAuth metadata.

=============
client_id and client_secret

Values issued by the OAuth provider to identify and authenticate your application. The `client_id` is public, while the `client_secret` must be kept confidential and is used during the token exchange to prove your app's identity.

=============
scope

A space-separated list of permissions your app is requesting. It defines what access the token will grant — for example, reading user profiles or writing data. The OAuth provider will show these scopes to the user during login.

=============
authorize_url

The endpoint where the user is sent to log in and grant access. It’s part of the OAuth provider’s infrastructure and handles user authentication and consent.

=============
auth_request_url

The full URL constructed from `authorize_url` and query parameters like `client_id`, `redirect_uri`, and `scope`. This is the link opened in the browser to start the OAuth flow.

=============
webbrowser.open()

A Python function that launches the default web browser and navigates to the given URL. Used here to initiate the login process for the user.

=============
urllib.parse.urlencode()

Encodes a dictionary of parameters into a URL query string. This ensures special characters are properly escaped and the URL is valid.

=============
urllib.parse.unquote()

Decodes percent-encoded characters in a URL. Used here to clean up the authorization code received from the redirect.

=============
handler.wfile.write()

Writes a response back to the browser window. In this script, it sends a simple message like “You may close this window” after the code is received.
handler is an instance of OAuthHandler, which inherits from http.server.SimpleHTTPRequestHandler

=============
global token_dict

Declares that `token_dict` is a global variable so it can be modified inside the `do_GET` method. This is where the access token and other OAuth metadata are stored after the token exchange.

=============
Content-Type: application/x-www-form-urlencoded

A header that tells the OAuth token endpoint how the POST data is formatted. This is required for most OAuth token exchanges.

=============
http.server.SimpleHTTPRequestHandler

A built-in Python class that handles HTTP GET requests and serves files from the current directory. It can be subclassed to customize how requests are processed — like extracting query parameters or sending custom responses.

=============
do_GET()

A method in `SimpleHTTPRequestHandler` that is automatically called when the server receives a GET request. You override this method to define custom behavior, such as parsing the URL and responding with HTML or triggering logic like token exchange.

=============
handler.send_response()

Sends an HTTP status code back to the client (browser). For example, `handler.send_response(200)` indicates success, while `handler.send_response(400)` signals a bad request.
handler is an instance of OAuthHandler, which inherits from http.server.SimpleHTTPRequestHandler

=============
handler.end_headers()

Finalizes the HTTP response headers. It must be called after `handler.send_response()` and before writing any content to the response body.
handler is an instance of OAuthHandler, which inherits from http.server.SimpleHTTPRequestHandler

=============
handler.wfile.write()

Writes raw bytes to the response body. In your code, it sends a message like “You may close this window” back to the browser after the authorization code is received.
handler is an instance of OAuthHandler, which inherits from http.server.SimpleHTTPRequestHandler

=============
("localhost", 8080)

The address tuple passed to `TCPServer`. It tells the server to listen on port 8080 of the local machine. This must match the `redirect_uri` registered with the OAuth provider.
with socketserver.TCPServer(("localhost", 8080), OAuthHandler) as httpd:
    ...
=============
with socketserver.TCPServer(...) as httpd

A context manager that ensures the server is properly started and shut down. It simplifies cleanup and avoids leaving open sockets after the request is handled.

