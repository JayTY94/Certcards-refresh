
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






10
CCH Axcess






11
CCH Axcess






12
CCH Axcess






13
CCH Axcess






14
CCH Axcess






15
CCH Axcess






16
CCH Axcess






17
CCH Axcess






18
CCH Axcess






19
CCH Axcess






20
CCH Axcess






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