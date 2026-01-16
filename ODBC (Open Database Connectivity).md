ODBC (Open Database Connectivity)

A standardized API that allows applications to connect to and interact with different database systems using SQL, regardless of the underlying database vendor. ODBC achieves this through database-specific drivers that translate generic ODBC calls into native database protocols.

ODBC Driver

A database-specific translation layer that converts ODBC API calls into the native communication protocol of a database system. Each database type (e.g., SQL Server, Oracle, PostgreSQL) requires its own ODBC driver.

ODBC Driver Manager

An operating system component that loads the correct ODBC driver, manages handles, routes API calls, and enforces ODBC standards. It acts as an intermediary between applications and ODBC drivers but does not optimize or execute SQL itself.

Data Source Name (DSN)

An operating-system-level configuration that defines how an application connects to a database, including the driver, server address, database name, and sometimes credentials. DSNs can be User DSNs or System DSNs, with System DSNs required for services like Power BI gateways.

DSN-less Connection

A database connection method where all connection details (driver, server, database, credentials) are provided directly in the connection string instead of relying on a preconfigured DSN. This improves portability but can complicate credential management.

Environment Handle (HENV)

An ODBC handle representing the global ODBC context for an application. It defines environment-wide settings such as the ODBC version and must be created before any connections or statements can be used.

Connection Handle (HDBC)

An ODBC handle representing a logical connection to a specific data source. It manages authentication, transaction behavior, and connection-level attributes, even if the physical network connection is established lazily.

Statement Handle (HSTMT)

An ODBC handle representing a single SQL operation. It manages SQL execution, parameter binding, cursor state, and result sets. Multiple statement handles can exist simultaneously on a single connection.

Descriptor Handle (HDESC)

An internal ODBC structure that describes metadata about parameters and result sets, including data types, sizes, nullability, and memory layout. Most applications rely on automatically managed descriptors rather than interacting with them directly.

Cursor

A database construct used to navigate through rows in a result set. ODBC supports multiple cursor types (e.g., forward-only, static, dynamic), which affect performance, memory usage, and visibility of concurrent data changes.

Parameter Binding

A mechanism where variables are bound to placeholders in a SQL statement instead of embedding literal values directly. Parameter binding improves performance, enforces type safety, and protects against SQL injection.

Diagnostic Records

Structured error and warning information returned by ODBC functions instead of exceptions. Diagnostic records include SQLSTATE codes, native error codes, and human-readable messages, and multiple records may be returned for a single failure.

SQLSTATE

A five-character standardized error code used by ODBC to categorize errors and warnings. SQLSTATE values allow applications to handle errors consistently across different database systems and drivers.

Auto-commit

An ODBC connection mode where each SQL statement is automatically committed as its own transaction. Disabling auto-commit allows explicit transaction control using commit and rollback operations.

On-premises Data Gateway

A service installed within a local network that enables Power BI Service to securely access on-premises data sources. The gateway initiates outbound connections to Power BI and hosts the required database drivers.


Gateway Service Account

The operating system account under which the Power BI on-premises data gateway runs. This account determines which drivers, DSNs, and network resources the gateway can access and is critical for Windows authentication scenarios.