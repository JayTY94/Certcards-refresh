



1
Exchange Online and Defender
An attacker can send email that passes SPF authentication (a false negative) by following these steps:
    Register a domain (for example, proseware.com) and configure SPF for the domain.
    Send email from a valid source for the registered domain, with the From email addresses in a different domain (for example, woodgrovebank.com).





2
Exchange Online and Defender
SPF breaks after messages encounter server-based email forwarding that redirects or relays messages.

    Server-based email forwarding changes the message source from the original server to the forwarding server.
    The forwarding server isn't authorized to send mail from the original MAIL FROM domain, so the message can't pass SPF authentication (a false positive).






3
Exchange Online and Defender
Each domain and any subdomains require their own individual SPF records. Subdomains don't inherit the SPF record of the parent domain. This behavior becomes problematic if you want to allow email from defined and used subdomains, but prevent email from undefined and unused subdomains.







4
Exchange Online and Defender
DKIM: As explained in Set up DKIM to sign mail from your cloud domain, DKIM uses a domain to digitally sign important elements of the message (including the From address) and stores the signature in the message header. The destination server verifies that the signed elements of the message weren't altered.







5
Exchange Online and Defender
How DKIM helps SPF: DKIM can validate messages that fail SPF. For example:

    Messages from an email hosting service where the same MAIL FROM address is used for mail from other domains.
    Messages that encounter server-based email forwarding.
    Because the DKIM signature in the message header isn't affected or altered in these scenarios, these messages are able to pass DKIM.





6
Exchange Online and Defender
As previously described, SPF makes no attempt to match the domain in MAIL FROM domain and From addresses. DKIM doesn't care if the domain that signed the message matches the domain in the From address. DMARC addresses these deficiencies by using SPF and DKIM to confirm that the domains in the MAIL FROM and From addresses match.









7
Exchange Online and Defender
Implicit email authentication extends regular SPF, DKIM, and DMARC checks by using signals from other sources to evaluate inbound email. These sources include:

    Sender reputation.
    Sender history.
    Recipient history.
    Behavioral analysis.
    Other advanced techniques.





8
Exchange Online and Defender
The results of Microsoft 365's implicit authentication checks are combined and stored in a single value named composite authentication or compauth for short. The compauth value is stamped into the Authentication-Results header in the message headers. The Authentication-Results header uses the following syntax:

Authentication-Results:
    compauth=<fail | pass | softpass | none> reason=<yyy>





9
Exchange Online and Defender
If you use only the Microsoft Online Email Routing Address (MOERA) domain for email (for example, contoso.onmicrosoft.com), the SPF TXT record is already configured for you. Microsoft owns the onmicrosoft.com domain, so we're responsible for creating and maintaining the DNS records in that domain and subdomains.





10
Exchange Online and Defender
If you use one or more custom domains for email (for example, contoso.com): The Microsoft 365 enrollment process already required you to create or modify the SPF TXT record in DNS for your custom domain to identify Microsoft 365 as an authorized mail source. However, you still have more work to do for maximum email protection






11
Exchange Online and Defender
Email authentication protection for undefined subdomains is covered by DMARC. Any subdomains (defined or not) inherit the DMARC settings of the parent domain (which can be overridden per subdomain). For more information, see Set up DMARC to validate the From address domain for cloud senders.







12
Exchange Online and Defender
Each subdomain that you use to send email from Microsoft 365 requires its own SPF TXT record. For example, the SPF TXT record for contoso.com doesn't cover marketing.contoso.com; marketing.contoso.com needs its own SPF TXT record.







13
Exchange Online and Defender
If you own registered but unused domains: If you own registered domains that aren't used for email or anything at all (also known as parked domains), configure SPF TXT records to indicate that no email should ever come from those domains as described later in this article.







14
Exchange Online and Defender
The basic syntax of the SPF TXT record for a custom domain in Microsoft 365 is:

v=spf1 <valid mail sources> <enforcement rule>
        Or:
v=spf1 [<ip4>|<ip6>:<PublicIPAddress1> <ip4>|<ip6>:<PublicIPAddress2>... <ip4>|<ip6>:<PublicIPAddressN>] [include:<DomainName1> include:<DomainName1>... include:<DomainNameN>] <-all | ~all>






15
Exchange Online and Defender
In Microsoft 365, you typically use IP addresses in the SPF TXT record only if you have on-premises email servers that send mail from the Microsoft 365 domain (for example, Exchange Server hybrid deployments). Some non-Microsoft email services might also use an IP address range instead of an include: value in the SPF TXT record.







16
Exchange Online and Defender






17
Exchange Online and Defender






18
Exchange Online and Defender






19
Exchange Online and Defender






20
Exchange Online and Defender






21
Exchange Online and Defender






22
Exchange Online and Defender






23
Exchange Online and Defender






24
Exchange Online and Defender






25
Exchange Online and Defender






26
Exchange Online and Defender






27
Exchange Online and Defender






28
Exchange Online and Defender






29
Exchange Online and Defender






30
Exchange Online and Defender






31
Exchange Online and Defender






32
Exchange Online and Defender






33
Exchange Online and Defender






34
Exchange Online and Defender






35
Exchange Online and Defender






36
Exchange Online and Defender






37
Exchange Online and Defender






38
Exchange Online and Defender






39
Exchange Online and Defender






40
Exchange Online and Defender