




1
Azure Compute Gallery and Disk Architecture
Where can a new image version's source come from? 
A managed image, a snapshot, a VM, another existing image version, or a VHD. Cannot use a VM you don't have access to. Each source carries its own metadata that may or may not be compatible with your destination definition's feature flags.






2
Azure Compute Gallery and Disk Architecture
Frozen version metadata — the "PropertyChangeNotAllowed" trap 
hen you create an image version, the feature flags from its source (DiskControllerTypes, SecurityType) are baked into the version itself, not just inherited live from the definition. If you later try to use that version as a source for a new version under a different definition with different flags, Azure rejects it: gallery image property 'features' has a different value. Practical fix: rehydrate via a temp VM and recapture, or build fresh.






3
Azure Compute Gallery and Disk Architecture
Immutability of DiskControllerTypes 
Once an image definition is created with a given DiskControllerTypes value, you cannot change it. az sig image-definition update --set features=... will return (PropertyChangeNotAllowed). Set it correctly at birth or create a new definition.






4
Azure Compute Gallery and Disk Architecture
Default DiskControllerTypes when omitted 
If you don't specify DiskControllerTypes at definition creation, Azure assigns SCSI-only by default. This is why custom-captured images frequently can't deploy to v6/v7 SKUs even when nothing about the OS would prevent it.






5
Azure Compute Gallery and Disk Architecture
DiskControllerTypes = "SCSI, NVMe" 
A compatibility declaration — the image is fit to deploy on hosts of either controller type. The platform picks the right one at deploy time based on the destination SKU. Does not mean two disks are attached or that conversion happens.






6
Azure Compute Gallery and Disk Architecture
SecurityType flag values

    Standard — no Trusted Launch
    TrustedLaunch — Secure Boot + vTPM + measured boot
    ConfidentialVM — adds hardware memory encryption (AMD SEV-SNP / Intel TDX)

Set on the image definition. Required for the corresponding VM to deploy as that security type.






7
Azure Compute Gallery and Disk Architecture
Trusted Launch vs. Confidential VM 
Trusted Launch protects the boot chain (rootkits, tampered firmware) but the host hypervisor can still read VM memory. 
Confidential VM adds hardware memory encryption so even Microsoft hosts can't peek at RAM. 
Use Trusted Launch as the default; Confidential VM when "even the cloud provider is in your threat model."






8
Azure Compute Gallery and Disk Architecture
vTPM Virtual Trusted Platform Module. 
Provides measured boot — a tamper-evident log of what code ran during boot, signed by the TPM. Used for attestation: a remote service can verify a VM booted clean. Not a network or disk encryption feature, despite being lumped under "security."






9
Azure Compute Gallery and Disk Architecture
Hyper-V Generation 2 = UEFI + GPT 
    Gen 1 = Legacy BIOS + MBR. 
    Gen 2 = UEFI firmware + GPT partition table. 

Trusted Launch, Secure Boot, and vTPM all require Gen 2. Set hyper_v_generation = "V2" on the image definition. Captured Gen 1 images cannot be retrofitted — you'd need to recapture from a Gen 2 source VM.






10
Azure Compute Gallery and Disk Architecture
Sysprep /generalize — purpose 
Strips machine-specific identifiers (SID, computer name, drivers tied to specific hardware enumerations, activation tickets) so the image can deploy onto many new VMs without collisions. Does not compress, encrypt, or update.






11
Azure Compute Gallery and Disk Architecture
Sysprep 3-run limit 
You cannot sysprep /generalize the same Windows install more than 3 times. Each pass adds wear to activation tickets, the driver store, and component-based servicing state. Microsoft caps it to prevent corruption. Implication: never reuse a generalized image as the base of another build — start fresh each time.






