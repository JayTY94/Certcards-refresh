network tech.md 
RADIUS
Remote Authentication Dial-In User Service
A networking protocol for centralized AAA (Authentication, Authorization, Accounting).
......................................
RADIUS – Core Function
Provides centralized authentication for users connecting to network services.
Also handles authorization (what resources can be accessed) and accounting (usage tracking).
......................................
RADIUS – How It Works

Network device sends user credentials to RADIUS server via UDP (ports 1812/1813).
Server checks credentials against backend (e.g., Active Directory).
Responds with Access-Accept or Access-Reject.
......................................

RADIUS – Key Characteristics

Centralized management for multiple devices.
Uses shared secret and MD5 hashing (less secure than modern standards).
Common in enterprise Wi-Fi (802.1X), VPNs.
Lightweight protocol over UDP.
......................................

RADIUS – AAA Explained
Authentication: Verifies identity.
Authorization: Grants permissions.
Accounting: Logs usage for auditing/billing.
......................................
RADIUS – Security Note
Encrypts credentials during transmission but relies on older cryptographic methods.
Consider alternatives like TACACS+ or modern protocols for stronger security.
......................................
RADIUS – Common Use Cases

Enterprise Wi-Fi authentication.
VPN access control.
Historical dial-up connections.
......................................

RADIUS – Ports to Remember
UDP 1812 → Authentication.
UDP 1813 → Accounting.
......................................

WAN
Wide Area Network
A network that spans large geographic areas, connecting multiple LANs or MANs.
......................................
WAN – Core Purpose
Enables communication and resource sharing between distant networks or sites.
Used by businesses, ISPs, and global organizations.
......................................
WAN – Key Characteristics

Covers large distances (city, country, global).
Uses public or private transmission mediums (leased lines, satellite, MPLS).
Typically slower and more expensive than LAN.
......................................

WAN – Common Technologies

MPLS (Multiprotocol Label Switching).
VPN over Internet.
Dedicated leased lines.
SD-WAN for dynamic routing and cost optimization.
......................................

WAN – WAN vs LAN
LAN: Local Area Network, limited to a building or campus.
WAN: Connects multiple LANs across wide distances.
......................................
WAN – Typical Use Cases

Connecting branch offices to headquarters.
Linking data centers across regions.
Providing Internet access to LANs.
......................................

WAN – Performance Considerations
Higher latency than LAN due to distance.
Requires robust security (encryption, VPN).
Bandwidth costs can be significant.
......................................
WAN – Protocols and Standards
Common protocols: IP, MPLS, Frame Relay (legacy).
Often relies on carrier-grade infrastructure.