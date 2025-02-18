Azure Compute Gallery (ACG) Vocabulary List
1. Compute Gallery Concepts
Azure Compute Gallery (ACG) – A service that helps manage, share, and distribute VM images across multiple subscriptions and regions.
Compute Gallery Resource – The top-level container that stores multiple image definitions and versions.
Subscription Scope – ACG is tied to a single subscription, but images can be shared across multiple subscriptions under the same Azure AD tenant.
Resource Group – A logical container that holds the Compute Gallery, Image Definitions, and Image Versions.
Cross-Subscription Sharing – ACG images can be shared with multiple subscriptions, but not across Azure AD tenants.
Cross-Tenant Sharing – Not supported in ACG; images cannot be shared between different Azure Active Directory (Azure AD) tenants.
2. Image Structure
Image Definition – A logical representation of an image, specifying OS type, publisher, and general metadata.
Image Version – A specific iteration of an image (e.g., 1.0.0, 2.1.0), stored in one or more regions.
Image Gallery Replication – The process of copying an image version to multiple regions to optimize availability and speed.
Replication Region Limit – Each image version can be replicated to a maximum of 50 regions.
Image Retention Policy – A strategy for keeping or removing older image versions to manage storage costs and subscription quotas.
3. Image Types
Generalized Image – A VM image that has been "cleaned" of system-specific data (using Sysprep for Windows or waagent -deprovision for Linux) to be reused across multiple VM deployments.
Specialized Image – A VM image that retains system-specific settings, including machine name, user accounts, and configurations—ideal for cloning.
Managed Image – A single, region-bound image stored in Azure, lacking versioning and replication features found in ACG.
OS Disk Image – An image containing only the operating system and configurations.
Data Disk Image – A separate image that includes application and data disks but does not contain an OS.
Shared Image – An image in ACG that is accessible across multiple subscriptions with proper RBAC configuration.
4. Image Creation Methods
Manual Image Creation
Capture from Existing VM – Creating an image by generalizing or specializing a VM and capturing it into ACG.
Manual VHD Upload – A process where you create a VHD file, upload it to Azure Storage, and convert it into an image.
Azure Marketplace Image as a Base – Using a pre-configured image from Azure Marketplace to deploy new VMs.
Automated Image Creation
Azure Image Builder (AIB) – A managed service that automates image creation by defining customizations (e.g., software installations, updates, configurations).
Packer – An open-source tool that automates multi-cloud VM image building, often used with Terraform or Azure DevOps.
Terraform Compute Gallery Module – A way to define ACG image builds and deployments using Infrastructure as Code (IaC).
Azure DevOps Pipelines for Image Deployment – A CI/CD workflow that automatically builds, tests, and publishes images.
5. Deployment & Access
VM Deployment from ACG – The process of creating VM instances using images stored in Azure Compute Gallery.
Shared Image Gallery Reader Role – An RBAC role that allows users to access images for deployment but not modify them.
Deployment Latency – The time required for a newly published image to become available for VM creation.
Ephemeral OS Disk – A temporary VM disk that cannot be used with ACG images.
Replication Completion Check – Before deploying a VM, images must be fully replicated to the region where deployment is taking place.
6. Versioning & Storage
Semantic Versioning (SemVer) – The required format (X.Y.Z, e.g., 1.0.0) for ACG image versions.
Immutable Image Versions – Once an image version is published, it cannot be modified—a new version must be created.
Maximum Image Versions Per Definition – Each image definition can store up to 1,000 versions.
Storage Costs for ACG – Storage pricing depends on:
Number of versions retained
Number of replicas in different regions
Image size
Image Version Deletion – Permanent action that cannot be undone.
7. Security & Access Control
RBAC (Role-Based Access Control) – Azure's permission model for granting access to ACG images.
Azure Compute Gallery Roles:
Reader – Can list and read images.
Contributor – Can create and manage images.
Owner – Full control over the gallery.
Shared Image Gallery Reader – Read-only access to images across subscriptions.
SAS Token (Shared Access Signature) – A temporary, secure URL-based access method often used for sharing VHD files in Azure Storage.
8. Planning & Limitations
Subscription & Region Restrictions
One Compute Gallery Per Subscription – ACG is bound to a single Azure subscription.
Region Availability – Not all Azure regions support Compute Gallery replication.
Azure Government & Sovereign Clouds – Some regions (e.g., China, US Gov) have restricted ACG availability.
Quota & Scaling Limits
Subscription Quotas – Limits on the number of image versions, definitions, and replication regions.
Replication Time Constraints – Image replication is not instantaneous and can take several minutes to hours.
Governance & Compliance
Azure Policy Enforcement – Some organizations restrict Compute Gallery usage via Azure Policies.
License Considerations – Some images (e.g., RHEL, Windows Server) require Azure Hybrid Benefit or additional licensing.
9. Key Takeaways
Azure Compute Gallery allows scalable, multi-region image management, but requires careful subscription, replication, and versioning planning.
Image versions are immutable – Plan versioning strategies carefully.
Replication increases storage costs – Select replication regions strategically.
RBAC must be explicitly assigned – Cross-subscription access is not automatic.
Automation (AIB, Packer, Terraform) improves efficiency – Use DevOps workflows to standardize image creation.
10. Bonus: Acronyms & Short Terms
Term	Meaning
ACG	Azure Compute Gallery
AIB	Azure Image Builder
RBAC	Role-Based Access Control
SAS	Shared Access Signature
VHD	Virtual Hard Disk
VM	Virtual Machine
IaC	Infrastructure as Code
CI/CD	Continuous Integration/Continuous Deployment
SemVer	Semantic Versioning
Would You Like This as a Downloadable Note or a PDF? 📄🚀
This should help you quickly reference key terms as you work with Azure Compute Gallery!