12
Azure Compute Gallery and Disk Architecture
NVMe vs. SCSI — why NVMe wins on modern hardware 
SCSI was designed for single-head spinning disks: one command queue made sense. 
NVMe was designed for parallel SSDs from scratch: up to 65,535 queues, each up to 65,535 commands deep. On many-core CPUs, every core can run its own queue without contending through one bottleneck. The result is dramatically higher IOPS-per-vCPU.






13
Azure Compute Gallery and Disk Architecture
Why v6/v7 SKUs went NVMe-only 
The underlying AMD EPYC (and equivalent Intel) hosts wire physical NVMe SSDs directly to the CPU over PCIe. Virtualizing SCSI on top would mean NVMe→SCSI→NVMe translation, capping per-vCPU IOPS at a fraction of the silicon's potential. Microsoft cut SCSI on these SKUs to deliver the IOPS modern workloads expect.






14
Azure Compute Gallery and Disk Architecture
Standard_D8as_v7 won't boot from a SCSI-only image 
The host has no SCSI controller to present to the guest. The image's metadata says "I require SCSI." No compatible storage path exists, so the VM creation fails. Fix: tag the image definition DiskControllerTypes=SCSI, NVMe at creation, or use a v5/v6-compatible SKU instead.






15
Azure Compute Gallery and Disk Architecture
Local NVMe temp disk vs. NVMe-attached managed disk 
Local NVMe = host-physical SSDs on the mainboard, microsecond latency, wiped on stop-deallocate (different host on resume). NVMe-attached managed disk = ordinary durable Azure block storage (Premium SSD v2 etc.), just exposed to the guest via NVMe protocol instead of SCSI. Same durability as before, faster wire.






16
Azure Compute Gallery and Disk Architecture
stornvme.sys and friends Windows storage stack:

    Class driver: disk.sys (protocol-agnostic)
    Miniport drivers: storvsc.sys (Hyper-V virtual SCSI), storahci.sys (SATA), stornvme.sys (NVMe)

The miniport is what swaps when the controller swaps. disk.sys doesn't care.




17
Azure Compute Gallery and Disk Architecture
Why a "dual-controller" image works 
At capture time, both storvsc and stornvme driver INFs are present in the Windows driver store. Sysprep /generalize removes device-specific binding state but preserves the store. At first boot on the destination, PnP enumerates whatever controller it finds and binds the matching driver. If you ship only one, you're locked to that controller.






18
Azure Compute Gallery and Disk Architecture
Plug and Play (PnP) at first boot 
When a generalized Windows VM starts on a new host, very early in boot the kernel enumerates devices, looks up matching INFs in the local driver store, loads the right storage miniport, and only then mounts the boot volume. No internet, no Windows Update, no VM agent yet — just kernel and driver store. Missing driver = INACCESSIBLE_BOOT_DEVICE BSOD.






19
Azure Compute Gallery and Disk Architecture
Don't prune the driver store 
Some build pipelines shrink images by trimming the Windows driver store. If you trim out the destination controller's driver, you've built an unbootable image. Won't surface until deploy. Default: leave the store alone unless you know exactly which devices the image will face.






20
Azure Compute Gallery and Disk Architecture
Azure VM Agent (waagent / WindowsAzureGuestAgent) 
The daemon that turns a generic OS into "an Azure VM." On first boot, reads provisioning input from the Azure fabric (hostname, password, custom data, SSH keys), then enables extensions. If absent or broken in a captured image, VMs deploy but never finish provisioning — extensions never run, status sits at "Not Ready." Smoke-test extension push on every Packer output.




21
Azure Compute Gallery and Disk Architecture
Packer + ACG: standard flow

    Spin up a temporary build VM in a transient resource group Packer creates
    Install software, configure, run any tests
    Run sysprep /generalize
    Capture to a managed image (intermediate) or directly to a gallery version
    Tear down the temp resource group
    The transient resource group is owned and cleaned up by Packer — don't put anything else in it.






