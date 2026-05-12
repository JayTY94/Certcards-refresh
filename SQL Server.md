




1
SQL Server
Transaction log (.ldf) Every database has data files (.mdf, .ndf) plus one transaction log file. Every change is written to the log before the data file (write-ahead logging). This is what makes rollback, crash recovery, and point-in-time restore possible. Think of the log as a journal of edits; the data file is the final book.







2
SQL Server
Recovery model — SIMPLE vs FULL vs BULK_LOGGED

SIMPLE — log truncates automatically. Small log, but you can only restore to the last full/diff backup. Fine for dev/test or reloadable data.
FULL — log keeps everything until you back it up. Enables point-in-time restore, but you must take log backups or the log grows forever. The production default.
BULK_LOGGED — like FULL but minimally logs bulk operations for speed. Niche.






3
SQL Server
Full backup A complete copy of the database at a point in time. The foundation other backups build on.

Full — everything (baseline)
Differential — only changes since the last full
Transaction log — log records since the last log backup; enables point-in-time restore (FULL recovery only)
Typical pattern: weekly full + daily diff + log backups every 15 min.







4
SQL Server
tempdb 
Shared system database used as a scratchpad by every database on the instance: temp tables, table variables, sort/hash spills, snapshot/RCSI version store. Recreated from scratch every service restart — nothing in it is persistent. Because everyone shares it, a slow or undersized tempdb hurts the entire instance.







5
SQL Server
SQL Server Agent 
Built-in scheduler service. Runs jobs (backups, maintenance, alerts, SSIS). Included in Standard and Enterprise; not in Express. Set it to auto-start after install — easy to miss.







6
SQL Server
Per-Core minimums 
Minimum 4 core licenses per physical processor, sold in 2-core packs. So even a 2-core CPU costs 4 cores worth of licenses.







7
SQL Server
Per-core licensing covers the SQL Server instance running on that hardware. The instance can host as many databases as you want — licensing is about the engine and the cores it runs on, not the databases or tables.







8
SQL Server
SQL Server editions at a glance

Enterprise — full features, no scale limits. For mission-critical, 24x7, large memory, advanced HA.
Standard — mid-tier. Buffer pool capped at 128 GB; offline index rebuilds only.
Web — only through SPLA (hosting providers). Not for direct enterprise purchase.
Developer — full Enterprise features, free, non-production use only.
Express — free, 10 GB DB cap, ~1.4 GB memory, 1 socket/4 cores, no SQL Agent.





9
SQL Server
Standard Edition memory cap (128 GB) 
Standard's database engine ignores RAM above 128 GB for the buffer pool. Provisioning a Standard VM with 512 GB wastes most of it. Right-size around 128–192 GB or move to Enterprise. Columnstore and In-Memory OLTP have separate, smaller caps on top.







10
SQL Server
Online index rebuild = Enterprise only 
24x7 shops that can't tolerate table locks during maintenance windows need Enterprise. Standard can only do offline rebuilds (schema-mod lock on the table). This single requirement drives many Enterprise purchases.







11
SQL Server
Software Assurance (SA) The optional add-on that unlocks most of the valuable rights:

License Mobility — reassign licenses more often than every 90 days (including same-day VM moves)
One free passive secondary — for Always On AGs, only if truly passive (no read/backup/DBCC workload)
Azure Hybrid Benefit — bring on-prem licenses to Azure (SQL VM, Managed Instance, Azure SQL DB) for ~40–55% off
Unlimited virtualization — license every physical core on a host + SA = unlimited SQL VMs on that host
Step-Up — upgrade Standard → Enterprise without rebuying
Disaster Recovery Rights — cold/warm DR replicas






12
SQL Server
Passive secondary licensing 
With Software Assurance (SA), one passive secondary per licensed primary is free in an Always On AG. It must be genuinely passive — no reporting reads, no offloaded backups beyond limited use, no DBCC checks. The moment you point workload at it, you owe full licenses.







13
SQL Server
License Mobility vs Azure Hybrid Benefit

License Mobility (through SA) — the underlying right to reassign licenses to different hardware or cloud providers more often than every 90 days.
Azure Hybrid Benefit (AHB) — the program you actually elect at deployment time in Azure to redeem that right.
On the exam: "bring my licenses to Azure" = AHB.





