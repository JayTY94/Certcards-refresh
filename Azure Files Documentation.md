






33
Azure Files Documentation
In general, mounting a file share can be simply achieved on Windows using a standard “net use” command. When you create a share, the Azure Portal automatically generates a “net use” command and makes it available for copy and pasting: look for the "Connect" button.





34
Azure Files Documentation
Use of different clients, SMB versions, firewall rules, ISPs, or IT policies can affect connectivity to Azure Files. Good news is AzFileDiagnostics isolates and examines each source of possible issues and in turn provides you with advice or workarounds to correct the problem.





35
Azure Files Documentation
You can access your Azure file shares over the public internet accessible endpoint, over one or more private endpoints on your network(s), or by caching your Azure file share on-premises with Azure File Sync (SMB file shares only).





36
Azure Files Documentation
SMB file shares communicate over port 445, which many organizations and internet service providers (ISPs) block for outbound (internet) traffic. This practice originates from legacy security guidance about deprecated and non-internet safe versions of the SMB protocol. SMB 3.x does not share these vulnerabilities.





37
Azure Files Documentation
NFS file shares rely on network-level authentication and are therefore only accessible via restricted networks. Using an NFS file share always requires some level of networking configuration.







38
Azure Files Documentation
For Azure Files, the Secure transfer required setting is enforced for all protocol access to the data stored on Azure file shares, including SMB, NFS, and FileREST. You can disable the Secure transfer required setting to allow unencrypted traffic.







39
Azure Files Documentation
NFS file shares are accessible from the storage account's public endpoint if and only if the storage account's public endpoint is restricted to specific virtual networks using service endpoints. See public endpoint firewall settings for additional information on service endpoints.







40
Azure Files Documentation
The Windows Server operating systems implement the Kerberos version 5 authentication protocol and extensions for public key authentication, transporting authorization data, and delegation.





1
Azure Files Documentation
The Kerberos authentication client is implemented as a security support provider (SSP), and it can be accessed through the Security Support Provider Interface (SSPI). Initial user authentication is integrated with the Winlogon single sign-on architecture.





2
Azure Files Documentation
The Kerberos Key Distribution Center (KDC) is integrated with other Windows Server security services that run on the domain controller. The KDC uses the domain's Active Directory Domain Services database as its security account database. Active Directory Domain Services is required for default Kerberos implementations within the domain or forest.







3
Azure Files Documentation
Beginning with Windows Server 2025, Kerberos no longer honors the legacy registry key REG_DWORD SupportedEncryptionTypes found in the path HKEY_LOCAL_MACHINE\CurrentControlSet\Control\Lsa\Kerberos\Parameters. Microsoft recommends using group policy instead.





4
Azure Files Documentation
The set of message packets that defines a particular version of the protocol is called a dialect. The Common Internet File System (CIFS) Protocol is a dialect of SMB. Both SMB and CIFS are also available on VMS, several versions of Unix, and other operating systems.







5
Azure Files Documentation
In the OSI networking model, Microsoft SMB Protocol is most often used as an Application layer or a Presentation layer protocol, and it relies on lower-level protocols for transport. The transport layer protocol that Microsoft SMB Protocol is most often used with is NetBIOS over TCP/IP (NBT). 





6
Azure Files Documentation
SMB Multichannel enables file servers to use multiple network connections simultaneously. It facilitates aggregation of network bandwidth and network fault tolerance when multiple paths are available between the SMB 3.0 client and the SMB 3.0 server.





7
Azure Files Documentation
Azure Files supports SMB Multichannel on SSD file shares for Windows clients. On the service side, SMB Multichannel is now enabled by default for all newly created storage accounts in all Azure regions. There's no extra cost for enabling SMB Multichannel.







8
Azure Files Documentation
Azure File Sync enables you to centralize your organization's file shares in Azure Files, while keeping the flexibility, performance, and compatibility of an on-premises file server. Azure File Sync transforms an on-premises (or cloud) Windows Server into a quick cache of your SMB Azure file share.





9
Azure Files Documentation
Azure File Sync enables you to centralize your organization's file shares in Azure Files transforming an on-premises (or cloud) Windows Server into a quick cache of your SMB Azure file share.





10
Azure Files Documentation
File shares (preview), offered by the Microsoft.FileShares resource provider. File shares are a new top-level resource that simplify the deployment of Azure Files by eliminating the storage account. Unlike classic file shares, which must be deployed into a storage account, file shares are deployed directly into the resource group like storage accounts themselves





11
Azure Files Documentation
Classic file shares, and the child objects for other storage services like blob containers, that live within the same storage account share a common pool of storage, IOPS, and throughput. This means placing multiple classic file shares in a storage account requires planning to avoid capacity bottlenecks





12
Azure Files Documentation
Many important settings, such as network and security rules, are applied at the storage account level. You should consider the storage account to be a trust boundary and only place classic file shares in the same storage account if you're ok with them having the same security settings.







13
Azure Files Documentation
Provisioned storage accounts are distinguished using the FileStorage storage account kind. Provisioned storage accounts allow you to deploy provisioned classic file shares on either SSD or HDD based hardware. We recommend using provisioned storage accounts for all new classic file share deployments.





14
Azure Files Documentation
Pay-as-you-go storage accounts are distinguished using the StorageV2 storage account kind. 
They allow you to deploy file shares on HDD based hardware. 
They can be used to store classic file shares and other storage resources such as blob containers, queues, or tables.






15
Azure Files Documentation
Using the storage account key to mount the Azure file share is effectively an administrator operation, because the mounted file share has full permissions to all of the files and folders on the share, even if they have ACLs. When using the storage account key to mount over SMB, the NTLMv2 authentication protocol is used.





16
Azure Files Documentation
Soft delete is a storage-account level setting that allows you to recover your file share when it's accidentally deleted. When a file share is deleted, it transitions to a soft deleted state instead of being permanently erased. You can configure the amount of time soft deleted shares are recoverable before they're permanently deleted.






17
Azure Files Documentation
You can back up your Azure file share via share snapshots, which are read-only, point-in-time copies of your share. Snapshots are incremental, meaning they only contain as much data as has changed since the previous snapshot. You can have up to 200 snapshots per file share and retain them for up to 10 years.





18
Azure Files Documentation
Azure Backup for Azure file shares handles the scheduling and retention of snapshots. Its grandfather-father-son (GFS) capabilities mean that you can take daily, weekly, monthly, and yearly snapshots, each with their own distinct retention period.





19
Azure Files Documentation
You can perform both item-level and share-level restores in the Azure portal using Azure Backup. All you need to do is choose the restore point (a particular snapshot), the particular file or directory if relevant, and then the location (original or alternate) you wish you restore to.





20
Azure Files Documentation
HDD file shares support all four redundancy types. SSD file shares support only LRS and ZRS.







21
Azure Files Documentation






22
Azure Files Documentation






23
Azure Files Documentation






24
Azure Files Documentation






25
Azure Files Documentation






26
Azure Files Documentation






27
Azure Files Documentation






28
Azure Files Documentation






29
Azure Files Documentation






30
Azure Files Documentation






31
Azure Files Documentation






32
Azure Files Documentation






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






