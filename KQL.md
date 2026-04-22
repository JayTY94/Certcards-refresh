1
KQL
The Pipe | 
KQL is a pipelined language. Each | takes the tabular result from the previous step and feeds it as input to the next operator. Read queries left-to-right, top-to-bottom: source table → filter → transform → aggregate → present.





2
KQL
Case-Insensitive String Operators Add a tilde (~) to make a string operator case-insensitive.

    == exact match · =~ case-insensitive match
    != not equal · !~ case-insensitive not equal
    contains / contains_cs, startswith / startswith_cs Default contains is already case-insensitive; add _cs when you need case sensitivity.





3
KQL
has vs. contains

    has — matches whole indexed terms (words split on punctuation/whitespace). Uses the term index. Fast.
    contains — substring scan, no index. Slow on large tables. "login" would match "relogin". 
    Rule of thumb: searching for a full token (username, IP, error code, GUID) → has. Need a partial substring → contains.






4
KQL
project vs. extend

    project — reshapes output. Only the listed columns survive.
    extend — adds calculated columns while keeping existing ones. Use project-away ColName to drop specific columns without re-listing the keepers. Use project-rename to rename without recalculating.






5
KQL
summarize — KQL's Aggregator There is no GROUP BY in KQL. Everything happens in one operator:

T | summarize Count=count(), Avg=avg(Dur) by EventLevel
The by clause defines the groups. Omit by to aggregate the entire table into one row.






6
KQL
ago() Returns a datetime relative to query execution time. ago(1h) = now minus one hour; ago(7d) = seven days ago. Common pattern: | where TimeGenerated > ago(24h). Returns a timestamp, not a timespan — don't confuse it with 1h as a literal.







7
KQL
bin() — Time and Numeric Buckets Rounds a value down to the nearest multiple of the bin size.

    bin(TimeGenerated, 5m) — 5-minute buckets for time-series charts
    bin(Price, 10) — numeric buckets of 10 Pair with summarize … by bin(...) for render timechart visualizations.






8
KQL
KQL Join — The innerunique Gotcha 
The default join kind is innerunique, not inner. It silently deduplicates the left side's join keys before matching — you can lose rows you expected. Always specify kind= explicitly:

    kind=inner — true inner join, every matching pair
    kind=leftouter — keep all left rows, null for unmatched
    kind=fullouter — keep unmatched rows from both sides
    kind=leftanti — left rows with no match on right (great for "not in")






9
KQL
let Statement Binds a name to a scalar, a tabular expression, or a function. Declared at the top of the query; ; separates statements.

    let cutoff = ago(7d);
    let VIPs = Users | where Tier == "Gold";
    VIPs | where LastSeen > cutoff






10
KQL
count() vs. dcount() vs. count_distinct()

    count() — total rows, duplicates included.
    dcount(col) — approximate distinct count using HyperLogLog. Fast on huge datasets, slight inaccuracy.
    count_distinct(col) — exact distinct count. Use on smaller sets where precision matters.






11
KQL
SourceTable            // pick data
| where …              // filter early (cheap, indexed)
| extend …             // add calculated columns
| project …            // trim to columns you need
| summarize … by …     // aggregate
| sort by … desc       // or top N by …
| render timechart     // visualize





12
KQL
Bonus — Common Type Casts

    tostring(), toint(), tolong(), toreal(), tobool()
    todatetime("2026-04-22"), totimespan("01:30:00")
    todynamic() to parse a JSON string into a dynamic object Casting is required before using a dynamic column in summarize by, sort by, or join on.






13
KQL
take / limit 
Synonyms. Return N arbitrary rows — no ordering guarantee. Use | take 10 while exploring a new table to see sample rows cheaply. For "top 10 most recent" or "top 10 largest," use top instead, which sorts first.







14
KQL
top vs. sort + take

    | top 10 by Amount desc — sorts and limits in one efficient step.
    | sort by Amount desc | take 10 — same result, slightly more work for the engine. Prefer top when you want the N largest/smallest.





15
KQL
distinct Returns unique combinations of the listed columns. Think of it as "give me the unique set."

Events | distinct UserId, EventType
Cheaper than summarize by UserId, EventType when you don't need aggregates.





16
KQL

in, !in, in~, !in~ Membership tests.

| where State in ("TX", "CA", "NY") — exact match
| where State in~ ("tx", "ca") — case-insensitive
!in / !in~ — not in You can also pass a dynamic array or a subquery: | where UserId in (VIPs | project UserId).