14
SQL Server
SQL Server Web Edition 
Available only through SPLA (Services Provider License Agreement) — for hosting providers serving SQL to their customers. Not for direct on-prem purchase by end customers.







15
SQL Server
Server + CAL — what a CAL covers 
One User CAL per named user OR one Device CAL per shared device. Not per core, not per database, not per GB. 50 named users = 50 User CALs + the Server license.







16
SQL Server
TempDB file sizing 
Best practice: one tempdb data file per logical core up to 8, then add more (in groups of 4) only if PAGELATCH contention persists. All files equally sized, equal autogrowth so the proportional fill algorithm spreads allocations evenly. Default in SQL Server 2016+.







17
SQL Server
Transaction log storage — what matters 
The log is append-only sequential writes; every commit waits on a flush. Write latency dominates — target sub-millisecond on premium SSD or NVMe. IOPS and throughput matter more for data files (random) and analytics workloads (sequential throughput).







18
SQL Server
Cost Threshold for Parallelism (default 5) 
The query cost above which SQL Server considers a parallel plan. Default of 5 is a 1990s relic. Recommended starting point: 25–50 for OLTP. Pair with a sane MAXDOP (often cores-per-NUMA-node, cap at 8).







19
SQL Server
MAXDOP 
Maximum number of cores a single query can use in parallel. 0 = unlimited (bad on big servers). Common guidance: cores-per-NUMA-node, capped at 8 for OLTP. Tune alongside Cost Threshold for Parallelism.







20
SQL Server
Separate disks for data, log, tempdb 
Three different I/O personalities sharing one disk = contention. Log writes are latency-sensitive; data is random; tempdb is bursty mixed. Isolating each prevents a hot tempdb or heavy reporting from starving the user log. Still the safe default for on-prem even on SSD/SAN.







21
SQL Server
FULL recovery means the log grows between log backups. Plan for:

Peak .ldf size between log backups (on the database disk)
Backup target capacity — full + diff + log files pile up over retention (e.g., 30 days)
Forget either and you'll hit a full disk. When the backup target fills, log backups fail, the log can't truncate, and the live disk fills next — cascade failure.







22
SQL Server
Backup storage capacity math 
Sized independently from the live database. Rough formula: (full size × retention copies) + (diff size × diff frequency × retention) + (log size × ~96 per day × retention) + offsite copies.





23
SQL Server
tempdb is shared by every database on the instance. Heavy temp use, sorts, spills, snapshot version store all hit it. Sizing rules:

Own fast storage (dedicated drive/LUN)
Multiple equally-sized data files (per-core, up to 8)
Pre-grow to expected peak — don't rely on autogrow during workload






24
SQL Server
Wait stats — the starting point 
Query sys.dm_os_wait_stats to see what SQL Server is waiting on. Most performance problems show up here first.







25
SQL Server
CXPACKET / CXCONSUMER 
Parallelism waits — threads of a parallel query waiting on each other. Often a sign MAXDOP and/or Cost Threshold for Parallelism need tuning. CXCONSUMER (2017+) is usually benign; CXPACKET signals skew.







26
SQL Server
PAGELATCH_UP on pages 2:1:1, 2:1:3, 2:2:3 
Database ID 2 = tempdb. Page numbers 1 (PFS), 2 (GAM), 3 (SGAM) are allocation pages. Heavy waits here = tempdb allocation contention. Fix: multiple equally-sized tempdb data files; tempdb on fast storage.







27
SQL Server
WRITELOG 
Waiting on the transaction log disk to acknowledge a write. Check Avg Disk sec/Write on the log volume — target sub-1ms. Common causes: log on slow/shared storage, antivirus scanning the .ldf, SAN cache misconfig.







28
SQL Server
SOS_SCHEDULER_YIELD 
CPU pressure. Workers are yielding their schedulers because demand exceeds available CPU. Reinforce with signal-waits % >20–25%. Could be undersized VM, runaway parallel queries, or missing indexes forcing CPU-burning scans.







29
SQL Server
PAGEIOLATCH_* 
Waiting on data pages to come back from disk. Storage latency or memory pressure (too little buffer pool → constant re-reads from disk).







