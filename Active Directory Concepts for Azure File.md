Active Directory Concepts for Azure Files

Domain
A logical security boundary and namespace (e.g., corp.contoso.com) that contains users, computers, and policies.

Computer Account
An AD object that represents a machine. Azure Files uses a pre-staged computer account to act as its “identity” for Kerberos.

User Account
An AD object representing a person or service. Not recommended for Azure Files because passwords usually expire.

Security Identifier (SID)
A unique, immutable identifier for an AD object. Used internally by Windows for access control. You’ll need the SID of the Azure Files computer account for Terraform.

Service Principal Name (SPN)
An attribute on an AD object that maps a service instance to that account. For Azure Files, the SPN is:
cifs/<storageaccount>.file.core.windows.net

Delegation of Control
Giving a non-admin user rights over a specific OU or object type (e.g., create/delete computer objects). Enables least-privilege administration.

unicodePwd Attribute
The AD attribute that stores the password for a user or computer account. For Azure Files, this is set to the storage account’s Kerberos key (kerb1/kerb2).

userAccountControl Attribute
A bitmask controlling properties of an AD account (enabled, disabled, password never expires, etc.). Not where the Kerberos key lives.

Kerberos Key (Storage Account key)
A secret (kerb1 or kerb2) generated on the storage account. Written to the computer account’s password so Kerberos tickets can be validated.

Key Distribution Center (KDC)
A service running on domain controllers that issues Kerberos tickets (TGTs and service tickets).

Kerberos Ticket Granting Ticket (TGT)
A Kerberos ticket issued to a user when they log in. Used to request service tickets from the KDC.

Kerberos Service Ticket
A ticket issued by the KDC for a specific SPN (e.g., cifs/storageacct.file.core.windows.net). Encrypted with the Kerberos key stored in AD.

KRB_AP_ERR_MODIFIED
Kerberos error meaning “the service ticket could not be validated by the target.” In Azure Files, this usually indicates the Kerberos key in AD doesn’t match the storage account’s key.

Duplicate SPN
A misconfiguration where two AD objects both claim the same SPN. Kerberos can’t decide which to use, so authentication fails.

Domain SID
The SID of the domain itself. Passed into Azure Files configuration so it can translate user/group SIDs correctly for access checks.

NetBIOS Domain Name
The short (pre–DNS) name for a domain, often all caps (e.g., CORP). Still required for some AD integrations like Azure Files.

Private Endpoint DNS Resolution
Clients mounting Azure Files over Kerberos must resolve the file endpoint (<storageaccount>.file.core.windows.net) to the private endpoint’s IP.


Active Directory Domain Services (AD DS)
The directory service role in Windows Server that provides authentication, authorization, and directory lookups. Runs on domain controllers.

Global Catalog (GC)
A special role of certain domain controllers. Stores a partial replica of all objects in the forest. Helps with lookups across domains.

Forest Functional Level (FFL) / Domain Functional Level (DFL)
Settings that define which AD features are available, based on the OS version of your DCs. Can matter when integrating newer features like Azure AD Connect.

DNS in AD
AD-integrated DNS zones store the records that let clients locate DCs (_kerberos._tcp, _ldap._tcp). Without this, Kerberos won’t work.

SRV Records
DNS records used to locate services (e.g., _kerberos._tcp.corp.contoso.com points to DCs that provide Kerberos).

Access Control Entry (ACE)
An individual line in an ACL (e.g., “Group=Accounting, Permission=Read”).

Discretionary ACL (DACL)
Defines who is allowed or denied access. The type you’ll be working with when setting NTFS permissions on Azure Files.

System ACL (SACL)
Defines which actions are audited in security logs. Less common but may appear in compliance discussions.

Token Groups
When a user logs in, AD builds a token containing all their SIDs (user SID + group SIDs). This token is compared against ACLs.

SIDHistory
An attribute that holds old SIDs when accounts are migrated. Ensures access continuity. Relevant if you ever migrate domains and still want Azure Files ACLs to work.

NTLM Authentication
Older, fallback authentication method. If Kerberos fails (e.g., due to missing SPN), clients may try NTLM. Azure Files AD integration doesn’t support NTLM, so SPNs and Kerberos are required.

Kerberos Double-Hop
A delegation problem where a credential can’t be passed to a second server. Not directly in Azure Files, but explains why Kerberos delegation rules exist.

Kerberos Constrained Delegation (KCD)
Allows a service to impersonate users only to specific services. Again, not core to Azure Files, but important context for how Kerberos is normally “tightly scoped.”

Ticket Granting Service (TGS)
The Kerberos service on the DC that issues service tickets (based on your TGT).

Time Skew
Kerberos is sensitive to clock drift. If a client and DC differ by more than ~5 minutes, tickets are rejected. Important when mixing on-prem and cloud.

Port 445 (SMB over TCP)
Required for SMB traffic. Many ISPs block this outbound, so Azure Files is usually used over VPN or ExpressRoute with a private endpoint.

Azure Private Endpoint
A network interface in your VNet that maps a private IP to a PaaS resource. For Azure Files, it’s how on-prem clients connect securely without relying on public 445.

Azure DNS Private Zone
Used to override DNS resolution of <storageaccount>.file.core.windows.net so it resolves to your private endpoint. Critical for Kerberos because the SPN must match.

Azure AD DS (Managed Domain)
A hosted domain service in Azure that provides AD DS without full domain controllers. Some orgs use this for Azure Files instead of extending their on-prem AD.

Azure Entra ID Kerberos (AAD Kerberos)
A newer model where Entra ID itself issues Kerberos tickets. Removes dependency on on-prem AD DS but behaves slightly differently.