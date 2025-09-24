1
Azure Files Documentation
The procedures for changing the size, cost, and performance characteristics for Azure File Shares are different for classic file shares, which use the Microsoft.Storage resource provider, versus file shares created with Microsoft.FileShares (preview).







2
Azure Files Documentation
The amount of storage, IOPS, and throughput you provision can be dynamically scaled up or down as your needs change. However, you can only decrease a provisioned quantity after 24 hours have elapsed since your last quantity increase. 





3
Azure Files Documentation
To toggle paid bursting, use the --paid-bursting-enabled parameter. Paid bursting is an advanced feature of the provisioned v1 model. Consult provisioned v1 paid bursting before enabling.





4
Azure Files Documentation
The access tier of the file share dictates to the ratio of storage to IOPS/throughput costs (in the form of transactions). There are three access tiers: transaction optimized, hot, and cool. Changing the tier of the Azure file share results in transaction costs for the movement to the new access tier. 





5
Azure Files Documentation
Quota is a limit on the size of the file share. The quota property is used in the provisioned v2 and provisioned v1 models to mean "provisioned storage capacity", however, in the pay-as-you-go model, quota has no direct impact on bill. 





6
Azure Files Documentation
To enable AD DS authentication over SMB for Azure file shares, you need to register your Azure storage account with your on-premises AD DS and then set the required domain properties on the storage account. To register your storage account with AD DS, you create a computer account (or service logon account) representing it in your AD DS. 





7
Azure Files Documentation
To register your storage account with AD DS, you create a computer account (or service logon account) representing it in your AD DS. Think of this process as if it were like creating an account representing an on-premises Windows file server in your AD DS. 





8
Azure Files Documentation
The AzFilesHybrid PowerShell module provides cmdlets for deploying and configuring Azure Files. It includes cmdlets for domain joining storage accounts to your on-premises Active Directory and configuring your DNS servers. It's provided in a .zip linked to in the learn.microsoft.com article.





9
Azure Files Documentation
# Create the Kerberos key on the storage account and get the Kerb1 key as the password for the AD identity 
# to represent the storage account
$ResourceGroupName = "<resource-group-name-here>"
$StorageAccountName = "<storage-account-name-here>"

New-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $StorageAccountName -KeyName kerb1
Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $StorageAccountName -ListKerbKey | where-object{$_.Keyname -contains "kerb1"}





10
Azure Files Documentation
If your OU containing the storage account's computer account enforces password expiration, you must update the password before the maximum password age to prevent authentication failures when accessing Azure file shares. See Update the password of your storage account identity in AD for details.





11
Azure Files Documentation
In order to enable AES-256 encryption, the domain object that represents your storage account must be a computer account (default) or service logon account in the on-premises AD domain. If your domain object doesn't meet this requirement, delete it and create a new domain object that does.







12
Azure Files Documentation
Azure Files supports identity-based authentication for Windows file shares over Server Message Block (SMB) using the Kerberos authentication protocol through the following methods:

    On-premises Active Directory Domain Services (AD DS)
    Microsoft Entra Domain Services
    Microsoft Entra Kerberos for hybrid user identities





13
Azure Files Documentation
To assign share-level RBAC permissions to specific users or groups, on-premises AD DS identities must be synced to Microsoft Entra ID using Entra Connect Sync. If identities aren't synced, you must use a default share-level permission, which applies to all authenticated users





14
Azure Files Documentation
Kerberos authentication is available with Active Directory using AES 256 encryption (recommended) and RC4-HMAC. AES 128 Kerberos encryption isn't yet supported.





15
Azure Files Documentation
By default access is limited to the Active Directory forest where the storage account is registered. Users from any domain in that forest can access the file share contents, provided they have the appropriate permissions. 





16
Azure Files Documentation
If a machine isn't domain joined, you can still use AD DS for authentication if the machine has unimpeded network connectivity to the on-premises AD domain controller and the user provides explicit credentials. For more information, see Mount the file share from a non-domain-joined VM or a VM joined to a different AD domain.







17
Azure Files Documentation
Enabling AD DS authentication for your Azure file shares allows you to authenticate to your Azure file shares with your on-premises AD DS credentials. Further, it allows you to better manage your permissions to allow granular access control.





