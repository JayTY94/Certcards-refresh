1
OAuth 2.0 RFC6749
In OAuth, the client requests access to resources controlled
   by the resource owner and hosted by the resource server, and is
   issued a different set of credentials than those of the resource
   owner.





2
OAuth 2.0 RFC6749
Instead of using the resource owner's credentials to access protected
   resources, the client obtains an access token -- a string denoting a
   specific scope, lifetime, and other access attributes.  





3
OAuth 2.0 RFC6749
Access tokens
   are issued to third-party clients by an authorization server with the
   approval of the resource owner.  The client uses the access token to
   access the protected resources hosted by the resource server.






4
OAuth 2.0 RFC6749
For example, an end-user (resource owner) can grant a printing
   service (client) access to her protected photos stored at a photo-
   sharing service (resource server), without sharing her username and
   password with the printing service.  Instead, she authenticates
   directly with a server trusted by the photo-sharing service
   (authorization server), which issues the printing service delegation-
   specific credentials (access token).






5
OAuth 2.0 RFC6749
The OAuth 1.0 protocol ([RFC5849]), published as an informational
   document, was the result of a small ad hoc community effort.  This
   Standards Track specification builds on the OAuth 1.0 deployment
   experience, as well as additional use cases and extensibility
   requirements gathered from the wider IETF community.  The OAuth 2.0
   protocol is not backward compatible with OAuth 1.0. 





6
OAuth 2.0 RFC6749
OAuth defines four roles:

   resource owner
      An entity capable of granting access to a protected resource.
      When the resource owner is a person, it is referred to as an
      end-user.

   resource server
   client
   authorization server





7
OAuth 2.0 RFC6749
OAuth defines four roles:

   resource owner
   
   resource server
      The server hosting the protected resources, capable of accepting
      and responding to protected resource requests using access tokens.

   client
   authorization server
   




8
OAuth 2.0 RFC6749
OAuth defines four roles:

   resource owner
   resource server

   client
      An application making protected resource requests on behalf of the
      resource owner and with its authorization.  The term "client" does
      not imply any particular implementation characteristics (e.g.,
      whether the application executes on a server, a desktop, or other
      devices).

   authorization server




9
OAuth 2.0 RFC6749
OAuth defines four roles:

   resource owner
   resource server
   client

   authorization server
      The server issuing access tokens to the client after successfully
      authenticating the resource owner and obtaining authorization.





10
OAuth 2.0 RFC6749
An authorization grant is a credential representing the resource
   owner's authorization (to access its protected resources) used by the
   client to obtain an access token.  This specification defines four
   grant types -- authorization code, implicit, resource owner password
   credentials, and client credentials -- as well as an extensibility
   mechanism for defining additional types.






11
OAuth 2.0 RFC6749
The authorization code is obtained by using an authorization server
   as an intermediary between the client and resource owner.  Instead of
   requesting authorization directly from the resource owner, the client
   directs the resource owner to an authorization server (via its
   user-agent as defined in [RFC2616]), which in turn directs the
   resource owner back to the client with the authorization code.





12
OAuth 2.0 RFC6749






13
OAuth 2.0 RFC6749






14
OAuth 2.0 RFC6749






15
OAuth 2.0 RFC6749






16
OAuth 2.0 RFC6749






17
OAuth 2.0 RFC6749






18
OAuth 2.0 RFC6749






19
OAuth 2.0 RFC6749






20
OAuth 2.0 RFC6749






21
OAuth 2.0 RFC6749






22
OAuth 2.0 RFC6749






23
OAuth 2.0 RFC6749






24
OAuth 2.0 RFC6749






25
OAuth 2.0 RFC6749






26
OAuth 2.0 RFC6749






27
OAuth 2.0 RFC6749






28
OAuth 2.0 RFC6749






29
OAuth 2.0 RFC6749






30
OAuth 2.0 RFC6749






31
OAuth 2.0 RFC6749






32
OAuth 2.0 RFC6749






33
OAuth 2.0 RFC6749






34
OAuth 2.0 RFC6749






35
OAuth 2.0 RFC6749






36
OAuth 2.0 RFC6749






37
OAuth 2.0 RFC6749






38
OAuth 2.0 RFC6749






39
OAuth 2.0 RFC6749






40
OAuth 2.0