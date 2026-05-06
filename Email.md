




1
Email
SMTP Ports — When Each Is Used

Port 25 — server-to-server SMTP. Used by Direct Send and connector-based relay (the device acts as a mail server).
Port 587 — submission port. Used by SMTP client submission against smtp.office365.com with STARTTLS. This is the "I'm a client authenticating as a mailbox" port.
Port 465 — legacy SMTPS, not used by M365 client submission.
Memory hook: 25 servers, 587 clients, 465 legacy.




2
Email
Direct Send — Key Constraint Drops mail at your tenant MX endpoint with no authentication, and Microsoft accepts it only for recipients in your accepted domains. Easy to set up, but internal-only. Update your SPF record to include the device's public IP, or messages will land in junk. Attackers actively abuse Direct Send to spoof internal senders — harden anti-spoof policies if you use it.






3
Email
SPF 10-Lookup Limit (RFC 7208) 
SPF evaluation costs DNS lookups — every include:, a, mx, ptr, exists counts at least one, and include: chains recurse. 
Cap is 10 lookups total. Hit 11+ and the result is permerror, treated as a hard fail by DMARC.
 Symptom: SPF passes for some receivers and fails for others. Fix: trim unused includes, or use SPF flattening.






4
Email
DKIM in Microsoft 365 — Two CNAMEs 
You publish two CNAMEs: selector1._domainkey.<domain> and selector2._domainkey.<domain>, both pointing into your <tenant>.onmicrosoft.com zone. 
Microsoft hosts the actual public-key TXT records. 
The two-selector design lets Microsoft rotate keys without you touching DNS — they sign with selector1, publish a new key at selector2, swap signing, then rotate selector1.






5
Email
SPF vs DKIM — What They Actually Authorize

SPF authorizes sending IP addresses — "this IP is allowed to send for my domain."
DKIM authorizes messages — a cryptographic signature proves the message wasn't altered and was signed by a server that holds the domain's private key.
DMARC requires that whichever one passes also aligns with the visible From: domain.





6
Email
Hybrid Exchange — Default vs Centralized Mail Transport

Default — Exchange Online sends outbound mail straight to the internet.
Centralized mail transport — Exchange Online routes outbound mail back through your on-prem Exchange first, which then sends to the internet.
Choose centralized when on-prem has something cloud doesn't — DLP gateway, journaling appliance, outbound encryption, regulatory archive. Cost: extra latency, hard dependency on on-prem.





7
Email
Gateway-in-Front-of-M365 Problem When your MX points to a third-party gateway (Mimecast, Proofpoint, Barracuda) that forwards to M365, EOP only sees the gateway as the sender. SPF passes against the gateway's IP — every time, regardless of the actual origin. Anti-spoof, DMARC, and IP reputation all weaken because the real source IP is invisible.






8
Email
Enhanced Filtering for Connectors (Skip Listing) The fix for the Gateway-in-Front-of-M365 Problem. 
Configure the partner connector with the gateway's IPs in the skip list. 
EOP then ignores those hops in the Received headers and evaluates SPF/anti-spoof against the IP that came before the gateway — the true origin.
Always enable this when M365 sits behind a third-party gateway.






9
Email
DMARC pct= Tag — Staged Rollout Specifies the percentage of failing messages to which the DMARC policy applies. Standard rollout:

    p=none; pct=100 — monitor only, collect aggregate reports
    p=quarantine; pct=10 — quarantine 10% of failures
    Ramp pct: 25 → 50 → 100
    p=reject; pct=100 — full enforcement

Going from p=none directly to p=reject is how you break payroll vendors and forwarders nobody documented.






10
Email
ACS Email vs Exchange Online — Decision Rule

Mailbox-shaped sending (a person or device acting as someone@contoso.com) → Exchange Online (SMTP AUTH, connector, Direct Send, or HVE for internal high-volume).
Application-shaped sending (transactional notifications, password resets, order confirmations) → Azure Communication Services Email.
ACS is per-message billed, no mailbox license needed, designed for high-volume external transactional traffic. Microsoft's recommended path for SaaS-style sending.





11
Email
Opportunistic TLS vs Forced TLS with Cert Validation

Opportunistic — default SMTP behavior. Uses STARTTLS if available, falls back to plaintext silently. Vulnerable to STARTTLS stripping and rogue certs.
Forced TLS + trusted CA + matching subject name (configured on a connector) — connection is rejected unless the cert is from a trusted CA and the subject matches the expected partner host. Blocks MitM. Use for regulated partner flows (legal, healthcare, financial).





12
Email
Connector Authentication Mechanisms

    Inbound from a partner / on-prem server → typically static IP match or certificate subject match (TLS).
    Inbound from a device for IP-based relay → static public IP listed on the connector.
    Modern application authenticating as a mailbox → OAuth 2.0 token via Microsoft Entra ID, not the connector itself.





13
Email
Forwarders and mailing lists rewrite headers, breaking SPF and often DKIM. 
ARC (Authenticated Received Chain) lets each intermediate hop record the auth results it observed and cryptographically sign that record. 
The final receiver can trust the chain even if SPF/DKIM no longer pass, preventing legitimate forwarded mail from being lost to DMARC enforcement.






14
Email
Basic Auth Deprecation Timeline (as of early 2026)

    SMTP AUTH Basic auth still works on existing tenants today.
    Disabled by default on existing tenants late December 2026.
    Final removal scheduled for H2 2027.
    Migration target: OAuth 2.0 for apps that can use MSAL; for devices that can't, move to connector-based relay (IP-authorized, survives the deprecation), HVE, or ACS Email depending on volume and recipient scope.





15
Email





16
Email





17
Email





18
Email





19
Email





20
Email





21
Email





22
Email





23
Email





24
Email





25
Email





26
Email





27
Email





28
Email





29
Email





30
Email





31
Email





32
Email





33
Email





34
Email





35
Email





36
Email





37
Email





38
Email





39
Email





40
Email





41
Email





42
Email





43
Email





44
Email





45
Email





46
Email





47
Email





48
Email





49
Email





50
Email





