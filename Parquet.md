




1
Parquet
Parquet — One-Line Definition

An open-source, columnar storage file format maintained by the Apache Software Foundation, designed for efficient analytical queries on large datasets.





2
Parquet
Row-Based vs. Columnar Storage

- Row-based (CSV, MySQL): all fields of one record stored together. Good for OLTP — fetching/updating whole records.
- Columnar (Parquet, ORC): all values of one column stored together. Good for OLAP — scanning a few columns across billions of rows.






3
Parquet
Parquet File Structure (Mental Model)

```
File
 └─ Row Group  (128–512 MB, unit of parallelism, holds min/max stats)
     └─ Column Chunk  (one per column, contiguous on disk)
         └─ Page  (~1 MB, unit of encoding + compression)
```

Wrapped at both ends with the magic bytes `PAR1`. Footer sits at the end.






4
Parquet
Magic Bytes

Every Parquet file starts AND ends with the 4-byte magic number `PAR1`. The last 8 bytes of the file are: `[4-byte footer length][PAR1]`. Readers use this to locate the footer.





5
Parquet
The Footer

Stored at the end of the file. Contains the schema, row group locations, column chunk byte offsets, and min/max statistics. A reader opens a Parquet file by jumping to the end first, reading the footer, and using it as a map.






6
Parquet
Why Footer-at-End Matters

Writers can stream data out without knowing the final schema or stats up front — they accumulate metadata as they go and write it once at the close. Readers only need a small range read (the footer) to plan the entire query.





7
Parquet
Row Group

A horizontal partition of the table — typically 128 MB to 512 MB worth of rows. Each row group contains one column chunk per column. Row groups are the unit of parallelism (one worker per group) and the unit at which min/max statistics are tracked.





8
Parquet
Column Chunk

Within a row group, each column is stored as a contiguous column chunk. This is what makes column pruning possible — readers seek directly to the chunks they need and skip the rest.






9
Parquet
Page

The smallest unit of compression and encoding inside Parquet. A column chunk is split into multiple pages (~1 MB each), and each page is encoded and compressed independently. This lets readers decompress only the pages they need.





10
Parquet
Hierarchy 

File → Row Groups → Column Chunks → Pages → Encoded values. Memorize this — most Parquet concepts map onto one of these four levels.





11
Parquet
Column Pruning

When a query selects only a few columns, Parquet reads just those column chunks from disk and skips all others. Possible because each column is stored contiguously in its own chunk. This is "select fewer columns = read fewer bytes."





12
Parquet
Predicate Pushdown

When a query has a `WHERE` filter, Parquet uses min/max statistics stored per row group to skip groups whose range can't match. Example: `WHERE age > 100` on a row group with max age 80 → skip the whole group without decompressing it.






13
Parquet
Column Pruning vs. Predicate Pushdown

- Column pruning skips columns based on what's `SELECT`-ed.
- Predicate pushdown skips rows (row groups) based on `WHERE` filters and min/max stats.

Both reduce IO; they're complementary, not the same thing.






14
Parquet
Min/Max Statistics

Every row group stores the min and max value per column in the footer. These are the engine behind predicate pushdown. Sorting your data on the filter column makes these ranges tight and dramatically improves skip rates.






15
Parquet
Sorted Writes Improve Performance

Writing Parquet sorted by a frequently-filtered column makes each row group's min/max range tight and non-overlapping. More queries can skip more groups. Unsorted data tends to give every row group a wide range that matches almost any predicate.





16
Parquet
Bloom Filters

A probabilistic data structure that answers "is value X definitely NOT in this row group?" Useful for equality predicates on high-cardinality columns (e.g., `user_id = 'abc123'`) where min/max ranges are too wide to help. Cannot help with range queries — those are min/max's job.





17
Parquet
Min/Max vs. Bloom Filters

