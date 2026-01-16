Exchange Online Email Validation.md









2
Exchange Online and Defender
Authenticated Received Chain (ARC): If a non-Microsoft service modifies inbound messages before delivery to Microsoft 365, you can identify the service as a trusted ARC sealer (if the service supports it). Trusted ARC sealers preserve unmodified email information so the modified messages don't automatically fail email authentication checks in Microsoft 365.








3
Exchange Online and Defender
Domain-based Message Authentication, Reporting, and Conformance (DMARC): DMARC helps destination email servers decide what to do with messages from the custom domain that fail SPF and DKIM checks. Be sure to include the DMARC policy (p=reject or p=quarantine) and DMARC report destinations (aggregate and forensic reports) in the DMARC records. 








4
Exchange Online and Defender
DomainKeys Identified Mail (DKIM): DKIM signs outbound messages and stores the signature in the message header that survives message forwarding. 








5
Exchange Online and Defender
Sender Policy Framework (SPF): The SPF TXT record identifies valid sources of email from senders in the domain. For instructions, see Set up SPF to identify valid email sources for your custom cloud domains.








6
Exchange Online and Defender
If you're using the *.onmicrosoft.com domain for email (also known as the Microsoft Online Email Routing Address or MOERA domain), there's not nearly as much for you to do: 

SPF and DKIM are configured automatically
DMARC still needs to be manually set up via DNS records.








7
Exchange Online and Defender
Protection features have an unconfigurable order of processing. For example, incoming messages are always evaluated for malware before spam.
The threat policies of a specific feature (anti-spam, anti-malware, anti-phishing, etc.) are applied in a specific order of precedence.








8
Exchange Online and Defender
If a user is intentionally or unintentionally included in multiple policies of a specific feature, the first applicable threat policy for that feature (based on the order of precedence) determines what happens to the item (a message, file, URL, etc.).









9
Exchange Online and Defender
Once the first threat policy is applied to a specific item for a user, policy processing for that feature stops. No more threat policies of that feature are evaluated for that user and that specific item.









10
Exchange Online and Defender
If you decide to use custom threat policies, use the Configuration analyzer to periodically compare the settings in your policies to the recommended settings in the Standard and Strict preset security policies.










11
Exchange Online and Defender
Email & collaboration permissions in the Microsoft Defender portal: Administration of some security features in Defender for Office 365 is available with Email & collaboration permissions. For example:
    Configuration analyzer
    Admin quarantine management and quarantine policies
    Admin submissions and review of user reported messages
    User tags








12
Exchange Online and Defender
You can create allow entries for domains and email addresses and URLs on the corresponding tabs in the Tenant Allow/Block List to override the following verdicts:

    Bulk
    Spam
    High confidence spam
    Phishing (not high confidence phishing)









13
Exchange Online and Defender
You can't create allow entries directly in the Tenant Allow/Block List for the following items:

    Malware or high confidence phishing verdicts for domains and email addresses or URLs.
    Any verdicts for files.








14
Exchange Online and Defender









15
Exchange Online and Defender









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
Exchange Online Email Validation