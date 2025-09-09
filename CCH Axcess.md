
31
CCH Axcess
When creating a client or editing an existing client, a check mark displays in the Meets Attributes column for any client access group where the client's general and administrative information meets the client attribute criteria as defined in the client access group profile.





32
CCH Axcess
Data flows from the client profile to tax returns. If the Firm > Setting and defaults > Tax > Options > Allow the option to update the client profile when changes are made to a tax return box is selected, you also have the option to update the client profile when changes are made to a tax return.








33
CCH Axcess
Token Authentication increases the security of firm and client data because:

    1. OIP applications do not need to handle usernames and passwords.
    2. The firm may enforce multi-factor authentication when a user is granting consent to an OIP application.
    3. Users may revoke consent to an OIP application without the need to change their password.





34
CCH Axcess
Resource - Some data or capability of a software platform. CCH Axcess Open Integration Platform (OIP) has resources for client, staff, firm, and other information.





35
CCH Axcess
Resource Server - The server that responds to API requests for a protected resource. For CCH Axcess this is usually published as part of api.cchaxces.com






36
CCH Axcess
Resource Owner - The CCH Axcess staff that can grant access to a protected resource. They can later revoke this consent if desired.






37
CCH Axcess
Authorization Server - The server that handles requests and responses for Oauth2 tokens. For CCH Axcess this is usually part of login.cchaxcess.com






38
CCH Axcess
Client Application - A software program that uses OIP APIs to obtain tokens and access protected resources on behalf of the resource owner. The term client in this context does not imply any specifics about the device where the application runs, only that it is making requests to and receiving responses from the resource server. 






39
CCH Axcess
We recommend using the following scopes for your OID application:
    CCHAxcess_data_writeaccess
    CCHAxcess_Profile
    IDInfo 
    offline_access 
    Openid - Required to have sub claims.





40
CCH Axcess
We recommend using the following scopes for your OID application:
    CCHAxcess_data_writeaccess - Allows the application to read or write CCH Axcess data as determined by the user's licenses and membership in security groups.
    CCHAxcess_Profile
    IDInfo 
    offline_access 
    Openid 





1
CCH Axcess
We recommend using the following scopes for your OID application:
    CCHAxcess_data_writeaccess 
    CCHAxcess_Profile - Provides additional information in the ID token about the authorizing user such as email and name. 
    IDInfo 
    offline_access 
    Openid 





2
CCH Axcess
We recommend using the following scopes for your OID application:
    CCHAxcess_data_writeaccess 
    CCHAxcess_Profile 
    IDInfo - Required to obtain the ID token that us used for logout.
    offline_access 
    Openid 





3
CCH Axcess
We recommend using the following scopes for your OID application:
    CCHAxcess_data_writeaccess 
    CCHAxcess_Profile
    IDInfo 
    offline_access - Required to obtain a refresh token.
    Openid 





4
CCH Axcess
Interpret the response from the CCH Axcess authorization token endpoint. When no errors take place and the status code is 200, the response body contains the following JSON name/value pairs:
    id_token - This JSON web token (JWT) is used for logout. It also contains useful information about the authorizing user if the application uses the scope CCHAxcess_Profile. 
    access token 
    expires_in 
    refresh_token





5
CCH Axcess
Interpret the response from the CCH Axcess authorization token endpoint. When no errors take place and the status code is 200, the response body contains the following JSON name/value pairs:
    id_token 
    access token - This JWT is used when making api requests for protected resources.
    expires_in 
    refresh_token






6
CCH Axcess
Interpret the response from the CCH Axcess authorization token endpoint. When no errors take place and the status code is 200, the response body contains the following JSON name/value pairs:
    id_token 
    access token 
    expires_in - The number of seconds until the access token expires. Refer to the next section for suggested use. 
    refresh_token 






7
CCH Axcess
Interpret the response from the CCH Axcess authorization token endpoint. When no errors take place and the status code is 200, the response body contains the following JSON name/value pairs:
    id_token 
    access token
    expires_in 
    refresh_token - A string that can be used to get new access and refresh tokens. Refer to the next section for suggested use.






