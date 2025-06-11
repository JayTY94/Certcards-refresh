Q: Why is a 200 K-row table (40 MB PBIX) unlikely to be “too large” for Power BI Desktop?
A: Power BI regularly handles multi-million-row tables under 100 MB if well-modeled; a 200 K-row table is small. Performance issues usually stem from query complexity or broken folding, not raw size.

Q: What is “query folding” and why does it matter for refresh timeouts?
A: Query folding means pushing filtering/sorting logic down to the data source. If a step breaks folding, Power Query pulls all rows client-side, increasing data volume and risking timeouts.

Q: What is the default command timeout for the SQL Server connector in Power Query?
A: 10 minutes. Queries taking longer will time out unless you explicitly increase the CommandTimeout in the M step.

Q: How can you increase the SQL connector’s command timeout in M?
A: In the Sql.Database(...) step, add CommandTimeout=#duration(0,0,20,0) (for 20 minutes), e.g.:

m
Copy
Edit
Source = Sql.Database("server", "db", [ Query="...", CommandTimeout=#duration(0,0,20,0) ])
Q: What tool in Power BI Desktop lets you see which query steps are folding, how long each step takes, and row counts?
A: Query Diagnostics (in Power Query Editor → Tools → Start Diagnostics / Stop Diagnostics).

Q: How do you use Performance Analyzer in Power BI Desktop?
A: In Report view, go to View → Performance Analyzer → Start Recording → Refresh Visuals. It shows DAX query times, visual rendering times, etc., for each visual.

Q: In a Pro workspace, which Service-side feature that profiles per-table/partition timings is unavailable?
A: The Query Inspector (Query performance pane) in the Power BI Service is only available on Premium or Premium Per User. Pro users only see basic Refresh History.

Q: Why might “Rows Loaded” in Refresh History show fewer rows than expected even when the status is “Succeeded”?
A: A query may have partially timed out or a partition returned 0 rows (e.g., due to filter/timeout). “Succeeded” can hide warnings about QueryTimeout or skipped partitions.

Q: What is the manual way to simulate incremental refresh on a Pro workspace?
A: Create two queries—one filtered to “History” (older than BoundaryDate) and disabled after initial load, and one “Recent” (rows ≥ BoundaryDate). Then append them in a third query and load only the appended table.

Q: Why does disabling load on the “History” query improve refresh performance?
A: Disabled queries aren’t re-executed on refresh. Only the “Recent” query runs against the source, so you fetch fewer rows (e.g., 100 K instead of 200 K) each cycle.

Q: How do you advance the refresh “cutoff date” when using manual partitioning with two queries?
A: Update the BoundaryDate parameter, temporarily re-enable the History query (and disable Recent), refresh History so it pulls the newly frozen rows, then re-disable History and re-enable Recent before a full refresh.

Q: If you freeze only half your rows (e.g., 100 K of 200 K), what kind of refresh time improvement can you expect?
A: Roughly a proportional gain—halving the pulled rows typically cuts variable query time nearly in half; speed-up may be ~40 % overall because fixed overhead (connection setup) remains.

Q: What are common pitfalls when manually partitioning with two queries?
A: Forgetting to disable History after its catch-up refresh (causes full pull), mismatched schemas between History & Recent, and letting the Historical table outgrow available memory.

Q: How can you verify gateway-related issues are not causing silent failures?
A: Download gateway logs (Admin Portal → Gateways → Diagnostics) and search for timeouts or errors (e.g., QueryTimeoutException). Also check gateway CPU/memory spikes.

Q: Name one alternative to the SQL connector when connecting to Dataverse that can improve folding and avoid timeouts.
A: Use the built-in Dataverse (OData/CDS) connector via Get Data → Dataverse. It often auto-folds better into Dataverse’s paging model than the SQL (TDS) endpoint.






You said:
Generate some more please


ChatGPT said:
Q: What are the two main components of query execution time when pulling data via SQL?
A: Fixed costs (connection setup, query plan, authentication, network latency) and variable costs (reading/transmitting each row). Reducing row count cuts the variable portion.

Q: How can you verify the actual row count fetched during a Service refresh?
A: In the Power BI Service, go to the dataset’s View Refresh History → Details, and check the “Rows Loaded” for each table or partition to see how many rows were imported.

Q: Why might switching to the Dataverse (OData/CDS) connector improve performance over the SQL connector?
A: The Dataverse connector is designed to leverage server‐side paging and API optimizations, often preserving query folding more reliably and avoiding TDS‐related throttling.

Q: What indicates a break in query folding when reviewing Query Diagnostics in Power Query?
A: In the “Folding” diagnostic table, any step marked “Not foldable” shows where folding stopped, meaning subsequent transformations happen client‐side.

Q: What is the typical Power BI Service behavior when you define an Incremental Refresh policy but deploy to a Pro workspace?
A: The service ignores the policy and performs a full‐table refresh each time, without partitioning.

Q: How do you detect gateway‐related timeouts or errors that might silently truncate a refresh?
A: Download the on‐premises gateway logs via Manage Gateways → Diagnostics and search for keywords like QueryTimeoutException, ICE, or indications of lost connections.

Q: In manual partitioning, why is it unnecessary to disable load on the appended (final) table?
A: The appended table’s logic only runs in‐memory, combining already‐loaded “History” and “Recent.” Disabling it would prevent the final unified table from being loaded into the model.

Q: What happens if you forget to disable the “History” query after updating your cut‐off date?
A: On subsequent refreshes, Power Query will re‐run the entire “History” slice each time, negating performance gains and re‐pulling all historical rows.

Q: How can you test the raw performance of your Dataverse SQL query outside of Power BI?
A: Copy the native SQL (e.g., SELECT … FROM dbo.account WHERE ModifiedOn ≥ '2024-01-01') into SQL Server Management Studio (SSMS) or Azure Data Studio, run it, and measure execution time to compare against Power BI.

Q: What is VertiPaq and why is it relevant when appending tables?
A: VertiPaq is Power BI’s in‐memory columnar engine. When appending tables with identical schemas, VertiPaq compresses and merges columns efficiently, making the in‐memory append step very fast.

Q: What are the risks of using a static RangeStart parameter over a long period?
A: If you never update RangeStart, new “late-arriving” or back‐dated changes older than that date won’t be captured. You risk permanently missing updates unless you periodically advance the boundary.

Q: When manually partitioning, how do you ensure both “History” and “Recent” queries share the same column structure?
A: Explicitly select and order columns in both queries (e.g., via Table.SelectColumns) so they match exactly, avoiding mismatched column errors during the append.

Q: Why might a table visual in Power BI show fewer rows than exist in the dataset even if the data model has all rows?
A: Large table visuals can hit rendering timeouts or be partially truncated. Use Performance Analyzer to see if the DAX query or visual rendering is timing out.

Q: How can you approximate how much time you’ll save by freezing N rows?
A: Estimate your original full‐pull time, subtract the fixed overhead (connection, plan) from both, and assume variable cost scales roughly with row count. For example, if 200 K rows take 10 min, pulling 100 K might take ~6 min, saving ~4 min per refresh.

Q: What should you do if your “Recent” slice still pulls too many rows and risks timeout?
A: Further narrow the filter (e.g., only Active records or a shorter date window), or split the “Recent” slice into smaller rolling windows (daily or weekly), freezing each once complete.






You said:
Can you add a few more that were related, even if they didn't come up in teh conversation?


ChatGPT said:

Thought for a couple of seconds
Q: What is the difference between Import mode and DirectQuery in Power BI, and how does it affect refresh?
A:

Import mode loads data into Power BI’s in-memory VertiPaq engine; refresh pulls and replaces those imported rows on a schedule.

DirectQuery leaves data in the source system and issues queries live; there is no “data refresh” per se—performance depends on source responsiveness, and you cannot use Import‐only features like Query Diagnostics or in-memory appends.

Q: How can you use Power BI parameters to make your queries more dynamic?
A:

Define Parameters (Home → Manage Parameters) like BoundaryDate, ServerName, or DatabaseName.

Reference them in M steps (e.g., Value.NativeQuery or in the Sql.Database connection).

When you change a parameter value, all dependent queries update automatically, enabling easy cut-off adjustments or environment switching.

Q: Why is it beneficial to remove unused columns before loading data into the model?
A:

Reduces data volume transferred over the network.

Lowers memory footprint in VertiPaq, improving compression ratios.

Speeds up query folding, since fewer columns need to be projected at the source.

Q: What role does Data Profiling in Power Query play when troubleshooting refresh issues?
A:

Data Profiling (enable under View → Column quality/Column distribution) lets you see values, error rates, and distinct counts.

Helps identify unexpected nulls, data type mismatches, or outliers that could increase transformation complexity or break folding.

Q: How can Aggregations in Power BI speed up queries on large fact tables?
A:

Define a summarized (aggregated) table at a higher grain (e.g., daily sales totals) and point visuals to it for common queries.

The engine stores both the detailed and aggregated tables; for queries that can be satisfied by the aggregate, Power BI never scans the full fact table, reducing query time dramatically.

Q: What is the effect of data type mismatches on Power Query folding and performance?
A:

If you change a column’s data type (e.g., from text to date) before filtering, Power Query may break folding because the source might not support that conversion natively.

Always apply type conversions at the end, after filters, or ensure the source can natively convert the type in the same query.

Q: How do incremental refresh policies handle late-arriving data, and what can you do to mitigate missed updates?
A:

Incremental refresh typically uses a RangeStart/RangeEnd window; any rows older than RangeStart aren’t re-queried.

To capture late-arriving updates, include a “stale data window” (e.g., overlapping dates) so you reprocess recent partitions that might receive back‐dated changes, then drop duplicates in Power Query or DAX.

Q: Why might using a Date dimension table improve model performance and simplify filters?
A:

A dedicated Date table lets you create one‐to‐many relationships to fact tables and use date‐intelligence DAX functions efficiently.

It centralizes filters (e.g., Year, Quarter) rather than filtering on a date column in every fact, reducing the complexity of DAX queries that run during refresh or visual rendering.

Q: What is the benefit of using Value.NativeQuery in Power Query when working with SQL sources?
A:

It allows you to write native SQL, including advanced filters, joins, or query hints (e.g., OPTION (MAXDOP 1)), ensuring that complex transformations happen on the server.

Improves folding by preventing Power Query from pulling unnecessary data, as the entire logic executes in the database and returns only the final result set.

Q: How can using the “Enable Load of Related Entities” option in the Dataverse connector improve performance?
A:

This option, in the Dataverse (OData) connector, fetches related lookup or option‐set tables alongside the main entity in one API call.

Reduces the number of round trips, preserves folding, and can significantly cut down on refresh time compared to separately querying each related table.


What’s the difference between SUMMARIZE and SUMMARIZECOLUMNS?
SUMMARIZE creates a virtual table using a row context that you must convert to filter context with CALCULATE, whereas SUMMARIZECOLUMNS works directly in filter context, handles aggregations and filter modifiers more predictably, and is optimized by the engine for better performance.

How does ALLEXCEPT work in a measure?
ALLEXCEPT(table, column1, …) removes all filters on the specified table except those on the listed columns. It’s used inside CALCULATE to preserve only certain filters (for example, keep EngagementID but ignore Task Category).

Why can’t you reference a newly added column alias in the same SUMMARIZECOLUMNS call?
DAX processes each expression in a single SUMMARIZECOLUMNS call in isolation, so the engine doesn’t know aliases until after all expressions are parsed. You must either inline the logic or add the column in a separate step.

What pattern lets you reference intermediate calculations by name when building a calculated table?
Use a two-step ADDCOLUMNS approach: first add your intermediate columns, then in a second ADDCOLUMNS call reference those names to compute further results (for example, percentages).

When would you use GENERATESERIES in DAX?
GENERATESERIES(start, end, increment) produces a single-column table of numeric values at the specified step size. It’s useful for creating bins or ranges (for example, percentage buckets) for frequency analysis.

What’s the scope of variables (VAR) inside an ADDCOLUMNS column definition?
A VAR declared inside one column’s definition lives only within that column. To share results, you must either repeat the logic or separate the columns into multiple ADDCOLUMNS calls so that the column values exist in the table.

Why might SUMMARIZECOLUMNS yield better performance than SUMMARIZE?
The Tabular engine has built-in optimizations for SUMMARIZECOLUMNS that reduce temporary table materializations and merge identical aggregations, resulting in faster query plans, especially on large fact tables.

What is the difference between row context and filter context in DAX?
Row context iterates over rows (as in iterators like SUMX or SUMMARIZE), while filter context filters tables for evaluation (as in measures and visuals). CALCULATE is the primary way to convert row context into filter context and apply or modify filters.