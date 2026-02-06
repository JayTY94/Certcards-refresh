



23
Microsoft Purview
Sensitive information types (SITs) are used to help identify sensitive data so that you can prevent it from being inadvertently or inappropriately shared. They're also used to help in locating relevant data in eDiscovery, and to apply governance actions to certain types of information. 





24
Microsoft Purview
Sensitive information types (SITs) are used to help identify sensitive data so that you can prevent it from being inadvertently or inappropriately shared. You define a custom SIT based on:

    patterns
    keyword evidence such as employee, social security number, or ID
    character proximity to evidence in a particular pattern
    confidence levels






25
Microsoft Purview
Exact Data Match (EDM)-based classification enables you to  create custom SITs that refer to exact values in a database of sensitive information. The database can be refreshed daily and can contain up to 100 million rows of data.





26
Microsoft Purview
When you work with EDM SITs, it's helpful to understand a few concepts that are unique to them.

A schema is an XML file. Microsoft Purview uses the schema to determine whether or not your data contains strings that match those that your sensitive information types are designed to detect.





27
Microsoft Purview
Every sensitive information type has a rule package. You use the rule package in an EDM SIT to define the various components of your EDM SIT.

Match
    Specifies the primary element (data field) to be used in exact lookup. It can be a regular expression with or without a checksum validation, a keyword list, a keyword dictionary, or a function.
Classification	
Supporting elements	
Confidence level
Proximity




27
Microsoft Purview
Every sensitive information type has a rule package. You use the rule package in an EDM SIT to define the various components of your EDM SIT.

Match
Classification	
    Specifies the sensitive information type match that triggers an EDM lookup.
Supporting elements	
Confidence level
Proximity




27
Microsoft Purview
Every sensitive information type has a rule package. You use the rule package in an EDM SIT to define the various components of your EDM SIT.

Match
Classification	
Supporting elements	
    Elements that, when found, provide evidence that helps increase the confidence of the match. For example, the occurrence of a last name in close proximity to an actual social security number. A supporting element can be a regular expression with or without a checksum validation, a keyword list, a keyword dictionary, or a single- or multi-token string match.
Confidence level
Proximity




27
Microsoft Purview
Every sensitive information type has a rule package. You use the rule package in an EDM SIT to define the various components of your EDM SIT.

Match
Classification	
Supporting elements	
Confidence level
    (High, Medium, Low)	Indication of how much supporting evidence is detected in addition to the primary element. The more supporting evidence an item contains, the higher the confidence that a matched item contains the sensitive info you're looking for. For more information about confidence levels, see Fundamental parts of a sensitive information type.
Proximity




27
Microsoft Purview
Every sensitive information type has a rule package. You use the rule package in an EDM SIT to define the various components of your EDM SIT.

Match
Classification	
Supporting elements	
Confidence level
Proximity
    The number of characters between primary and supporting element.







28
Microsoft Purview
Microsoft Purview comes with many built-in SITs that are predefined. 
These SITs come with schemas, REGEX patterns, keywords, and confidence levels. 
Because the schema and primary and secondary data values are all highly sensitive, you encrypt them via a hash function that includes a randomly generated or self-supplied salt value. Only the hashed values are uploaded to the service.





29
Microsoft Purview
Multi-token matching is designed to be used when your corroborative evidence field contains multi-token values but matching such values to a SIT isn't easily accomplished. For instance, when you have an Address field containing values like 1 Microsoft Way, Redmond, WA or 123 Main Street, New York, NY.







30
Microsoft Purview
E5 license is required to make use of credential scanning SITs. For a list of all the credential scanning SITs, see All credentials sensitive information types. This SIT contains all the credential scanning SITs that are available in the portal. 





31
Microsoft Purview
Named entity SITs also show up in the Purview portal by default. They detect person names, physical addresses, and medical terms and conditions. They can't be edited or copied. For more information, see Learn about named entities.







32
Microsoft Purview
To understand how proximity works, let’s start by taking a look at some sample detection criteria. Here, were want to detect nine-digit social security numbers. The detection criteria require that a nine-digit regular expression (primary element) is found in conjunction with supporting evidence (among the AccountNumber, Name, and DateOfBirth fields) that appears within 250 characters (the proximity).







33
Microsoft Purview






34
Microsoft Purview






35
Microsoft Purview






36
Microsoft Purview






37
Microsoft Purview






38
Microsoft Purview






39
Microsoft Purview






40
Microsoft Purview