You said:
removing

Throw in some more related terms 
ChatGPT said:
Absolutely! Here’s an expanded vocabulary list with additional related terms to give you the most comprehensive reference for working with Azure Compute Gallery (ACG), image creation, and VM deployment. 🚀

Azure Compute Gallery (ACG) & Image Management Vocabulary
1. Compute Gallery Concepts
Azure Compute Gallery (ACG) – A service that helps manage, share, and distribute VM images across multiple subscriptions and regions.
Shared Image Gallery (SIG) – The previous name for Azure Compute Gallery (Microsoft rebranded it).
Compute Gallery Resource – The top-level container that holds image definitions and versions.
Compute Gallery Replication – The process of copying image versions to multiple regions for faster VM deployments.
Subscription Scope – A Compute Gallery is tied to a single subscription, but images can be shared across subscriptions in the same Azure AD tenant.
Cross-Subscription Sharing – The ability to share Compute Gallery images with multiple subscriptions.
Cross-Tenant Sharing – Not supported in Compute Gallery; images cannot be shared across Azure Active Directory (Azure AD) tenants.
Regional Availability – Not all Azure regions support Compute Gallery; some government clouds and sovereign regions have restrictions.
2. Image Structure
Image Definition – A template that defines the OS, configurations, and metadata for an image.
Image Version – A specific iteration of an image (e.g., 1.0.0, 2.1.0).
Image Gallery Replication – The process of copying an image version to multiple Azure regions.
Replication Region Limit – Each image version can be replicated to a maximum of 50 regions.
Image Retention Policy – A strategy to keep or remove older image versions to optimize storage costs.
3. Image Types
Generalized Image – An image that has been prepared for reuse across multiple VMs by removing system-specific data.
Specialized Image – An image that retains all system settings, making it suitable for cloning instead of mass deployment.
Managed Image – A single-instance VM image stored in Azure but lacks the replication/versioning benefits of Compute Gallery.
OS Disk Image – An image that contains only the operating system and its configurations.
Data Disk Image – An image that contains application or data disk information, but no OS.
Shared Image – An image in Compute Gallery that can be accessed across multiple subscriptions.
Golden Image – A fully configured and security-hardened VM image used as the standard baseline for deployments.
4. Image Creation Methods
Manual Image Creation
Capture from Existing VM – Creating an image by generalizing or specializing a VM and capturing it into Compute Gallery.
Manual VHD Upload – The process of creating a VHD file, uploading it to Azure Storage, and converting it into an image.
Azure Marketplace Image as a Base – Using a pre-configured image from Azure Marketplace to create new VM images.
Automated Image Creation
Azure Image Builder (AIB) – A managed service that automates the customization and publishing of VM images.
Packer – A multi-cloud image builder used for creating VM images in Azure, AWS, and other cloud platforms.
Terraform Compute Gallery Module – A way to define Compute Gallery images using Infrastructure as Code (IaC).
Azure DevOps Pipelines for Image Deployment – A CI/CD process that automates image creation, testing, and publishing.
5. Deployment & Access
VM Deployment from ACG – The process of creating VMs from images stored in Compute Gallery.
Shared Image Gallery Reader Role – An RBAC role that allows users to access images for deployment but not modify them.
Deployment Latency – The time required for a newly published image to become available for VM creation.
Ephemeral OS Disk – A temporary VM disk that cannot be used with Compute Gallery images.
Replication Completion Check – Before deploying a VM, images must be fully replicated to the region where deployment is taking place.
6. Versioning & Storage
Semantic Versioning (SemVer) – The required versioning format (X.Y.Z, e.g., 1.0.0).
Immutable Image Versions – Once an image version is published, it cannot be modified; a new version must be created.
Maximum Image Versions Per Definition – Each image definition can store up to 1,000 versions.
Image Version Deletion – Permanent action that cannot be undone.
Storage Costs for ACG – Pricing depends on:
Number of versions retained
Number of replica regions
Size of images stored
Snapshot vs. Image – A snapshot is a point-in-time backup of a disk, while an image is a reusable VM template.
7. Security & Access Control
RBAC (Role-Based Access Control) – Azure’s permission model for granting access to ACG images.
Azure Compute Gallery Roles:
Reader – Can view and list images.
Contributor – Can create and manage images.
Owner – Full control over the Compute Gallery.
Shared Image Gallery Reader – Read-only access to images across subscriptions.
SAS Token (Shared Access Signature) – A temporary, secure URL-based access method for sharing VHD files in Azure Storage.
Private Endpoint for Compute Gallery – A network security feature that restricts access to the gallery within a private virtual network (VNet).
Customer-Managed Keys (CMK) – Encryption keys controlled by your organization instead of using Azure-managed encryption.
8. Planning & Limitations
Subscription & Region Restrictions
One Compute Gallery Per Subscription – ACG is tied to a single subscription.
Region Availability – Not all Azure regions support Compute Gallery replication.
Azure Government & Sovereign Clouds – Some regions (China, US Gov) have restricted Compute Gallery availability.
Quota & Scaling Limits
Subscription Quotas – Limits on the number of image versions, definitions, and replication regions.
Replication Time Constraints – Image replication is not instant and can take minutes to hours.
Governance & Compliance
Azure Policy Enforcement – Some organizations restrict Compute Gallery usage via Azure Policies.
License Considerations – Some images (e.g., RHEL, Windows Server) require Azure Hybrid Benefit or additional licensing.