18
Azure Files Documentation
When using AD DS authentication, you assign share-level permissions to hybrid identities synced to Microsoft Entra ID while managing file/directory-level access using Windows ACLs.





19
Azure Files Documentation
Azure file shares use the Kerberos protocol to authenticate with an identity source. When an identity associated with a user or application running on a client attempts to access data in Azure file shares, the request is sent to the identity source to authenticate the identity. 





20
Azure Files Documentation
If a client successfully authenticates to an identity source, that identity source returns a Kerberos ticket. Azure Files authenticates requests with that Kerberos ticket, not user credentials.





21
Azure Files Documentation
If you're keeping your primary file storage on-premises, Azure Files is an ideal solution for backup and DR to improve business continuity. You can use Azure file shares to back up your file servers while preserving Windows discretionary access control lists (DACLs). 





22
Azure Files Documentation
You can enable identity-based authentication over SMB using one of three identity sources: On-premises Active Directory Domain Services (AD DS), Microsoft Entra Domain Services, or Microsoft Entra Kerberos (hybrid identities only). You can only use one identity source for file access authentication per storage account.





23
Azure Files Documentation
For Microsoft Entra Domain Services authentication, you must enable Microsoft Entra Domain Services and domain-join the VMs you plan to access file data from. Your domain-joined VM must reside in the same VNET as your Microsoft Entra Domain Services hosted domain.







24
Azure Files Documentation
Hybrid identities

Hybrid user identities are identities in AD DS that are synced to Microsoft Entra ID using either the on-premises Microsoft Entra Connect Sync application or Microsoft Entra Connect cloud sync, a lightweight agent that can be installed from the Microsoft Entra Admin Center.







25
Azure Files Documentation
On-premises Active Directory Domain Services (AD DS)

AD DS is commonly adopted by enterprises in on-premises environments or on cloud-hosted VMs, and AD DS credentials are used for access control. For more information, see Active Directory Domain Services Overview.





26
Azure Files Documentation
Microsoft Entra Domain Services

Microsoft Entra Domain Services provides managed domain services such as domain join, group policies, LDAP, and Kerberos/NTLM authentication. These services are fully compatible with Active Directory Domain Services. For more information, see Microsoft Entra Domain Services.







27
Azure Files Documentation
Azure AD Connect V1 has been retired as of August 31, 2022 and is no longer supported. Azure AD Connect V1 installations may stop working unexpectedly. If you are still using an Azure AD Connect V1 you need to upgrade to Microsoft Entra Connect V2 immediately.








28
Azure Files Documentation
Ensure port 445 is open: The SMB protocol requires TCP port 445 to be open. Connections will fail if port 445 is blocked. You can check if your firewall or ISP is blocking port 445 by using the Test-NetConnection PowerShell cmdlet. For more information, see Port 445 is blocked.







29
Azure Files Documentation
A storage account key is an administrator key for a storage account, including administrator permissions to all files and folders within the file share you're accessing, and for all file shares and other storage resources (blobs, queues, tables, etc.) contained within your storage account.





30
Azure Files Documentation
SMB Multichannel enables an SMB client to establish multiple network connections to an SMB file share. Azure Files supports SMB Multichannel on SSD file shares for Windows clients. On the service side, SMB Multichannel is now enabled by default for all newly created storage accounts in all Azure regions. There's no extra cost for enabling SMB Multichannel.







31
Azure Files Documentation
SMB Multichannel enables clients to use multiple network connections that provide increased performance while lowering the cost of ownership. Increased performance is achieved through bandwidth aggregation over multiple NICs and utilizing Receive Side Scaling (RSS) support for NICs to distribute the I/O load across multiple CPUs.







32
Azure Files Documentation
Metadata caching is an enhancement for SSD Azure file shares that reduces metadata latency and raises metadata scale limits. The feature increases latency consistency and available IOPS, and it boosts network throughput.







33
Azure Files Documentation






34
Azure Files Documentation






35
Azure Files Documentation






36
Azure Files Documentation






37
Azure Files Documentation






38
Azure Files Documentation






39
Azure Files Documentation






40
Azure Files Documentation






