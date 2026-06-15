# Databricks Fundamentals — Study Notes

*Quick-reference flashcards. Each entry stands alone. Skim anytime.*

---


Lakehouse
 — A data platform that combines a data lake's cheap, flexible storage with a data warehouse's reliability and speed. It's the core idea behind Databricks: one system for raw files *and* trustworthy business tables.

<p align="center">• • •</p>


Data lake vs. Data warehouse
 — A *lake* is a cheap dumping ground for raw files (flexible but messy); a *warehouse* holds clean, structured tables (reliable but rigid and pricey). The lakehouse merges the best of both.

<p align="center">• • •</p>


Apache Spark
 — The engine underneath Databricks that processes huge datasets in parallel across many machines. When people say data work is "fast at scale" on Databricks, Spark is why.

<p align="center">• • •</p>


Notebook
 — A browser-based document of code cells (SQL or Python) that you run one at a time, with results and charts appearing inline. Your main workspace for getting things done.

<p align="center">• • •</p>


Cluster / Compute
 — The rented servers that actually run your code. You start one to do work and shut it down when finished. 
It bills while running
 — idle clusters quietly waste money.

<p align="center">• • •</p>


Serverless compute
 — Databricks manages the underlying servers for you, so compute starts quickly with no cluster setup to babysit. Less to manage, fast to spin up.

<p align="center">• • •</p>


Cluster vs. Serverless
 — With a regular *cluster* you choose and manage the machines (and watch idle cost). With *serverless*, Databricks handles the servers behind the scenes and they start near-instantly.

<p align="center">• • •</p>

## Delta Lake


Delta Lake
 — The reliable table format that sits on top of raw cloud files and makes them trustworthy. It's what turns a messy lake into something you can safely report from.

<p align="center">• • •</p>


ACID transactions
 — Delta Lake's all-or-nothing write guarantee: concurrent jobs and mid-job crashes won't leave corrupted or half-written data. The same reliability databases have always had, now on cheap cloud files.

<p align="center">• • •</p>


Time travel
 — Delta keeps a version history, so you can query a table *as it existed* at an earlier point. Great for audits, recovering from a bad write, or reproducing yesterday's numbers.

<p align="center">• • •</p>


Schema enforcement
 — Delta rejects writes that don't match the table's defined structure (wrong columns/types), protecting tables from accidental corruption.

<p align="center">• • •</p>

## Medallion Architecture


Medallion architecture
 — A design pattern that refines data through three progressively cleaner layers: 
Bronze → Silver → Gold
. Data flows left to right, getting more polished at each hop. (Think medal tiers: rough to refined.)

<p align="center">• • •</p>


Bronze layer
 — Raw data ingested 
largely as-is
 from the source, minimal transformation. The faithful, replayable original — if downstream logic changes, you can always reprocess from here. *Mental image: the loading dock.*

<p align="center">• • •</p>


Silver layer
 — 
Cleaned and conformed
 data: duplicates removed, formats fixed, schema standardized — but 
still row-level detail
, not yet summarized. *Mental image: the cleaning station.*

<p align="center">• • •</p>


Gold layer
 — 
Cleaned *and* aggregated
 tables: KPIs, totals, roll-ups — purpose-built for dashboards, BI, and executives. *Mental image: the showroom.*

<p align="center">• • •</p>


Silver vs. Gold (the tricky one)
 — Both are clean. 
Silver = detailed rows, tidied up. Gold = those rows rolled up into summaries.
 The tell: words like *summarized, aggregated, KPIs, dashboard, or executive* point to 
Gold
. If it's still individual transactions (just clean ones), it's 
Silver
.

<p align="center">• • •</p>

## Unity Catalog & Governance


Unity Catalog
 — Databricks' governance layer: controls who can access which data, tracks where data came from, and centralizes permissions across the workspace. The keyword is *governance* — not speed, not storage.

<p align="center">• • •</p>


GRANT / REVOKE
 — SQL commands in Unity Catalog that give or remove a user's access to data objects (tables, schemas). The everyday mechanics of "who can see what."

<p align="center">• • •</p>


Data lineage
 — A Unity Catalog feature that traces how data flows from source through each transformation to the final tables. Invaluable for audits and debugging "where did this number come from?"

<p align="center">• • •</p>


Managed vs. External tables
 — With a 
managed
 table, Databricks controls both the metadata *and* the data files (drop the table → data is deleted). With an 
external
 table, the data files live 
outside Databricks' control
 (drop the table → files remain). Rule of thumb: managed = Databricks owns the files; external = you do.

<p align="center">• • •</p>

## Ingestion, Sharing & Optimization


Auto Loader
 — Efficiently detects and ingests 
new files as they arrive
 in cloud storage, without reprocessing everything each run. An *ingestion* tool — getting data in.

<p align="center">• • •</p>


Delta Sharing
 — An open protocol for securely sharing 
live
 data with people *outside* your organization — no copying or emailing files. Recipients see current data through a governed connection.

<p align="center">• • •</p>


Liquid clustering
 — An optimization that organizes how data is physically laid out on disk so queries skip irrelevant data and run faster. Increasingly the default, replacing older manual *partitioning*.

<p align="center">• • •</p>


Databricks SQL
 — The part of the platform aimed at running queries, building dashboards, and BI-style analytics on lakehouse data — the natural touchpoint if your world is reporting and Power BI.

<p align="center">• • •</p>

## Quick Context


Certification fit
 — For a reporting/BI focus, the 
Data Analyst Associate
 cert (SQL on Databricks, dashboards, Unity Catalog basics, basic Delta) is the natural starting point. The 
Data Engineer Associate
 goes deeper into pipelines, ingestion, and orchestration.

<p align="center">• • •</p>


Lakeflow (2026 branding)
 — Recent Databricks material rebrands orchestration and pipelines under "Lakeflow" (e.g., Lakeflow Jobs, Lakeflow Declarative Pipelines). The underlying skills are the same; only the names changed.