30
SQL Server
Page Life Expectancy (PLE) 
Seconds a data page stays in the buffer pool before being evicted. Falling PLE = memory pressure. Old "300 seconds" rule is obsolete on modern RAM — baseline your own normal and watch for drops. PLE per NUMA node is more meaningful than the instance total.







31
SQL Server
Parameter sniffing 
After a stats update or recompile, SQL Server caches a plan shaped for the first parameter value seen. If that value is atypical, the plan is terrible for everyone else. 
Fixes: OPTION (RECOMPILE), OPTIMIZE FOR hints, or enable Automatic Plan Correction via Query Store (2017+).







32
SQL Server
Query Store 
The single biggest troubleshooting upgrade in modern SQL Server. Captures query plans, performance over time, and lets you force a known-good plan. Turn it on for every production database.







33
SQL Server
Log won't truncate in FULL recovery 
Almost always: log backups aren't running (or are failing). Only log backups truncate the log in FULL. Check log_reuse_wait_desc in sys.databases — it tells you exactly what's holding the log (LOG_BACKUP, ACTIVE_TRANSACTION, REPLICATION, etc.). Memorize this column.







34
SQL Server
FULL → SIMPLE recovery — the danger 
Switching to SIMPLE to "fix log growth" throws away point-in-time recovery. If the DB dies, you can only restore to the last full/diff backup — every change since is lost. Fix the missing log backups instead.







35
SQL Server
Deadlock capture — modern way 
Use Extended Events. The built-in system_health XE session already captures xml_deadlock_report by default — pull recent deadlocks from it for free. Open the .xel file in SSMS for the visual deadlock graph. Profiler is deprecated; trace flags 1204/1222 are noisy.







36
SQL Server
Database in SUSPECT state — procedure

Set to EMERGENCY mode (read-only, single-user)
Run DBCC CHECKDB to assess corruption
Restore from backup if possible — always preferred
Last resort: REPAIR_ALLOW_DATA_LOSS (which can drop data to make the DB consistent)
Never run REPAIR_ALLOW_DATA_LOSS as step one.







37
SQL Server
Finding live blocking 
sys.dm_exec_requests + sys.dm_os_waiting_tasks — blocking_session_id column shows who's blocking whom. sp_WhoIsActive (Adam Machanic, free) is the de facto tool — install it on every instance. Activity Monitor in SSMS works but is heavier.







38
SQL Server
Index fragmentation thresholds (Paul Randal guidance)

< 5% — leave alone
5–30% — ALTER INDEX ... REORGANIZE (online, gentler)
> 30% — ALTER INDEX ... REBUILD (faster, heavier; online rebuild requires Enterprise)
On SSD/NVMe, fragmentation matters less than it used to. Update statistics regularly — often matters more than rebuilding.







39
SQL Server
Per Core vs Server + CAL

Per Core: license every core (4-core minimum per CPU). No user limit. Scales.
Server + CAL: one server license + one CAL per user/device. Cheaper at small user counts. Doesn't scale past ~25–50 users.






40
SQL Server
Enterprise vs Standard — common deal-breakers

Online index rebuild → Enterprise
128 GB buffer pool → Enterprise

Advanced Always On AGs (multi-DB, multi-readable secondaries) → Enterprise
TDE with customer-managed keys at scale, advanced HA features → Enterprise






41
SQL Server
Data files vs log file vs tempdb — I/O personalities

Data files — random reads/writes; IOPS + capacity
Log file — sequential writes; latency is king
tempdb — bursty mixed; needs its own fast disk + multiple equally-sized files






42
SQL Server
A SQL Server instance (engine, Windows service) hosts many databases. Each database is data files + a transaction log, organized into schemas. Recovery model decides log behavior → log file sizing → backup strategy → backup target sizing. Edition decides features and limits → which decides what hardware is useful (Standard caps RAM at 128 GB) and whether the workload is even possible (online rebuilds → Enterprise).





43
SQL Server
tempdb is shared and needs its own fast storage. OLTP vs OLAP decides what kind of fast storage. Per-core licensing covers the instance on its hardware; Server+CAL is a small-shop alternative. Software Assurance unlocks the valuable rights (passive secondary, Azure Hybrid Benefit, License Mobility, unlimited virtualization).





44
SQL Server






45
SQL Server






46
SQL Server






47
SQL Server






48
SQL Server






49
SQL Server






50
SQL Server