22
Azure Compute Gallery and Disk Architecture
Managed image vs. Gallery image version 
Managed image (Microsoft.Compute/images) = older single-region, unversioned, no replication, no sharing. 
Gallery version (Microsoft.Compute/galleries/images/versions) = modern, versioned, replicated, shareable. 
Managed images still appear as intermediate capture targets (the --managed-image flag on az sig image-version create). Don't end-state on a managed image.






23
Azure Compute Gallery and Disk Architecture
azurerm_shared_image vs. ARM feature flags — the gap 
Terraform's azurerm provider lags ARM API. As of v4.70 it does not expose DiskControllerTypes on azurerm_shared_image. 
When you need a feature azurerm doesn't surface, the right move is azapi_resource — same provider ecosystem, but you write the raw ARM JSON body. 
Don't manually edit Terraform state. Don't abandon IaC. Bridge with azapi.






24
Azure Compute Gallery and Disk Architecture
disk_controller_type on azurerm_windows_virtual_machine 
Tells Azure which controller protocol to use when attaching the OS disk to the guest at create time. 
Only valid when (a) the SKU supports that controller, AND (b) the source image's definition is tagged compatible with that controller. 
Setting it to NVMe on a v7 SKU with a SCSI-only image still fails — controller compatibility is gated at the image, not just the VM resource.






25
Azure Compute Gallery and Disk Architecture
replicaCount on a gallery image version 
Controls how many parallel copies of the version exist within each target region. Higher count = more deployment throughput, less throttling under burst (e.g., a 1000-VM scale-out). It does not control how many regions the version lives in — that's the regional replication list. Storage cost scales linearly with replica count.






26
Azure Compute Gallery and Disk Architecture
excludeFromLatest 
Hides the version from the :latest alias so default deployments skip it, while version-pinned deployments still succeed. Useful for staging a new version without auto-promoting it, or quarantining a bad version while leaving direct references working.






27
Azure Compute Gallery and Disk Architecture
endOfLifeDate behavior 
A label, not an enforcement. After the date, Azure annotates the version as past EOL but it remains deployable. No auto-delete, no auto-block, running VMs unaffected. If you need it gone, you delete it explicitly. Set EOL dates as a planning signal, not a kill switch.






28
Azure Compute Gallery and Disk Architecture
Premium SSD v2 — what to know 
Region/AZ availability is patchy compared to v1. Historically had restrictions on use as an OS disk (loosened over time). Pricing and IOPS scaling differ — v2 lets you tune size, IOPS, and throughput independently. Check current Azure docs before planning a tier migration.






29
Azure Compute Gallery and Disk Architecture
Direct shared gallery vs. RBAC sharing vs. community gallery

RBAC sharing: grant Reader role on the gallery resource. Requires AAD identity in your tenant.
Direct shared gallery: share specific versions to other subscriptions/tenants without RBAC roles on the gallery itself. Recipient pulls via a sharedGalleryImageVersion URI.
Community gallery: public, anyone can pull. Mostly for ISVs publishing reference images.
Direct shared = least friction for B2B image handoffs but weaker pull auditability.




30
Azure Compute Gallery and Disk Architecture
The capture-journey shortcuts

Set DiskControllerTypes=SCSI, NVMe at definition creation time — never try to add it later.
Capture from a VM whose SKU matches or exceeds the controllers you want supported. Don't delete the source VM until the captured image is verified deploying to the target SKU.
If a version source has frozen feature metadata that conflicts with your destination definition, you must rehydrate (deploy → recapture) or build fresh from Packer. There is no in-place metadata fix on a version.





31
Azure Compute Gallery and Disk Architecture





32
Azure Compute Gallery and Disk Architecture





33
Azure Compute Gallery and Disk Architecture





34
Azure Compute Gallery and Disk Architecture





35
Azure Compute Gallery and Disk Architecture





36
Azure Compute Gallery and Disk Architecture





37
Azure Compute Gallery and Disk Architecture





38
Azure Compute Gallery and Disk Architecture





39
Azure Compute Gallery and Disk Architecture





40
Azure Compute Gallery and Disk Architecture