- Min/max → range predicates (`age > 50`, `date BETWEEN ...`)
- Bloom filters → equality predicates on high-cardinality columns (`user_id = 'X'`)

Both live in row group metadata; Parquet uses whichever fits the query.






18
Parquet
Self-Describing Schema

Parquet embeds its full schema (column names, types, nesting structure) in the file footer. No external schema file needed — any reader can open any Parquet file and immediately know its structure. Major advantage over CSV.






19
Parquet
Dictionary Encoding

For columns with low cardinality (few distinct values across many rows — country codes, status flags, categories), Parquet builds a small dictionary of unique values and stores each row as a tiny integer index into that dictionary. Often compresses 10–100x. The default encoding for most string columns.





20
Parquet
Other Encodings

- Plain — raw values, fallback when nothing else fits.
- Dictionary — small set of repeated values.
- Run-Length Encoding (RLE) — long runs of identical values.
- Delta — sorted or near-sorted numeric sequences (stores differences, not values).
- Bit-packing — small integers packed into the minimum bits needed.

Encoding is chosen per page based on the data.





21
Parquet
Compression Codecs

Common Parquet codecs:
- Snappy — default, fast, moderate ratio.
- Gzip — slower, better ratio.
- ZSTD — modern, tunable speed/ratio, often beats both.
- LZ4 — very fast, lower ratio.

Encoding happens first (reduces redundancy), then compression on the encoded bytes.





22
Parquet
Encoding vs. Compression

- Encoding — a smarter way to represent values (dictionary, delta, RLE). Data-aware.
- Compression — a general-purpose byte-level squeeze (Snappy, Gzip, ZSTD). Data-agnostic.

Parquet applies both, in that order, per page.





23
Parquet
Dremel Model

The algorithm Parquet uses to store nested data (structs, arrays, maps) in pure columnar form. Originally published by Google. Each leaf field becomes its own column, accompanied by two extra integers per value: definition level and repetition level.





24
Parquet
Definition Level

Indicates how many of a field's optional/nullable ancestors are actually present in this record. Tells the reader at what point in a nested path a null occurred. Distinguishes "the whole struct is missing" from "the struct exists but this field is null."





25
Parquet
Repetition Level

Indicates at which nesting level a new list element begins. Value 0 means "start of a new record"; higher values mean "continuation of an existing list at level N." Handles repeated fields and arrays.





26
Parquet
When NOT to Use Parquet

- Frequent single-row updates (OLTP) — Parquet is immutable and write-once.
- Tiny files where overhead dominates.
- Anything humans need to read directly (it's a binary format).
- Workloads dominated by full-record fetches rather than column scans.





27
Parquet
Cloud Object Storage (S3/ADLS/GCS) Friendliness

Parquet's footer-at-end + per-column-chunk byte offsets make it ideal for HTTP byte-range reads. A reader on S3 fetches the footer (small range read), then issues targeted GETs only for the column chunks it needs. No companion files, no full downloads.





28
Parquet
Parquet vs. ORC

Both are columnar, both used in Big Data. ORC originated in the Hive ecosystem; Parquet in the Spark/Twitter/Cloudera ecosystem. Performance is broadly comparable. Parquet has won in the cloud and Python data ecosystems; ORC remains common in legacy Hadoop/Hive deployments.





29
Parquet
Parquet vs. Avro

- Parquet → columnar, optimized for analytical reads.
- Avro → row-based, optimized for streaming, message passing, and write-heavy workloads (e.g., Kafka).

Use Avro when you write a lot and read whole records. Use Parquet when you read selectively across many records.





30
Parquet






31
Parquet






32
Parquet






33
Parquet






34
Parquet






35
Parquet






36
Parquet






37
Parquet






38
Parquet






39
Parquet






40
Parquet






41
Parquet






42
Parquet






43
Parquet






44
Parquet






45
Parquet






46
Parquet






47
Parquet






48
Parquet






49
Parquet






50
Parquet






