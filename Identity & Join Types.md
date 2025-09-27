 Identity & Join Types
Hybrid Identity: A user identity synchronized between on-prem AD DS and Microsoft Entra ID.
Microsoft Entra Join: Device is joined directly to Entra ID (formerly Azure AD).
Hybrid Join: Device is joined to both on-prem AD and Entra ID.
Domain Join: Traditional AD DS join, used in on-prem environments.
Enterprise Registration: Device is registered with Entra ID but not joined.
🔄 Synchronization & Trust
Microsoft Entra Connect: Tool to sync identities between AD DS and Entra ID.
Password Hash Sync (PHS): Syncs password hashes to Entra ID for seamless login.
Pass-through Authentication (PTA): Authenticates users against AD DS in real time.
Federation (AD FS): Redirects authentication to AD FS; used in complex hybrid setups.
Cloud Kerberos Trust: Allows Entra ID to issue Kerberos tickets without direct access to domain controllers.
🧱 Kerberos & Authentication
Microsoft Entra Kerberos: Cloud-native KDC that issues Kerberos tickets for hybrid users.
AzureADKerberos Computer Object: Special AD object used by Entra Kerberos to issue tickets.
Kerberos Constrained Delegation (KCD): Allows services to impersonate users and request Kerberos tickets.
TGT (Ticket Granting Ticket): Core Kerberos credential used to access services.
SPN (Service Principal Name): Identifier for services in Kerberos authentication.
⚙️ VM & Extension Configuration
System Assigned Managed Identity: Identity assigned to the VM for authenticating to Azure services and Entra ID.
AADLoginForWindows Extension: VM extension that enables Entra login and triggers Entra join.
mdmId: Identifier for the MDM provider (usually the Entra tenant ID or Intune app ID).
MDM User Scope: Determines which users auto-enroll into Intune; required for Entra join to succeed.
🛠️ Command-Line Tools & Diagnostics
Tool	Command	Purpose
dsregcmd	/status	Check Entra join, domain join, and device registration status.
/leave	Unjoin the device from Entra ID.
klist	(no args)	View current Kerberos tickets.
purge	Clear all Kerberos tickets.
nltest	/dsgetdc:<domain>	Find domain controllers.
/query	Query trust relationships.
whoami	/groups	View group memberships and SIDs.
PowerShell	Install-Module AzureADHybridAuthenticationManagement	Manage Entra Kerberos server object.