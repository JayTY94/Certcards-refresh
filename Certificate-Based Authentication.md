




1
Certificate-Based Authentication
X.509
The standard that defines the structure of a public-key certificate — fields like subject, issuer, serial number, validity dates, public key, and the issuer's signature. Every TLS/HTTPS, S/MIME, or smart-card cert you encounter is an X.509 certificate.





2
Certificate-Based Authentication
X.509 vs PKCS#12
- X.509 = the certificate itself (just the public side + identity + signature).
- PKCS#12 = a password-protected *container* (`.p12` / `.pfx`) bundling a certificate with its private key for transport.
- Memory hook: "X.509 is the ID card; PKCS#12 is the briefcase you carry it in."





3
Certificate-Based Authentication
PKCS#10 vs PKCS#12
- PKCS#10 = the CSR format. A signed *request* sent to a CA asking for a certificate.
- PKCS#12 = a container bundling an issued certificate + its private key.
- Memory hook: "10 asks, 12 stores."






4
Certificate-Based Authentication
Certificate Signing Request (CSR)
What you generate to ask a CA for a certificate. Contains your public key + identity info (CN, org, etc.), and is signed with your private key as proof of possession — proving you hold the matching private key. The CA verifies that signature, then issues the cert. Your private key never leaves your machine.





5
Certificate-Based Authentication
Proof-of-Possession Signature
The self-signature on a CSR that proves the requester holds the private key matching the public key in the request. Consumed at issuance — not present on the final certificate.






6
Certificate-Based Authentication
Subject Alternative Name (SAN)
The X.509 extension that lists additional hostnames a single cert covers (e.g., `www.site.com`, `api.site.com`, `site.com`). Modern browsers ignore the legacy Common Name (CN) field entirely and only validate hostnames against the SAN list.





7
Certificate-Based Authentication
Common X.509 Extensions — Quick Reference
- SAN — additional hostnames covered by the cert.
- Key Usage — what the key may do (digital signature, key encipherment, etc.).
- Basic Constraints — flags whether the cert is a CA (`cA:TRUE`) and a path length limit.
- AIA (Authority Information Access) — URLs to the issuer's cert and OCSP responder.





8
Certificate-Based Authentication
CRL (Certificate Revocation List)
A signed, time-stamped list of revoked certificate serial numbers, published periodically by the CA. Clients download and cache it. Simple, works offline once cached, but the list can grow large and freshness is bounded by the publish interval.





9
Certificate-Based Authentication
OCSP (Online Certificate Status Protocol)
Real-time, per-certificate revocation check. The client asks the CA's OCSP responder "is *this one* serial still valid?" — lightweight versus downloading a full CRL, but requires a live connection.






10
Certificate-Based Authentication
CRL vs OCSP
- CRL = bulk download of all revoked serials. Scales poorly as the list grows.
- OCSP = query one cert at a time. Lower bandwidth, but needs the responder to be reachable and leaks browsing data to the CA.
- Modern solution → OCSP stapling.





11
Certificate-Based Authentication
OCSP Stapling
The *server* fetches a recent signed OCSP response from the CA periodically and "staples" it to its TLS handshake. The client gets a freshness proof without phoning the CA. Solves three problems at once: latency, privacy leakage to the CA, and responder availability.
Anchor: "Stapling = the server brings the receipt with it."






12
Certificate-Based Authentication
OCSP Must-Staple
An extension baked into a certificate that tells clients: reject the connection unless a stapled OCSP response is present. Without must-staple, clients usually soft-fail when OCSP is unreachable, and an attacker who can block OCSP traffic exploits that. Must-staple closes the soft-fail hole.





13
Certificate-Based Authentication
Mutual TLS (mTLS)
TLS where both sides present certificates. Standard TLS only authenticates the server (e.g., browsing the web); mTLS additionally authenticates the client. Common in zero-trust networks, service meshes, and API-to-API auth. Same PKI machinery — just used both directions.





14
Certificate-Based Authentication
Root Certificate Trust — Why Roots Are Trusted
Root CAs are trusted because their certificates are preinstalled in the client's trusted root store (Windows, macOS, iOS, Android, browsers ship a curated list). Trust is bootstrapped by the OS/browser vendor's vetting process — *not* by any cryptographic signature on the root itself. Roots are self-signed; that's what makes them trust anchors.





15
Certificate-Based Authentication
Why Self-Signed Roots Aren't a Red Flag
Every root CA cert is self-signed (issuer = subject). It has to be — the chain has to terminate somewhere. The trust comes from out-of-band vetting (browser/OS root programs), not from another cert.






16
Certificate-Based Authentication
Subordinate (Intermediate) CAs — Why Use Them
The root's private key is kept offline in tightly protected hardware. Day-to-day signing is delegated to subordinate CAs. If a subordinate is compromised, you revoke and replace it without touching the root.






17
Certificate-Based Authentication
Certificate Pinning
Defends against the *trusted-but-malicious CA* problem. Normally, any CA in your root store can mint a valid cert for any domain — a compromised or coerced CA could issue a fraudulent cert for your bank. Pinning hardcodes which specific cert / public key / CA a client should accept for a given domain.
- HPKP (web pinning) was deprecated, largely replaced by Certificate Transparency.
- Mobile apps still pin heavily.





18
Certificate-Based Authentication
Certificate Transparency (CT) — quick context
Public append-only logs of every certificate issued by participating CAs. Misissued certs become visible publicly so domain owners can detect them. Complements (and on the web largely replaces) pinning.






19
Certificate-Based Authentication
Smart Card as an Auth Factor
A smart card storing a private key is "something you have" — the cryptographic key never leaves the card, and the card itself is the physical possession factor. Pair with a PIN ("something you know") to make CBA inherently multi-factor.





20
Certificate-Based Authentication
Why CBA Is "Phishing-Resistant"
The credential is cryptographically bound to the legitimate server's identity (TLS handshake transcript signed with the user's private key). A spoofed site can't get a usable signature out of the user because it isn't the real server. Nothing typeable means nothing replayable.





21
Certificate-Based Authentication
Private Key Compromise → Response
Revoke the certificate. Rotating usernames, passwords, or extending validity does nothing — the attacker holds the math. Revocation is the only correct first move; reissue afterward with a fresh key pair.






22
Certificate-Based Authentication






23
Certificate-Based Authentication






24
Certificate-Based Authentication






25
Certificate-Based Authentication






26
Certificate-Based Authentication






27
Certificate-Based Authentication






28
Certificate-Based Authentication






29
Certificate-Based Authentication






30
Certificate-Based Authentication






31
Certificate-Based Authentication






32
Certificate-Based Authentication






33
Certificate-Based Authentication






34
Certificate-Based Authentication






35
Certificate-Based Authentication






36
Certificate-Based Authentication






37
Certificate-Based Authentication






38
Certificate-Based Authentication






39
Certificate-Based Authentication






40
Certificate-Based Authentication






41
Certificate-Based Authentication






42
Certificate-Based Authentication






43
Certificate-Based Authentication






44
Certificate-Based Authentication






45
Certificate-Based Authentication






46
Certificate-Based Authentication






47
Certificate-Based Authentication






48
Certificate-Based Authentication






49
Certificate-Based Authentication






50
Certificate-Based Authentication






