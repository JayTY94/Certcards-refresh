




11
Microsoft Purview
The Microsoft Purview Data Map provides the foundation for data discovery and data governance. It captures metadata about data present in analytics, software-as-a-service (SaaS), and operational systems in hybrid, on-premises, and multicloud environments. The data map stays up to date with its built-in scanning and classification system.







12
Microsoft Purview
The Data Map has two components: metadata storage and operation throughput, represented as a capacity unit (CU). All Microsoft Purview accounts, by default, start with one capacity unit and elastically grow based on usage. Each data Map capacity unit includes a throughput of 25 operations/sec and 10 GB of metadata storage limit.







13
Microsoft Purview
Some examples of operations are:

Create an asset in Data Map
Add a relationship to an asset such as owner, steward, parent, lineage, etc.
Edit an asset to add business metadata such as description, glossary term, etc.
Keyword search returning results to search result page.





14
Microsoft Purview
Operations are the throughput measure of the Microsoft Purview Data Map. They include any Create, Read, Write, Update, and Delete operations on metadata stored in the Data Map.





15
Microsoft Purview
The technical metadata includes schema, data type, columns, and so on, that are discovered during Microsoft Purview scanning. The business metadata includes automated (for example, promoted from Power BI datasets, or descriptions from SQL tables) and manual tagging of descriptions, glossary terms, and so on.





16
Microsoft Purview
Microsoft Purview Data Map can automatically scale up and down within the elasticity window (check current limits). To get the next level of the elasticity window, a support ticket needs to be created.







17
Microsoft Purview
The default limit for maximum operations per second is 10 capacity units. If you're working with a large Microsoft Purview environment and require a higher throughput, you can request a larger capacity of elasticity window by creating a quota request. 





18
Microsoft Purview
Running a scan invokes the process to ingest metadata from the registered data sources. The metadata curated at the end of the scan and curation process includes technical metadata. This metadata can include data asset names such as table names or file names, file size, columns, and data lineage





19
Microsoft Purview
If you have any Azure Policies preventing updates to Storage accounts, this causes errors for the Microsoft Purview scanning process. Follow the Microsoft Purview exception tag guide to create an exception for Microsoft Purview accounts.





20
Microsoft Purview
By design, you can't register data sources multiple times in the same Microsoft Purview account. This architecture helps to avoid the risk of assigning different access control to the same data source.






21
Microsoft Purview
After the data source is registered, set up a scan to manage automated and secure metadata scanning and curation.
Scan setup includes configuring the name of the scan, scope of scan, integration runtime, scan trigger frequency, scan rule set, and resource set uniquely for each data source per scan frequency.






22
Microsoft Purview
When you scan a storage account, Microsoft Purview uses a set of defined patterns to determine if a group of assets forms a resource set. You can use resource set pattern rules to customize or override how Microsoft Purview detects which assets are grouped as resource sets. 





23
Microsoft Purview






24
Microsoft Purview






25
Microsoft Purview






26
Microsoft Purview






27
Microsoft Purview






28
Microsoft Purview






29
Microsoft Purview






30
Microsoft Purview






31
Microsoft Purview






32
Microsoft Purview






33
Microsoft Purview






34
Microsoft Purview






35
Microsoft Purview






36
Microsoft Purview






37
Microsoft Purview






38
Microsoft Purview






39
Microsoft Purview






40
Microsoft Purview