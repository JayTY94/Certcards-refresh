




1
SQL Server Config
SQL Server instance
A full installation of the SQL Server database engine running as a Windows service. Each instance has its own configuration, system databases, ports, and collation. Multiple instances can exist on one machine.





2
SQL Server Config
Instance isolation model
Each SQL Server instance operates independently with its own system databases, ports, collation, and services, even on the same machine.





3
SQL Server Config
Default instance (MSSQLSERVER)
The primary SQL Server instance on a machine, accessed using only the server name (no instance suffix). Only one default instance can exist.





4
SQL Server Config
Named instance
A SQL Server instance identified by a name (e.g., Server\SQLREPL). Has independent configuration and typically uses a dynamic port unless configured otherwise.





5
SQL Server Config
SQL Server service
A Windows service that runs a SQL Server instance (e.g., SQL Server (SQLREPL)). Stopping the service stops that instance.





6
SQL Server Config
SQL Server Installation Center
The setup tool used to install, modify, repair, or remove SQL Server instances and features. Required for instance-level changes.





7
SQL Server Config
Instance discovery (Setup)
The process SQL Setup uses to detect installed instances. If this fails, options like “Remove instance” may not appear.





8
SQL Server Config
Setup Bootstrap folder
Directory containing SQL Server installer executables (e.g., ...Setup Bootstrap\SQL2019\). Used to launch setup manually.





9
SQL Server Config
Repair vs Remove (SQL Setup)
Repair fixes an installation; Remove uninstalls an instance or feature. Availability depends on setup context.





10
SQL Server Config
System databases
Core databases required by each instance:

master (metadata/config)
model (template for new DBs)
msdb (jobs, backups)
tempdb (temporary objects)





11
SQL Server Config
tempdb
A system database recreated on startup that always uses the instance collation. Frequently involved in collation-related issues.





12
SQL Server Config
Instance-level collation
The collation assigned at install time to an instance. Controls system databases and defaults for new databases.





13
SQL Server Config
Database collation
The collation assigned to a user database. Can be changed independently, but does not affect tempdb or instance behavior.





14
SQL Server Config
Column-level collation
A collation applied directly to a column. Overrides database default for comparisons and sorting.





15
SQL Server Config
tempdb collation inheritance
tempdb always uses instance collation, which can cause conflicts when user databases use different collations.





16
SQL Server Config
Collation conflict error
Occurs when SQL Server compares strings with incompatible collations (often in joins or temp tables).





17
SQL Server Config
Rebuild system databases
A destructive operation that recreates master, model, msdb, and tempdb. Required to change instance-level collation without reinstalling.





18
SQL Server Config
SQL Server Configuration Manager
Tool used to manage SQL services, network protocols, and ports for each instance.





19
SQL Server Config
SQL Server port
The TCP port an instance listens on. Default instance usually uses 1433; named instances may use other ports.





20
SQL Server Config
Dynamic port
A port automatically assigned at startup. Requires SQL Browser or other resolution to connect.





21
SQL Server Config
Static port
A fixed port manually assigned to an instance. Removes dependency on SQL Browser and improves connectivity reliability.





22
SQL Server Config
SQL Server Browser service
A service that resolves Server\InstanceName into a port number for clients. Required when using named instances without specifying ports





23
SQL Server Config
SQL Browser dependency
Occurs when a client relies on SQL Browser to resolve named instance connections. Common failure point if blocked or disabled.





24
SQL Server Config
Instance name resolution
The process of translating Server\InstanceName into a network port. Handled by SQL Browser or avoided by specifying a port directly.





25
SQL Server Config
Named instance connection failure pattern
Common issue where:

ping works
SQL connection times out
Caused by port resolution failure (SQL Browser or firewall).





26
SQL Server Config
Connection string (SQL Server)
The string used by applications to connect to SQL Server.
Examples:
Server=MyServer\SQLREPL
Server=MyServer,1434

Using a port is more reliable than using an instance name.





27
SQL Server Config
SQL connectivity test hierarchy
Standard troubleshooting order:

DNS / ping
Port check (Test-NetConnection)
SQL login (sqlcmd)
Application config





28
SQL Server Config
SQL Server setup features
Components installed per instance (e.g., Database Engine, Replication). Removing an instance removes its associated features.





29
SQL Server Config
Replication / SQL Replicator (context)
An external service or application that connects to SQL Server. Sensitive to connection reliability, collation compatibility, and configuration correctness.





30
SQL Server Config






31
SQL Server Config






32
SQL Server Config






33
SQL Server Config






34
SQL Server Config






35
SQL Server Config






36
SQL Server Config






37
SQL Server Config






38
SQL Server Config






39
SQL Server Config






40
SQL Server Config






41
SQL Server Config






42
SQL Server Config






43
SQL Server Config






44
SQL Server Config






45
SQL Server Config






46
SQL Server Config






47
SQL Server Config






48
SQL Server Config






49
SQL Server Config






50
SQL Server Config






