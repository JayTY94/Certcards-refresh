1. Custom Entities (Dataverse)
Definition: Custom entities in Dataverse are user-defined entities that are created to store application-specific data. They go beyond the standard predefined entities like Account, Contact, etc.
2. Lookup Field (Dataverse)
Definition: A Lookup Field is used in Dataverse to establish relationships between entities. It is typically used in Many-to-One and One-to-Many relationships to link records from different tables.
3. Power Automate Triggers - "When a Record is Modified"
Definition: This trigger in Power Automate is used to start a flow when an existing record in Dataverse is updated (modified), as opposed to when a new record is created or deleted.
4. Dataverse Maximum Record Size
Definition: In Dataverse, the maximum size for a single record, including all fields (and all data types), is 8MB. This applies to individual records, not entire tables.
5. Many-to-One Relationship (Dataverse)
Definition: A Many-to-One relationship in Dataverse refers to a relationship where multiple records in one entity can be related to a single record in another entity. For example, many contacts can be associated with a single account. This relationship is established using a Lookup field.
6. OData $filter (Query Option)
Definition: The $filter query option allows you to filter records based on a condition (e.g., Age gt 18 to find records where the age is greater than 18). It is used to narrow down the results from the OData query.
7. OData $orderby (Query Option)
Definition: The $orderby query option is used to specify the sorting order of the results in OData queries, either ascending (asc) or descending (desc).
8. OData $top (Query Option)
Definition: The $top query option in OData specifies the number of records to retrieve from the service, limiting the results to a specified number of records (e.g., $top=10 will return only the first 10 records).
9. OData $expand (Query Option)
Definition: The $expand query option is used to include related entities in the response. For example, when querying a Contact entity, you can use $expand=Account to include the related Account entity in the same response.
10. OData $count (Query Option)
Definition: The $count query option is used to retrieve only the number of records in an entity set, without returning the actual data. This is useful when you just need the record count.
11. OAuth 2.0 Authentication (Dataverse & Dynamics 365)
Definition: OAuth 2.0 is the authorization protocol used to authenticate and authorize applications and users accessing the Dataverse and Dynamics 365 Web APIs. It involves acquiring access tokens to interact with these services.
12. Web API (Dataverse and Dynamics 365)
Definition: The Web API in Dataverse and Dynamics 365 is a RESTful service that allows external applications to interact with the data. It supports CRUD operations (Create, Read, Update, Delete) and querying capabilities.
13. FetchXML (Dataverse Query Language)
Definition: FetchXML is a query language used in Dataverse and Dynamics 365. It is a proprietary language that is similar to SQL and is designed to retrieve data in a structured format, especially useful for complex queries and aggregations.
14. API Throttling (Dataverse)
Definition: API throttling refers to limiting the number of API requests a client can make within a specified time period. This helps prevent overload on the system and ensures fair use of resources across all users.
15. System Administrator Role (Dynamics 365)
Definition: The System Administrator role in Dynamics 365 grants full access to all data, settings, and configurations in the system. This role is typically required for making changes to the system and accessing the Web API.
16. Many-to-Many Relationship (Dataverse)
Definition: A Many-to-Many relationship allows multiple records in one entity to be related to multiple records in another entity. This is often implemented using a junction table or an intermediate entity to store these relationships.
17. Environment (Power Platform)
Definition: An Environment in the Power Platform is a container for data, applications, and resources. It can have its own Dataverse instance, and different environments are used for different stages of development (e.g., development, testing, production).
18. Entity Set (OData)
Definition: An Entity Set in OData represents a collection of entities of the same type. For example, a Contact entity set would represent all the contact records in the system.
19. Metadata Document (OData)
Definition: The Metadata document in OData is an XML document that describes the structure of the OData service, including the entities, relationships, and operations that are available for querying.
20. $batch (OData Query Option)
Definition: The $batch query option allows you to group multiple OData requests (e.g., create, update, or delete operations) into a single HTTP request. This improves performance by reducing the number of HTTP calls needed.