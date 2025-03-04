Azure Functions:
A serverless compute service that allows you to run event-driven code without having to manage infrastructure.

Timer Trigger:
A type of trigger in Azure Functions that runs code on a schedule defined by a CRON expression. It can be configured to run immediately on startup for testing purposes with the run_on_startup parameter.

Managed Identity:
A feature in Azure that provides an automatically managed identity in Azure Active Directory (Azure AD) for applications to use when connecting to resources that support Azure AD authentication. There are system-assigned and user-assigned managed identities.

Service Principal:
An identity created for use with applications, hosted services, and automated tools to access Azure resources. Managed identities are represented as service principals in Azure AD.

DefaultAzureCredential:
A credential class provided by the azure-identity package that attempts to authenticate using multiple methods (e.g., EnvironmentCredential, ManagedIdentityCredential) in a predefined order, making it useful for both local development and production environments.

ManagedIdentityCredential:
A credential class specifically used to obtain tokens via the managed identity assigned to an Azure resource. It works only when the resource (e.g., Azure Function) is running in Azure.

OAuth2:
An open standard for access delegation commonly used as a way to grant websites or applications limited access to user information without exposing passwords.

Scope:
In the context of Azure AD, the scope (or resource) string defines what resource the access token is intended for. For Dynamics 365, it’s typically the base URL with the /.default suffix (e.g., "https://accuity.crm.dynamics.com/.default").

Environment Variables:
Variables set at the operating system or application level that can be used to store configuration values such as connection strings, credentials, or environment settings. In Azure Functions, these are defined in the local.settings.json for local development and in Application Settings in the Azure Portal for production.

local.settings.json:
A file used in Azure Functions for local development to set environment variables and other settings without hardcoding values in your code.

Dynamics 365 / Dataverse:
Microsoft's suite of business applications (Dynamics 365) and the underlying data platform (Dataverse) that allows you to store and manage data. Integration with Dynamics typically involves using its Web API.

Application User:
A user type in Dynamics/Dataverse that represents an application (via its service principal) rather than an interactive human user. This is used to grant an application's managed identity the permissions to interact with Dynamics data.

IMDS (Instance Metadata Service):
A service available in Azure VMs and other compute resources that provides information about the running instance, including the endpoint used by managed identities to fetch tokens. This endpoint isn’t available in local development environments.

HTTP Headers:
Key-value pairs sent with HTTP requests to provide metadata about the request. For Dynamics API requests, headers typically include Authorization (with the bearer token) and Content-Type.