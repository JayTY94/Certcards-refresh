



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






5
Exchange Online and Defender






6
Exchange Online and Defender






7
Exchange Online and Defender






8
Exchange Online and Defender






9
Exchange Online and Defender






10
Exchange Online and Defender






11
Exchange Online and Defender






12
Exchange Online and Defender






13
Exchange Online and Defender






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
Exchange Online and Defender