1
Azure Virtual Machines
Azure reserves the first four addresses and the last address in each subnet for its use.







2
Azure Virtual Machines
The VM size can be changed while the VM is running, as long as the new size is available in the current hardware cluster the VM is running on. 
The command line tools report an error if you attempt to resize a VM to an unavailable size. 
Changing a running VM size automatically reboots the machine to complete the request.





3
Azure Virtual Machines
There is no separate cost for NICs. However, there is a limit to how many NICs you can use based on your VM's size. Size your VM accordingly and reference Virtual Machine pricing.





4
Azure Virtual Machines
Let's assume you want to configure and install more software on your virtual machine after the initial deployment. You want this task to use a specific configuration, monitored and executed automatically.

Azure VM extensions are small applications that enable you to configure and automate tasks on Azure VMs after initial deployment.







5
Azure Virtual Machines
Azure Backup is a backup as a service offering that protects physical or virtual machines no matter where they reside: on-premises or in the cloud.







6
Azure Virtual Machines
Azure Backup uses several components that you download and deploy to each computer you want to back up. The component that you deploy depends on what you want to protect.

    Azure Backup agent
    System Center Data Protection Manager
    Azure Backup Server
    Azure Backup VM extension





7
Azure Virtual Machines
Azure Backup uses a Recovery Services vault for storing the backup data. Azure Storage blobs back up a vault, making it an efficient and economical long-term storage medium. With the vault in place, you can select the machines to back up, and define a backup policy (when snapshots are taken and for how long they’re stored).







8
Azure Virtual Machines
Metrics are numerical values collected at predetermined intervals to describe some aspect of a system. Metrics can measure VM performance, resource utilization, error counts, user responses, or any other aspect of the system that you can quantify.





9
Azure Virtual Machines
Azure Monitor Metrics automatically monitors a predefined set of metrics for every Azure VM, and retains the data for 93 days with some exceptions.







10
Azure Virtual Machines
Azure automatically collects basic metrics for VM hosts. On the VM's Overview page in the Azure portal, you can see built-in graphs for the following important VM host metrics.

    VM availability
    CPU usage percentage (average)
    OS disk usage (total)
    Network operations (total)
    Disk operations per second (average)





11
Azure Virtual Machines
You can use Azure Monitor Metrics Explorer to plot more metrics graphs, investigate changes, and visually correlate metrics trends for your VMs. With Metrics Explorer you can track the same metric over multiple VMs in a resource group or other scope, and use splitting to show each VM on the graph.






12
Azure Virtual Machines
What are the layers of a VM that need to be monitored?
VM monitoring layers consist of the VM host and the client VM, which includes the guest OS and the workloads and applications that run on the VM.







13
Azure Virtual Machines
To open Metrics Explorer, you can:

    Select Metrics from the VM's left navigation menu under Monitoring.
    Select the See all Metrics link next to Platform metrics on the Monitoring tab of the VM's Overview page.
    Select Metrics from the left navigation menu on the Azure Monitor Overview page.






14
Azure Virtual Machines
Metric Namespace: 
In Metrics Explorer, most resource types have only one namespace, but for some types, you must pick a namespace. For example, storage accounts have separate namespaces for files, tables, blobs, and queues





15
Azure Virtual Machines
2. Which of these parameters isn't included in the dropdown fields when you define a Metrics Explorer graph?
Time range
You select the time range and granularity for a metrics graph by selecting the time filter above the graph.







16
Azure Virtual Machines
The VM client includes the operating system and other workloads and applications. To monitor the software running on your VM, you install the Azure Monitor Agent, which collects data from inside the VM. VM insights:

    Installs Azure Monitor Agent on your VM.
    Creates a DCR that collects and sends a predefined set of client performance data to a Log Analytics workspace.
    Presents the data in curated workbooks.






17
Azure Virtual Machines
1. What capabilities does enabling VM insights provide?
Prebuilt client performance workbooks and guest OS metrics.
Enable VM insights with the Azure Monitor Agent to collect guest OS metrics and use prebuilt workbooks to visualize VM client performance.







18
Azure Virtual Machines
2. What's a quick way to install the Azure Monitor Agent to collect guest OS metrics?
Select the Azure Monitor Agent when you enable VM insights.
Select the Azure Monitor Agent instead of the legacy Log Analytics Agent when you enable VM insights.







19
Azure Virtual Machines
Azure Virtual Desktop uses Azure Monitor for monitoring and alerts like many other Azure services. This lets admins identify issues through a single interface.





20
Azure Virtual Machines
You can open Azure Monitor for Azure Virtual Desktop by doing the following:

    Go to the Azure portal.
    Search for and select Azure Monitor from the Azure portal. Select Insights Hub under Insights, then select Azure Virtual Desktop. Once you have the page open, enter the Subscription, Resource group, Host pool, and Time range of the environment you want to monitor.

This assumes that the diagnostics settings and workspace were already configured.





21
Azure Virtual Machines
To collect information on your Azure Virtual Desktop infrastructure, you'll need to enable several diagnostic settings on your Azure Virtual Desktop host pools and workspaces (this is your Azure Virtual Desktop workspace, not your Log Analytics workspace).







22
Azure Virtual Machines






23
Azure Virtual Machines






24
Azure Virtual Machines






25
Azure Virtual Machines






26
Azure Virtual Machines






27
Azure Virtual Machines






28
Azure Virtual Machines






29
Azure Virtual Machines






30
Azure Virtual Machines






31
Azure Virtual Machines






32
Azure Virtual Machines






33
Azure Virtual Machines






34
Azure Virtual Machines






35
Azure Virtual Machines






36
Azure Virtual Machines






37
Azure Virtual Machines






38
Azure Virtual Machines






39
Azure Virtual Machines






40
Azure Virtual Machines