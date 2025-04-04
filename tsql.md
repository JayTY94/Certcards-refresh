Column and Table Aliasing:

Use the AS keyword to rename columns and tables (e.g., ts_name AS ar_adjustment_name).
Consistent naming conventions (like using underscores) improve readability and maintenance.


JOIN Types and Conditions:

FULL OUTER JOIN: Returns rows when there is a match in either table, useful for capturing unmatched records.
Self-Joins: Joining a table to itself using different aliases to handle relationships within the same table.


Inline Comments in SQL:

Use -- to add descriptive comments that explain parts of your query, making it easier to understand later.




COALESCE Function:

Returns the first non-null value from a list of expressions (e.g., COALESCE(ts_invoiceid, inv.ts_invoiceid)).




CASE Expressions:

Implements conditional logic within queries to create computed columns or flags (e.g., flagging which date or account source is used).




SQL Query Formatting:

Consistent indentation and spacing make queries easier to read, especially as complexity increases.




Indexing Considerations:

Ensure columns used in JOINs or WHERE clauses are indexed for better performance.




Self-Joins for Hierarchies:

Useful for comparing or relating data within the same table.
Effective for simple or fixed-level hierarchies; consider recursive CTEs for deep or variable hierarchies.




Pivoting Data:

Use the PIVOT operator to transform rows into columns for reporting or data summarization.




Set Operations:

UNION / UNION ALL: Combine result sets from multiple queries (with or without duplicate removal).
INTERSECT: Returns rows common to both queries.
EXCEPT: Returns rows from the first query that do not appear in the second.




Common Table Expressions (CTEs):

Defined with the WITH clause to create temporary result sets within a query.
Recursive CTEs: Handle hierarchical data by repeatedly referencing the CTE itself.




Subqueries:

Queries nested within other queries (in SELECT, FROM, or WHERE clauses) to return single or multiple values.




Derived Tables:

Subqueries in the FROM clause that act as temporary tables with an alias.




Temporary Tables:

Created with a hash (#) prefix to hold intermediate results for complex or staged queries.




Table Variables:

Declared using DECLARE and used similarly to temporary tables, often for smaller data sets with a more limited scope.




Stored Procedures:

Precompiled TSQL routines that encapsulate one or more SQL statements, enhancing reusability, performance, and security.




User-Defined Functions (UDFs):

Custom functions that return scalar values or tables, encapsulating reusable logic.




Transactions and Isolation Levels:

Use BEGIN TRANSACTION, COMMIT, and ROLLBACK to group related SQL statements, ensuring data integrity.
Isolation levels (e.g., READ COMMITTED) manage concurrency and data consistency.




Error Handling with TRY...CATCH:

Handle runtime errors gracefully, allowing you to manage exceptions and roll back transactions when necessary.




Dynamic SQL:

Build and execute SQL statements dynamically at runtime using sp_executesql or EXEC(), which is useful when the query structure must adapt to input parameters.




Window Functions:

Functions like ROW_NUMBER(), RANK(), LEAD(), and LAG() perform calculations across sets of rows related to the current row without collapsing the result set.







Flashcard 1
Q: What happens in T-SQL if you use GROUP BY but select columns that are not aggregated or not in the GROUP BY clause?
A: You get an error. All columns in the SELECT must either be part of the GROUP BY clause or be wrapped in an aggregate function like SUM, AVG, MAX, etc.

Flashcard 2
Q: What is the purpose of the GROUP BY clause in T-SQL?
A: It collapses rows into groups based on the values of one or more columns and applies aggregate functions to each group.

Flashcard 3
Q: How do window functions differ from aggregate functions with GROUP BY?
A: Window functions (like SUM(...) OVER (...)) calculate values across sets of rows without collapsing them into a single row, preserving the full row data.

Flashcard 4
Q: What does SUM(x) OVER (PARTITION BY y) do?
A: It sums the values of x for each group of rows where y has the same value, but keeps each row intact in the result set.

Flashcard 5
Q: Why would you use COALESCE(a, b) in a SELECT statement?
A: It returns the first non-null value among its arguments. Useful for fallback values like choosing between custom and default rates.

Flashcard 6
Q: When should you use window functions instead of GROUP BY?
A: When you want to calculate totals, ranks, or running sums without reducing the number of rows in your result set.

