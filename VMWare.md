vMotion

A VMware feature that allows the live migration of virtual machines between ESXi hosts with no downtime.
vSphere Cluster

A group of ESXi hosts that work together as a single entity, allowing for resource pooling and the management of VMs in a unified way.
ESXi Host

A physical server that runs the VMware ESXi hypervisor to host virtual machines (VMs).
vCenter Server

VMware's centralized management platform for multiple ESXi hosts and their associated virtual machines, used for configurations, monitoring, and management tasks.
High Availability (HA)

A VMware feature that automatically restarts virtual machines on another host if the original host fails. It ensures minimal downtime in case of host failure.
Fault Tolerance (FT)

A VMware feature that provides continuous availability by creating a shadow VM on a different host that automatically takes over in case of a host failure, ensuring zero downtime.
Distributed Resource Scheduler (DRS)

A feature of VMware vSphere that automatically balances workloads across ESXi hosts in a cluster, ensuring optimal resource usage.
Shared Storage

A storage system that is accessible by multiple ESXi hosts in a cluster, essential for vMotion, HA, and Storage vMotion.
vMotion Compatibility

The requirement for shared storage and network configuration to allow seamless migration of virtual machines between hosts without downtime.
VMware Horizon

A VMware product used for Virtual Desktop Infrastructure (VDI), enabling the delivery of virtual desktops and applications.
Hypervisor

Software that allows the creation and management of virtual machines by abstracting the physical hardware. There are two types: Type 1 (bare-metal) and Type 2 (hosted).
Type 1 Hypervisor

A hypervisor that runs directly on physical hardware, without an underlying operating system. Examples: VMware ESXi, Microsoft Hyper-V.
Type 2 Hypervisor

A hypervisor that runs on top of an existing host operating system, using the OS for resource management. Examples: VMware Workstation, Oracle VirtualBox.
Host Failure

When a physical ESXi host becomes unavailable due to hardware failure, power loss, or other issues, potentially affecting the VMs running on it.
VMware ESXi

A Type 1 hypervisor that runs on physical servers to create and manage virtual machines in a VMware environment.
Resource Pool

A logical grouping of CPU, memory, and storage resources in a VMware cluster, which can be allocated to virtual machines.
vCenter Server Management

The management and configuration of VMware environments through vCenter Server, which provides centralized control over ESXi hosts, virtual machines, and cluster settings.
Storage vMotion

The ability to migrate virtual machine disk files from one datastore to another without downtime, essential for managing storage resources across a cluster.
vSAN (Virtual SAN)

A VMware product that creates virtualized storage by aggregating local storage from ESXi hosts in a cluster, providing a shared storage solution without needing external storage hardware.
vSphere

VMware's suite of products for virtualization, including vCenter Server, ESXi, vMotion, and more, used to create and manage virtualized data centers.
Zero Downtime

The goal of technologies like Fault Tolerance (FT), where there is no interruption in service, even during host or hardware failures.
Live Migration

The process of moving a running virtual machine from one physical host to another with no interruption in service, typically using vMotion.



ESXi Shell

A command-line interface (CLI) used to manage and troubleshoot VMware ESXi hosts. The ESXi Shell allows administrators to run shell commands directly on the ESXi host for tasks like system configuration, troubleshooting, and diagnostics.
vSphere Client

A graphical user interface (GUI) tool used to manage and configure VMware ESXi hosts and virtual machines. The vSphere Client connects to vCenter Server to manage multiple ESXi hosts and provides an easy interface for monitoring, configuration, and troubleshooting tasks.
VMkernel

The core operating system that VMware ESXi uses to manage physical resources, such as CPU, memory, and storage. The VMkernel is responsible for creating and managing virtual machines, handling I/O operations, and providing resource management.
ESXi Host Profiles

A feature that allows administrators to configure, enforce, and standardize settings across multiple ESXi hosts in a cluster. Host profiles ensure consistency in configuration, such as networking, storage, and security settings, across all hosts in a given environment.
vSphere Distributed Switch (vDS)

A virtual switch that allows the central management of network configurations across multiple ESXi hosts. A vDS provides enhanced features like port mirroring, private VLANs, and traffic shaping for advanced network management in VMware environments.
ESXi Datastore

A storage container used by ESXi hosts to store virtual machine disk files (VMDKs), ISO images, templates, and other data related to virtual machines. Datastores can be backed by shared storage solutions, such as SAN (Storage Area Network), NFS (Network File System), or vSAN.
vMotion Network