8
CCH Axcess
The Authorization Code Flow (defined in OAuth 2.0 RFC 6749, section 4.1), involves exchanging an authorization code for a token.

This flow can only be used for confidential applications (such as Regular Web Applications) because the application's authentication methods are included in the exchange and must be kept secure.





9
CCH Axcess
The following terms are used to define your organizational unit hierarchy:

    Firm.
    Region (if used, requires at least one Office).
    Office (requires at least one Business Unit). An office can only be assigned to one region.
    Business Unit. A business unit can be assigned to one or more offices.






10
CCH Axcess
Once you assign a return default to an organization unit, if there is a configuration set assigned to a lower-level organization unit, the lower-level setting overrides the settings of the higher-level organizational unit. See Defining Your Firm's Organizational Unit Hierarchy for more information.






11
CCH Axcess
Return configuration sets are used to set default tax return input, such as signature block, correspondence options, and e-filing options. A return configuration set can then be selected or applied automatically to tax returns. Your firm can assign a return configuration set as the default for an organizational unit in Firm > Settings and defaults.





12
CCH Axcess
Each return must be assigned to a configuration set. If you have only one configuration set, it cannot be deleted. If you delete a configuration set with returns assigned to it, those returns are assigned to another configuration set that you specify during the deletion process.







13
CCH Axcess
Configuration sets that have been used for printing returns can be deleted. Those configuration sets will be soft deletedClosed and can be recovered and used to print exact duplicates of the returns they originally produced. Configuration sets that have never been used to print returns are permanently removed from the system and cannot be recovered.







14
CCH Axcess
Federal ID number (PTIN)
Enter the signer's federal Preparer Tax Identification Number (PTIN). It will display on all federal returns instead of the Social Security Number and is used for states conforming to the federal provision. The number must begin with a P.
Note: The PTIN, consisting of a P and the eight digits assigned to this preparer, must be formatted correctly or it will not save when you exit this window.





15
CCH Axcess
Use the Correspondence return configuration set windows to do the following:

    Configure your letter types and label options
    Customize a heading and complimentary close
    Customize options for letter and filing instructions content
    Configure grantor, custodial, and beneficiary letter preparation
    Customize stationery options for your letterhead and font





16
CCH Axcess
The term Pro Forma in CCH® ProSystem fx® Tax means to roll forward a return from one year to the next. The following video shows how to Pro Forma your returns using Tax.







17
CCH Axcess
If the Use "I" in all Letters option is selected for Organizers, the singular grammar variables I, me, and my are set automatically and are not flagged as potential grammar variables in Organizer letters.





18
CCH Axcess
You can use the Add Client window to enter minimal information about the new client, or you can click Client Profile to open the Client Profile window where you can enter more detailed information. See Entering General Client Information for more information.

If you have the right to add a client, you also have the ability to add a return.








19
CCH Axcess
You can change standard clients to any client type other than custom and custom clients to any other client type.
The availability of client types depends on returns that are associated with the client. See Changing Types for Clients with Returns below for more information.






20
CCH Axcess
You can change the client type for multiple clients by doing the following:

    Open Dashboard, click Application Links on the navigation panel, and then click Client Manager under Clients.
    In the Client Manager grid, select the check box to the left of each client to update. You must select 100 or fewer clients of the same client type.
    Select Update Multiple > Client Type Only from the Home ribbon.
    On the General window, change the client type selection.





21
CCH Axcess






22
CCH Axcess






23
CCH Axcess






24
CCH Axcess






25
CCH Axcess






26
CCH Axcess






27
CCH Axcess






28
CCH Axcess






29
CCH Axcess






30
CCH Axcess






31
CCH Axcess






32
CCH Axcess






33
CCH Axcess






34
CCH Axcess






35
CCH Axcess






36
CCH Axcess






37
CCH Axcess






38
CCH Axcess






39
CCH Axcess






40
CCH Axcess