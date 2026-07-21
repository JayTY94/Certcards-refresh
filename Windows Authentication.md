




1
Windows Authentication
Kerberos — The default Windows domain auth protocol. You prove your identity once and get a TGT (Ticket Granting Ticket), then trade that TGT for per-service tickets — no re-entering your password. Ticket-based, timestamped, and it fails if clocks drift more than 5 minutes.







2
Windows Authentication
KDC (Key Distribution Center) — The Kerberos brain that issues TGTs and service tickets. It runs on every DC — there's no separate KDC box — so "which DC am I on?" is "which KDC am I using?"







3
Windows Authentication
Netlogon — The service that maintains the secure channel between a member machine and a DC. It's the computer's own login to the domain, distinct from the user's login.







4
Windows Authentication
DC Locator — The client-side process that finds a DC. It queries DNS SRV records first, preferring a DC in its own AD site.







5
Windows Authentication
DNS SRV records — Service-location records DCs register so clients can find them. Generic: _ldap._tcp.<domain>, _kerberos._tcp.<domain>. Site-specific (queried first): _ldap._tcp.<site>._sites.<domain>. Stale or missing SRV records make authentication problems look like password problems.







6
Windows Authentication
AD Sites and Services — Maps IP subnets → physical sites so clients prefer a nearby DC. If a subnet isn't associated with the right site, the client can't tell where it is and may authenticate against a distant DC.







7
Windows Authentication
Secure Channel — The trust link between a domain member and the domain, protected by the computer account password. When it breaks you get "The trust relationship between this workstation and the primary domain failed."







8
Windows Authentication
Hybrid Entra Join — A device joined to on-prem AD and registered in Microsoft Entra ID at the same time. It lives in both worlds — which means it can fail in either.







9
Windows Authentication
Primary Refresh Token (PRT) — The artifact that gives an Entra-connected device single sign-on to cloud (and Entra-integrated) apps. The modern cloud equivalent of a Kerberos TGT.







10
Windows Authentication
PDC Emulator — The DC role that is the authoritative time source at the top of the domain's time hierarchy (plus urgent password changes and lockout). Because Kerberos is clock-sensitive, a drifting PDCe causes logon flapping.







11
Windows Authentication
W32Time — The Windows Time service that keeps each machine's clock chasing the PDCe. PDCe = the source; W32Time = the mechanism. Check with w32tm /query /status, fix with w32tm /resync.







12
Windows Authentication
Computer account password — Every domain-joined machine has its own password that auto-rotates ~every 30 days and must match AD. Restoring a VM from an old snapshot re-introduces a stale password → broken secure channel.







13
Windows Authentication
Automatic site coverage — When a site has no DC, a DC from the lowest-cost connected site (per site-link cost) registers that site's SRV records and covers it — deterministic, not random or broadcast.







14
Windows Authentication
TGT vs. service ticket — At logon you get a TGT (via AS-REQ/AS-REP). To reach a specific resource you exchange the TGT for a service ticket (via TGS-REQ/TGS-REP). New session = TGT; each resource = its own service ticket.







15
Windows Authentication
Cross-domain referral — Reaching a resource in another trusted domain, your home KDC can't issue that ticket directly — it returns a referral ticket pointing you at the other domain's KDC. More trusts = more hops = more places to flake.







16
Windows Authentication
CloudAP — The Cloud Authentication Provider plugin inside LSASS that requests, caches, and renews the PRT at sign-in, then hands out PRT-derived tokens for SSO. PRT problems show up in CloudAP's operational event logs.







17
Windows Authentication
PRT + TPM — The PRT's session key is bound to the device's TPM, so a copied PRT is useless on another machine. Clearing/resetting the TPM invalidates the PRT and forces re-auth.







18
Windows Authentication
PRT hybrid dependency — On a Hybrid Entra joined device, getting/refreshing the PRT requires the device to authenticate against an on-prem DC first, then Entra issues the PRT. So an on-prem DC outage can break cloud SSO even when the internet is fine — the key bridge between on-prem plumbing and cloud symptoms.







19
Windows Authentication
Checking the PRT — dsregcmd /status → look for AzureAdPrt : YES and the device-state/join fields. First command to run right after a hybrid sign-in failure.







20
Windows Authentication
NTLM — The legacy challenge-response protocol, no tickets or timestamps. Still present as a fallback when Kerberos can't be used.







21
Windows Authentication
Negotiate (SPNEGO) — The referee that picks the protocol: Kerberos first, NTLM as fallback. It does not pick a DC — that's DC Locator. Silent NTLM fallback often masks a broken Kerberos path.