A dedicated network connection used for transferring virtual machine memory and CPU state during a vMotion migration. This network should be optimized for high throughput and low latency to ensure smooth VM migration without performance degradation.
ESXi Lockdown Mode

A security feature that restricts access to an ESXi host to only a few trusted sources, such as the vCenter Server or specific administrators. When Lockdown Mode is enabled, direct access to the ESXi host (such as via SSH or the vSphere Client) is disabled, except for users who have administrative privileges.
vSphere HA Agent

A software agent installed on each ESXi host in a vSphere Cluster to enable High Availability (HA). The HA agent monitors the health of the host and communicates with other hosts to restart VMs automatically in the event of a host failure.
DirectPath I/O

A feature in VMware ESXi that allows direct access to a physical device (e.g., a network adapter, GPU, or storage controller) by a virtual machine, bypassing the hypervisor for better performance. This is typically used for workloads requiring high performance, such as GPU acceleration or network-intensive applications.
vSphere Distributed Resource Scheduler (DRS) Affinity Rules

Rules that can be configured in DRS to control the placement of virtual machines on ESXi hosts in a vSphere Cluster. Affinity rules can force specific VMs to run on the same host or on separate hosts, ensuring better workload management.
ESXi Virtual Machine Monitor (VMM)

A component of VMware ESXi that manages virtual machine execution, including CPU, memory, and I/O operations. It ensures that VMs are isolated from each other and allows each VM to operate independently of the host.
ESXi Installation

The process of installing VMware ESXi on a physical server. During installation, ESXi is deployed directly onto the hardware without requiring an underlying OS. The process typically involves configuring storage, network settings, and adding the host to vCenter Server for management.
VMware Tools

A suite of utilities and drivers that are installed in the guest operating system of a virtual machine running on an ESXi host. VMware Tools improves performance, provides better integration between the guest OS and ESXi, and allows features like vMotion and quiesced snapshots to function properly.
ESXi Logging and Troubleshooting

A set of logs and diagnostic tools built into VMware ESXi for monitoring system health, performance, and troubleshooting issues. Logs like vmkernel.log and hostd.log provide valuable information about system events, errors, and VM status for troubleshooting.
vSphere Fault Tolerance (FT) Primary and Secondary VM

In Fault Tolerance (FT), there are two VMs: the primary VM (the active VM) and the secondary VM (the shadow VM). The primary VM runs on one ESXi host, while the secondary VM is running in real-time on another host. If the primary VM fails, the secondary VM takes over immediately without any downtime.
Host Bus Adapter (HBA)

A hardware component in ESXi hosts that provides connectivity between the host and storage systems (e.g., SAN). HBAs are used to connect the ESXi host to the storage network, facilitating data transfers to and from virtual machines.
Storage I/O Control (SIOC)

A feature in VMware vSphere that manages storage I/O requests to ensure that all virtual machines receive fair access to storage resources. It helps avoid I/O contention by controlling the bandwidth allocated to different VMs when accessing shared storage.
ESXi Console Access

The ability to access the ESXi host’s console directly via the physical server or over a network using remote tools like SSH or the vSphere Client. This allows administrators to troubleshoot and configure the host or to work around issues when vCenter Server is unavailable.
Storage Policy-Based Management (SPBM)

A feature in VMware vSphere that enables administrators to manage storage resources using policies, such as performance, redundancy, and capacity. SPBM ensures that virtual machines and storage resources are compliant with business requirements and ensures that virtual machine storage is allocated to meet desired performance criteria.
vCenter Server Appliance (VCSA)

A Linux-based virtual appliance version of vCenter Server, which is optimized for VMware environments. The VCSA is a lightweight, pre-configured appliance designed to simplify deployment and management of vCenter Server without needing a Windows server.
ESXi Free License (VMware ESXi Free)

A free version of VMware ESXi that provides basic virtualization capabilities without advanced features like vMotion, HA, or DRS. It's limited to 8 physical CPU cores and does not include access to vCenter Server for centralized management.
VMFS (Virtual Machine File System)

A high-performance file system used by VMware ESXi to store virtual machine disk files (VMDKs) on shared storage. VMFS is optimized for virtual machine workloads and allows multiple ESXi hosts to access the same datastore simultaneously.
Host Profiles Compliance

A feature that checks whether an ESXi host is in compliance with the host profile configurations. If an ESXi host deviates from the standard profile (e.g., security or networking settings), it can be flagged for correction.
Virtual Machine Snapshot

A point-in-time copy of the state, data, and configuration of a virtual machine. Snapshots allow for the restoration of the VM to a previous state, which is useful for testing, troubleshooting, or backup purposes.