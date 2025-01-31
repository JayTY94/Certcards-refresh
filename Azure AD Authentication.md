1. App Registration
Registers an app in Azure AD, creating its identity to authenticate with Azure services. Allows the app to access resources and interact with Azure services.

2. Service Principal
A security identity for an app to authenticate and access Azure resources. Used for automated services and applications instead of using user credentials.

3. Role-Based Access Control (RBAC)
Manages who can access Azure resources and what actions they can perform by assigning roles to users, groups, or Service Principals at specific scopes.

4. Role Assignment
Links a principal (user, group, service principal) to a role at a defined scope, granting specific permissions to interact with Azure resources.

5. Scope
Defines the level at which a role is applied, such as management group, subscription, resource group, or individual resource. Higher scopes apply to all child resources.

6. Principal
An identity (user, group, service principal) that is granted access to Azure resources based on assigned roles.

7. Built-In Roles
Predefined roles like Owner, Contributor, and Reader that grant specific permissions to manage Azure resources at various scopes.

8. Custom Roles
User-defined roles with specific permissions, used when built-in roles don’t provide the required access or for more granular control.

9. Role Inheritance
Roles assigned at a higher scope (e.g., subscription) are inherited by resources at lower scopes (e.g., resource groups, resources).

10. Managed Identities
Azure-managed identities used by Azure resources (like VMs) to authenticate to other Azure services, removing the need to manage credentials.

11. App Registration vs Enterprise Application
App Registration defines the app’s identity, while Enterprise Application represents the actual instance of the app within an Azure AD tenant.

12. Service Principal Authentication Methods
Authentication for service principals can be done using Client Secret, Client Certificate, or Managed Identity, which provides secure, credential-free access to Azure services.

13. Conditional Access Policies
Policies that enforce secure access to resources based on conditions like user location, device, or risk level, helping secure Azure resource access.

14. Azure Role Assignment Best Practices
Apply the least privilege principle, assign roles at the resource group level, and minimize Owner role usage to reduce security risks.

15. Role Assignment Propagation
Role permissions may take time to propagate across Azure, so changes in role assignments might not be immediately reflected in access control.

16. Azure AD Roles vs Azure Resource Roles
Azure AD Roles manage access to directory functions (e.g., Global Administrator), while Resource Roles control access to Azure resources (e.g., Contributor).

Let me know if you'd like to adjust or expand on any of these!