22
Windows Authentication
SPN (Service Principal Name) — The unique name identifying a service in AD (e.g., MSSQLSvc/db01:1433). Kerberos needs it to encrypt the service ticket. Missing or duplicate SPNs → Kerberos fails → NTLM fallback.







23
Windows Authentication
PAC (Privilege Attribute Certificate) — Rides inside the Kerberos ticket carrying your group membership SIDs for authorization. A cached ticket holds a stale PAC after group changes — which is why access "starts working" after a sign-out or klist purge.







24
Windows Authentication
Global Catalog (GC) — Holds a partial, forest-wide copy of every object; queried at logon to expand universal group memberships and resolve UPN logons (user@domain.com). Has its own SRV records (_gc._tcp…).







25
Windows Authentication
Cached credentials — A stored verifier (not the actual password) from a prior successful logon, enabling offline sign-in with no DC reachable. Why the laptop logs in fine at the coffee shop.







26
Windows Authentication
Windows Hello for Business — cloud Kerberos trust — After a passwordless sign-in, Entra ID issues a partial TGT that the on-prem KDC honors, so the user can still reach on-prem resources. The simplest modern WHfB deployment model.







27
Windows Authentication
Conditional Access — A cloud policy engine that evaluates device, location, and risk before granting a token. Sits in the cloud sign-in flow — not on the DC, not near the TGT.







28
Windows Authentication
DC Locator vs. Negotiate vs. KDC — Three different verbs: DC Locator picks where you authenticate (which DC), Negotiate picks how (Kerberos vs NTLM), the KDC does the actual authenticating (issues tickets). Keep the verbs separate and the whole model holds together.







29
Windows Authentication
PHS vs. PTA vs. Federation — Three hybrid sign-in methods. PHS (Password Hash Sync): a hash-of-the-hash syncs up, password validated entirely in the cloud — most resilient. PTA (Pass-through Auth): an on-prem agent validates against a DC in real time — no hash in cloud, but inherits on-prem outages. Federation (AD FS): a separate on-prem farm handles auth — most moving parts.







30
Windows Authentication
PRT vs. TGT — Same idea, different worlds: the TGT is your on-prem Kerberos SSO artifact; the PRT is your Entra/cloud SSO artifact. A hybrid device holds both, and in hybrid the PRT actually depends on getting Kerberos working first.







31
Windows Authentication
Secure channel (machine) vs. user logon — Two separate authentications. "Trust relationship failed" = the computer's password/secure channel is broken (fix without rejoining). An expired user password is a different failure entirely.







32
Windows Authentication
Seamless SSO vs. PRT — Both give silent cloud sign-in. Seamless SSO uses on-prem Kerberos against the AZUREADSSOACC$ account (for domain-joined / browser scenarios); the PRT is the richer, modern path for Entra/Hybrid-joined devices.







33
Windows Authentication
dsregcmd /status	

Join state + PRT (AzureAdPrt : YES). Start here for hybrid/cloud sign-in issues.





34
Windows Authentication
nltest /dsgetdc:<domain>	

Shows which DC was located and the flags used — confirms site-aware selection.





35
Windows Authentication
Test-ComputerSecureChannel -Repair / nltest /sc_reset:<domain>

Test and repair a broken secure channel without rejoining (preserves the computer object/SID).





36
Windows Authentication
w32tm /query /status
w32tm /resync

Check and correct clock skew (Kerberos dies past 5 min).





37
Windows Authentication
klist / klist purge

View cached tickets / clear them to force a fresh TGT + PAC (fixes "stale group membership" access).





38
Windows Authentication
nslookup -type=srv _ldap._tcp.<domain>

Verify DCs are registering their SRV records in DNS.





39
Windows Authentication
The authentication path 
    Find a DC → DC Locator → DNS SRV lookup → Sites & Services picks the closest.
    Machine proves itself → Netlogon opens the secure channel (computer account password).
    User proves themselves → Kerberos AS-REQ → KDC on that DC → TGT issued.
    Reach resources → TGT → service tickets per app (each needs an SPN; each carries a PAC).
    Hybrid layer → device authenticates to a DC, then Entra issues a PRT for cloud SSO.





40
Windows Authentication






41
Windows Authentication






42
Windows Authentication






43
Windows Authentication






44
Windows Authentication






45
Windows Authentication






46
Windows Authentication






47
Windows Authentication






48
Windows Authentication






49
Windows Authentication






50
Windows Authentication






