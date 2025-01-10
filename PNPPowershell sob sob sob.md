1. Connect-PnPOnline (PnP.PowerShell)
Establishes a connection to a SharePoint site using various authentication methods like client credentials or device code flow, enabling subsequent PnP.PowerShell cmdlets to interact with SharePoint.

2. Add-PnPFile (PnP.PowerShell)
Uploads a file to a specified SharePoint document library or folder. Supports parameters like -Path for local files and -Stream for uploading via a data stream.

3. Get-PnPConnection (PnP.PowerShell)
Retrieves details about the current PnP.PowerShell connection, including authentication method, scopes, and connection type, aiding in troubleshooting and verification.

4. Invoke-RestMethod (Microsoft.PowerShell.Utility)
Sends HTTP and HTTPS requests to RESTful APIs and processes the responses. Commonly used for interacting directly with SharePoint REST API in PowerShell scripts.

5. System.IO.Stream (System.IO)
Represents a sequence of bytes, such as a file. Used in PowerShell to handle file data streams for operations like uploading files to SharePoint.

6. PSCredential (Microsoft.PowerShell.Security)
A PowerShell object that securely stores a username and password. Utilized for authentication purposes, ensuring sensitive information is handled safely.

7. OAuth 2.0 Device Code Flow
An authentication method enabling devices with limited input capabilities to obtain user authorization without requiring a client secret, suitable for public clients.

8. OAuth 2.0 Client Credentials Flow
An authentication method where applications authenticate using a client ID and client secret, enabling server-to-server interactions without user involvement.

9. OAuth 2.0 Authorization Code Flow
An interactive authentication method involving user login and authorization, suitable for applications that can securely handle client secrets and require delegated permissions.

10. Azure AD App Registration
The process of registering an application in Azure Active Directory to obtain identifiers like client ID and tenant ID, enabling the app to authenticate and access Microsoft APIs.

11. Client ID (client_id)
A unique identifier assigned to an Azure AD application upon registration. Used to identify the application during authentication processes.

12. Client Secret (client_secret)
A confidential key associated with an Azure AD application, used alongside the client ID to authenticate the application in secure authentication flows.

13. Tenant ID (tenant_id)
A unique identifier for your Azure Active Directory tenant. Specifies the directory in which the application is registered and operates.

14. API Permissions
Permissions granted to an application to access specific APIs like SharePoint or Microsoft Graph. Can be delegated (user-based) or application-level (app-only).

15. Admin Consent
Approval granted by an Azure AD administrator for an application to access certain resources or perform specific actions, essential for elevated API permissions.

16. Scopes
Define the level of access an application has to resources. Examples include Files.ReadWrite.All and Sites.ReadWrite.All, determining what operations the app can perform.