17
KQL
between Inclusive range check for numbers or datetimes.


    | where ResponseTime between (100 .. 500)
    | where TimeGenerated between (datetime(2026-04-01) .. datetime(2026-04-22))






18
KQL
Null and Empty Checks

    isnull(col) / isnotnull(col) — null check (numeric/datetime)
    isempty(col) / isnotempty(col) — empty-string check (strings)
    coalesce(a, b, c) — first non-null value Strings use isempty, everything else uses isnull. Mixing them up is a classic bug.






19
KQL
String Functions
    strcat(a, b, c) — concatenate
    strlen(s) — length
    substring(s, start, length)
    split(s, ";") — returns a dynamic array






20
KQL
String Functions
    tolower(), toupper()
    trim(@"\s+", s)
    — trim by regex
    replace_string(s, "old", "new")
    extract(@"Error (\d+)", 1, Message)
    — first regex capture group






21
KQL
parse Operator Turns unstructured strings into columns using a template.

T | parse Message with "User " user " logged in from " ip
Everything between the literals is captured into named columns. Faster and cleaner than chained extract() calls when the format is predictable. Use parse kind=regex for regex-based parsing.







22
KQL
Dynamic Types (JSON-like) dynamic holds arbitrary JSON: arrays, property bags, nested objects.

    parse_json(jsonString) — convert string to dynamic
    todynamic() — same thing
    Access nested: col.Level1.Level2 or col["key with space"]





23
KQL
Dynamic Types (JSON-like) dynamic holds arbitrary JSON: arrays, property bags, nested objects.

    Array index: arr[0]
    array_length(arr), bag_keys(obj) Gotcha: you must cast dynamic values before using them in summarize by, sort by, or join on — e.g., tostring(col.Id).






24
KQL
mv-expand — Array to Rows Turns one row with an array into multiple rows (like SQL UNNEST or CROSS APPLY).

T | mv-expand Tag = Tags
If Tags held ["red","blue","green"], you now get three rows. Use mv-apply when you need to filter or transform each element before expansion.







25
KQL
make_set, make_list, make_bag Aggregations that collect values into a dynamic array/object.

    make_set(Col) — unique values, no duplicates
    make_list(Col) — all values in order, duplicates kept
    make_bag(pack(...)) — property bag

ex
| summarize Devices = make_set(DeviceId) by UserId





26
KQL
Conditional Aggregations: countif, sumif, avgif


| summarize
    Errors = countif(Level == "Error"),
    Warnings = countif(Level == "Warning"),
    BigSpend = sumif(Amount, Amount > 1000)

Avoids filtering then re-joining — one pass, multiple conditional buckets.





27
KQL
DateTime Cheatsheet

    now() — current query time
    ago(7d) — 7 days before now
    Literals: datetime(2026-04-22), datetime(2026-04-22 10:30:00)
    Timespans: 1h, 30m, 7d, 500ms






28
KQL
DateTime Cheatsheet

    Parts: datetime_part("hour", t), dayofweek(t), monthofyear(t)
    Anchors: startofday(t), startofweek(t), startofmonth(t)
    Math: datetime1 - datetime2 → timespan; datetime + 1h → datetime






29
KQL

case() — Multi-way If/Else


| extend Severity = case(
    Latency < 100, "Fast",
    Latency < 500, "Normal",
    Latency < 2000, "Slow",
    "Critical")

Evaluates predicates top-to-bottom; last value is the default. Use iff(cond, a, b) for a simple two-way.







30
KQL
union Stacks rows from multiple tables (schemas unified).

union SecurityEvent, SigninLogs | where TimeGenerated > ago(1h)
Use union kind=outer (default) to keep all columns; kind=inner keeps only shared columns. Wildcards supported: union App_*.







31
KQL
render — Built-in Visualizations Last step of a query to chart results:

    render timechart — time-series line chart
    render barchart / columnchart
    render piechart
    render scatterchart Works directly in Log Analytics, Sentinel, and Fabric Real-Time Dashboards.






32
KQL
Common Beginner Mistakes

    Using = instead of == for equality (single = is assignment).
    Forgetting to project before a join — slower and leaks ambiguous columns.
    Relying on default join (hits the innerunique trap).






33
KQL
Common Beginner Mistakes

    Using contains where has would do the job.
    Using count() when you meant dcount().
    Expecting row order without calling sort + serialize.





34
KQL






35
KQL






36
KQL






37
KQL






38
KQL






39
KQL






40
KQL