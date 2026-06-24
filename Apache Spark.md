




1
Apache Spark
RDD (Resilient Distributed Dataset) — Spark's most fundamental data structure: a fault-tolerant collection of elements partitioned across a cluster so it can be processed in parallel. "Resilient" means a lost partition can be rebuilt from its lineage.







2
Apache Spark
DataFrame — Data organized into named columns with a schema — essentially a distributed table, like a spreadsheet or SQL table. Built on top of RDDs but higher-level and faster because Spark understands its structure. The default choice for most structured work today.







3
Apache Spark
Schema — The definition of a DataFrame's column names and data types. It's the structure that lets Spark's optimizer reason about and speed up your queries.







4
Apache Spark
Partition — A chunk of a dataset that lives on a single node and is processed as one unit of work. More partitions means more tasks can run in parallel. This is what makes distributed processing possible.







5
Apache Spark
Lineage — Spark's recorded recipe of the transformations used to build a dataset. If a node fails, Spark replays the lineage to rebuild only the lost partition — no snapshots or manual intervention required. This is the "Resilient" in RDD.







6
Apache Spark
DAG (Directed Acyclic Graph) — Spark's internal map of all transformation steps and their dependencies. "Acyclic" = flows one direction, no loops. When you call an action, Spark uses the DAG to plan the most efficient execution path.







7
Apache Spark
Transformation — A lazy operation (e.g., map, filter, groupByKey, distinct, flatMap) that defines a new dataset but does not execute. It only adds a step to the recipe (the DAG).







8
Apache Spark
Action — An operation (e.g., collect, count, save) that triggers actual computation and returns a result to the driver or writes output. Nothing runs until an action is called.







9
Apache Spark
Lazy Evaluation — Spark delays all computation until an action is called. This lets it see the entire pipeline first and optimize before doing real work. Transformations build the recipe; actions cook the meal.







10
Apache Spark
Narrow vs. Wide Transformation — 
Narrow (map, filter) needs data from only one partition — no data movement. 
Wide (groupBy, join, reduceByKey) needs data from many partitions, forcing a shuffle across the network. 
Shuffles are expensive — minimizing them is core to performance tuning.







11
Apache Spark
Driver — The "brain" of a Spark application. Runs your main function, creates the SparkSession, splits the job into tasks, delegates them to executors, and collects results. If the Driver crashes, the whole application fails.







12
Apache Spark
Executor — A worker process that runs the actual tasks assigned by the Driver and stores data for its node. If the Driver is the manager, executors are the team members doing hands-on work. Many run in parallel.







13
Apache Spark
Cluster Manager — Allocates CPU and memory across the cluster's machines — the "landlord" of resources. Spark supports Standalone (built-in), YARN (Hadoop's), and Kubernetes.







14
Apache Spark
SparkSession — The unified entry point into all Spark functionality — the "front door." Created at the start of every modern Spark program to read data, run SQL, and build DataFrames. It replaced older separate entry points like SparkContext and SQLContext.







15
Apache Spark
Job → Stages → Tasks — Spark's execution hierarchy. An action creates a job; the job splits into stages (divided at shuffle boundaries); each stage breaks into tasks that run in parallel — one task per partition. Biggest to smallest unit of work.







16
Apache Spark
Spark Core — The foundation everything else sits on: task scheduling, memory management, fault recovery, and the RDD API. All higher-level libraries are built on top of it.







17
Apache Spark
Spark SQL — Lets you query structured data using SQL or the DataFrame API, with automatic optimization via Catalyst.







18
Apache Spark
Catalyst Optimizer — Spark SQL's query optimizer. It analyzes and rewrites your query into a more efficient execution plan before anything runs (reordering filters, pruning columns, etc.). A big reason DataFrames outperform hand-written RDD code.







19
Apache Spark
Structured Streaming — Processes continuous, real-time data (e.g., Kafka events) using the same DataFrame API as batch. The key idea: it treats a live stream as an unbounded table that keeps growing, so you query live data like a static dataset.







20
Apache Spark
MLlib — Spark's scalable machine learning library — distributed algorithms for classification, regression, clustering, and recommendations. Lets you train models on datasets too big for one machine.







21
Apache Spark
cache() / persist() — By default Spark recomputes a dataset every time you use it. These methods keep it in memory after the first computation so reuse is fast — hugely valuable in iterative work like ML training or repeated queries.







22
Apache Spark
Broadcast Variable — Sends a small, read-only dataset to every node once, instead of shipping a copy with every task. Classic use: a small lookup table joined against a huge dataset. Saves network traffic.







23
Apache Spark
Spark vs. Hadoop MapReduce — MapReduce writes every intermediate result to disk between steps (slow). Spark keeps intermediate data in memory whenever possible, slashing disk I/O — up to ~100x faster for certain workloads.







24
Apache Spark
RDD vs. DataFrame — RDD is low-level and unstructured (just a distributed collection); DataFrame adds a schema (named columns + types), enabling Catalyst optimization. Use DataFrames by default; drop to RDDs only for fine-grained control.







25
Apache Spark
Transformation vs. Action — Transformations are lazy and return a new dataset (define work); actions are eager and return a result or write output (trigger work). Remember: nothing computes until an action runs.







26
Apache Spark
Driver vs. Executor — Driver plans and coordinates (the manager); executors do the actual computation on data partitions (the workers).







27
Apache Spark
Official APIs — Scala, Java, Python, and R. Spark itself is written in Scala and runs on the JVM, but PySpark (Python) is the most popular today, especially for data science.







28
Apache Spark
Tip: The interlocking trio to truly internalize — lazy evaluation → DAG → lineage. Together they explain why Spark is both optimizable and fault-tolerant.





29
Apache Spark






30
Apache Spark






31
Apache Spark






32
Apache Spark






33
Apache Spark






34
Apache Spark






35
Apache Spark






36
Apache Spark






37
Apache Spark






38
Apache Spark






39
Apache Spark






40
Apache Spark






41
Apache Spark






42
Apache Spark






43
Apache Spark






44
Apache Spark






45
Apache Spark






46
Apache Spark






47
Apache Spark






48
Apache Spark






49
Apache Spark






50
Apache Spark