17. SharePoint Site URL
The web address of a SharePoint site (e.g., https://accuityllp.sharepoint.com/sites/ASB), serving as the entry point for accessing site resources and APIs.

18. Document Library
A SharePoint component where documents are stored, managed, and shared. Examples include "Shared Documents" or custom libraries within a site.

19. Server Relative URL
The URL path relative to the SharePoint server, excluding the domain (e.g., /sites/ASB/Shared Documents), used in REST API endpoints for precise resource targeting.

20. SharePoint REST API
A set of web services provided by SharePoint to perform operations like CRUD actions on lists, libraries, and other SharePoint objects using standard HTTP methods.

21. 403 Forbidden Error
An HTTP status code indicating that the server understands the request but refuses to authorize it, typically due to insufficient permissions.

22. AADSTS7000218 Error
An Azure AD error stating that the authentication request lacks a client_assertion or client_secret, preventing successful token acquisition.

23. Parameter Set Conflict
Occurs when incompatible or conflicting parameters are used together in a PowerShell cmdlet, leading to errors as PowerShell cannot determine the intended operation.

24. AppInv.aspx
A SharePoint page used to grant app permissions to specific SharePoint sites, allowing custom or third-party apps to access site resources based on defined permissions.

25. Microsoft Graph API
A unified API endpoint for accessing various Microsoft 365 services, including SharePoint, enabling developers to interact with data and perform operations across Microsoft products.

26. Token Acquisition
The process of obtaining an OAuth 2.0 access token from Azure AD, which is then used to authenticate and authorize API requests to services like SharePoint.

27. Error Handling in PowerShell
Techniques like try-catch blocks used to manage and respond to errors gracefully in scripts, ensuring robustness and easier troubleshooting.

28. System.IO.File (System.IO)
A PowerShell class providing methods for file manipulation, such as reading, writing, opening, and closing files, essential for handling file operations in scripts.

29. Invoke-RestMethod Parameters
Key parameters include -Method (HTTP method), -Uri (API endpoint), -Headers (authentication and content type), and -Body (data payload), crucial for API interactions.

30. Admin Consent Process
The administrative approval process in Azure AD where an admin grants an application the necessary permissions to access resources on behalf of users or the organization.

31. Get-PnPFile (PnP.PowerShell)
Retrieves a file from a SharePoint document library. Allows downloading files to a local path or accessing file properties and content directly within PowerShell scripts.

32. Set-PnPFileCheckedIn (PnP.PowerShell)
Checks in a previously uploaded file in SharePoint, optionally adding comments. Essential for managing document versions and maintaining collaboration workflows.

33. Remove-PnPFile (PnP.PowerShell)
Deletes a specified file from a SharePoint library or folder. Useful for automating cleanup tasks or managing outdated documents programmatically.

34. Get-PnPSite (PnP.PowerShell)
Fetches information about the current SharePoint site, including properties like URL, title, and storage usage. Helps in monitoring and managing site configurations.

35. New-PnPList (PnP.PowerShell)
Creates a new SharePoint list within a site. Supports specifying list templates, columns, and settings, facilitating automated list management.

36. Add-PnPListItem (PnP.PowerShell)
Adds a new item to a SharePoint list. Enables automated data entry and integration with other systems by programmatically populating list data.

37. Update-PnPListItem (PnP.PowerShell)
Modifies an existing item in a SharePoint list. Allows updating fields and properties, supporting dynamic data management and automation.

38. Remove-PnPListItem (PnP.PowerShell)
Deletes an item from a SharePoint list. Useful for maintaining data integrity and automating data cleanup processes.

39. Get-PnPGroup (PnP.PowerShell)
Retrieves information about SharePoint groups within a site. Assists in managing permissions and user access by programmatically handling group memberships.

40. Add-PnPUserToGroup (PnP.PowerShell)
Adds a user to a specified SharePoint group. Facilitates automated user management and access control within SharePoint environments.

41. Remove-PnPUserFromGroup (PnP.PowerShell)
Removes a user from a SharePoint group. Helps in maintaining accurate group memberships and enforcing access policies through scripts.

42. Set-PnPWeb (PnP.PowerShell)
Configures properties of a SharePoint site, such as title, description, and logo. Enables automated site customization and configuration management.

43. Get-PnPWeb (PnP.PowerShell)
Fetches details about the current SharePoint site, including properties like language, template, and navigation settings. Useful for site audits and management.

44. Register-AzureADApplication (AzureAD)
Registers a new application in Azure Active Directory using PowerShell. Automates the setup of app registrations for authentication and API access.

45. New-AzureADServicePrincipal (AzureAD)
Creates a service principal for an Azure AD application. Essential for granting applications permissions and enabling secure interactions with Azure resources.

46. Grant-AzureADAppPermission (AzureAD)
Assigns specific API permissions to an Azure AD application. Ensures applications have the necessary access rights to perform intended operations.

47. Microsoft Graph Permissions
Defines the access levels applications have to Microsoft 365 services via Graph API. Includes delegated and application permissions for fine-grained control.

48. Token Caching
Stores OAuth tokens locally to reduce the need for repeated authentication requests. Enhances script performance and reduces latency in API interactions.

49. Throttling in SharePoint
Limits the number of API requests to prevent abuse and ensure service stability. Requires implementing retry logic and handling throttling responses in scripts.

50. PowerShell Profiles
Scripts that run automatically when PowerShell starts. Used to customize the environment, load modules, and define functions for enhanced productivity.

51. PSCredential Object (Microsoft.PowerShell.Security)
Stores and manages user credentials securely within PowerShell. Used for authenticating commands that require user-based permissions.

52. Invoke-WebRequest (Microsoft.PowerShell.Utility)
Sends HTTP and HTTPS requests to web pages or web services. Similar to Invoke-RestMethod but provides more detailed response information.

53. JSON Conversion
Transforms PowerShell objects to JSON format and vice versa using ConvertTo-Json and ConvertFrom-Json. Essential for handling REST API payloads and responses.

54. REST API Endpoints
Specific URLs used to access SharePoint resources via REST API. Includes paths for sites, lists, libraries, and items, enabling targeted operations.

55. API Rate Limits
Restrictions on the number of API calls an application can make within a specific timeframe. Requires managing request rates to avoid exceeding limits and facing throttling.

56. Azure Key Vault Integration
Securely stores and manages secrets, keys, and certificates used by applications. Enhances security by preventing hardcoding of sensitive information in scripts.

57. SharePoint App Permissions
Defines the access rights granted to SharePoint apps via AppInv.aspx or Azure AD. Controls what resources and actions an app can perform within SharePoint.

58. CSOM (Client-Side Object Model)
An alternative to REST API for interacting with SharePoint from client applications. Provides a different set of libraries and methods for SharePoint operations.

59. PowerShell Modules
Packages containing cmdlets, functions, and scripts that extend PowerShell's capabilities. Examples include PnP.PowerShell and AzureAD, facilitating specialized tasks.

60. Error Codes and Messages
Standardized responses from SharePoint and Azure AD indicating the status of requests. Understanding common errors like AADSTS7000218 aids in effective troubleshooting.

Additional Related Items
61. New-AzureADApplication (AzureAD)
Creates a new application registration in Azure Active Directory via PowerShell. Automates the process of setting up apps for authentication and API access.

62. Get-MsalToken (MSAL.PS)
Retrieves an OAuth 2.0 access token using Microsoft Authentication Library (MSAL) in PowerShell. Facilitates secure token acquisition for API calls.

63. ConvertTo-SecureString (Microsoft.PowerShell.Security)
Transforms plain text into a secure string object in PowerShell. Essential for handling sensitive data like passwords and client secrets securely.

64. Grant-PnPAzureADAppPermission (PnP.PowerShell)
Grants specific API permissions to an Azure AD application directly from PowerShell. Streamlines the permission assignment process for SharePoint access.

65. Invoke-PnPRequest (PnP.PowerShell)
Sends custom HTTP requests to SharePoint APIs within PnP.PowerShell scripts. Allows for advanced interactions beyond standard cmdlet capabilities.

66. Export-PnPProvisioningTemplate (PnP.PowerShell)
Exports a SharePoint site's configuration into a provisioning template. Facilitates site replication, migration, and backup through PowerShell.

67. Import-PnPProvisioningTemplate (PnP.PowerShell)
Imports a provisioning template into a SharePoint site, applying configurations and structures defined in the template. Enables automated site setup and customization.

68. Get-PnPList (PnP.PowerShell)
Retrieves a SharePoint list from the connected site. Used to access list properties, items, and metadata for further manipulation or analysis.

69. Set-PnPList (PnP.PowerShell)
Modifies properties of a SharePoint list, such as title or description. Enables automated updates and management of list configurations.

70. Add-PnPField (PnP.PowerShell)
Adds a new field (column) to a SharePoint list or library. Supports various field types and configurations for customized data structures.

71. Remove-PnPField (PnP.PowerShell)
Deletes a field from a SharePoint list or library. Useful for cleaning up unused or outdated columns programmatically.

72. Get-PnPListItem (PnP.PowerShell)
Fetches items from a SharePoint list based on specified criteria. Enables data retrieval for reporting, analysis, or further processing within scripts.

73. New-PnPField (PnP.PowerShell)
Creates a new field in a SharePoint list or library. Supports defining field types, settings, and validations for structured data management.

74. Get-AzureADServicePrincipal (AzureAD)
Retrieves information about service principals in Azure Active Directory. Used to manage application identities and their associated permissions.

75. New-Object (Microsoft.PowerShell.Utility)
Creates an instance of a .NET Framework or COM object in PowerShell. Essential for handling complex data structures and interacting with .NET classes.

76. ConvertFrom-SecureString (Microsoft.PowerShell.Security)
Transforms a secure string object back into plain text. Should be used cautiously to avoid exposing sensitive information.

77. Write-Verbose (Microsoft.PowerShell.Utility)
Outputs detailed information during script execution when the verbose preference is enabled. Aids in debugging and understanding script flow.

78. Write-Debug (Microsoft.PowerShell.Utility)
Outputs debug information during script execution when the debug preference is enabled. Useful for in-depth troubleshooting and script analysis.

79. Invoke-WebRequest Parameters (Microsoft.PowerShell.Utility)
Includes -Method, -Uri, -Headers, -Body, and others. Facilitates detailed HTTP request configurations for interacting with web services.

80. PowerShell Pipeline
A feature that allows the output of one cmdlet to be passed as input to another cmdlet. Enables chaining commands for efficient data processing.

81. SecureString (System.Security)
Represents text that should be kept confidential, such as passwords. Provides methods to encrypt and handle sensitive information securely in scripts.

82. Export-Clixml (Microsoft.PowerShell.Utility)
Serializes PowerShell objects to an XML format file. Useful for securely storing complex objects, including credentials, for later retrieval.

83. Import-Clixml (Microsoft.PowerShell.Utility)
Deserializes PowerShell objects from an XML format file. Allows retrieving previously exported objects, maintaining their original structure and properties.

84. Environment Variables
Variables that are set at the operating system level and accessible within PowerShell. Used to store configuration data and secrets securely without hardcoding.

85. Retry Logic
A programming practice where failed operations are attempted again after a delay. Essential for handling transient errors like API throttling or network issues.

86. Exponential Backoff
A strategy for retrying failed operations with increasing delays between attempts. Helps in mitigating the impact of transient failures and reducing load on services.

87. Chained Cmdlets
Using multiple cmdlets in a sequence where each cmdlet processes data output from the previous one. Enhances script efficiency and readability.

88. Function Definitions
Custom reusable blocks of code in PowerShell scripts. Allows encapsulating logic for repeated tasks, improving maintainability and modularity.

89. PowerShell Profiles
Scripts that run automatically when PowerShell starts. Used to customize the environment, load modules, and define functions for enhanced productivity.

90. SharePoint CSOM (Client-Side Object Model)
A programming model that allows interaction with SharePoint data from client applications. Provides an alternative to REST API for performing SharePoint operations.

91. PowerShell Scopes
Defines the visibility and lifetime of variables and functions within PowerShell. Includes global, script, and local scopes, managing how data is accessed and modified.

92. Secure Password Handling
Practices for managing passwords securely in scripts, such as using ConvertTo-SecureString and PSCredential objects, to prevent exposure of sensitive information.

93. JSON Payloads
Data formatted in JSON used in REST API requests and responses. PowerShell uses ConvertTo-Json and ConvertFrom-Json for handling JSON data structures.

94. PowerShell Modules
Packages containing cmdlets, functions, and scripts that extend PowerShell's capabilities. Examples include PnP.PowerShell and AzureAD, facilitating specialized tasks.

95. HTTP Status Codes
Standardized codes returned by web servers indicating the result of an HTTP request. Examples include 200 OK, 403 Forbidden, and 404 Not Found.

96. SharePoint Permissions Levels
Predefined or custom permission sets in SharePoint that determine user access rights, such as Read, Contribute, and Full Control, managing what actions users can perform.

97. App-Only Authentication
A mode where applications authenticate without a user context, using client credentials to perform operations based on granted permissions. Suitable for automated scripts and services.

98. Delegated Permissions
Permissions granted to applications to act on behalf of a signed-in user. Requires user consent and is used in interactive authentication scenarios.

99. Token Expiry
The duration an OAuth 2.0 access token remains valid before needing renewal. Scripts must handle token refresh logic to maintain uninterrupted API access.

100. PowerShell Remoting
A feature allowing commands to be executed on remote computers. Facilitates managing SharePoint servers and other remote systems through PowerShell scripts.