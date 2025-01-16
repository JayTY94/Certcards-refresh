Vocabulary List


Trunk Port

Definition: A switch port configured to carry traffic for multiple VLANs using VLAN tagging protocols like IEEE 802.1Q, enabling seamless communication between switches across different VLANs.
VLAN Tagging

Definition: A method of identifying and segregating network traffic into different Virtual Local Area Networks within the same physical infrastructure by adding VLAN tags to Ethernet frames.
VLAN Tagging Hybrid Port

Definition: A switch port configuration that can handle both tagged (multiple VLANs) and untagged (single default VLAN) traffic simultaneously, allowing flexibility in connecting various devices.
VLAN ID (VLAN Identifier)

Definition: A unique number assigned to each VLAN (ranging from 1 to 4094) used to distinguish and manage VLAN traffic within a network, essential for proper VLAN tagging and segregation.
WirelessHART

Definition: An adaptation of the IEEE 802.15.4 standard for industrial automation, focusing on reliable and secure wireless communication in harsh environments, commonly used in manufacturing.
Wireshark

Definition: A popular network protocol analyzer used for capturing, inspecting, and analyzing network traffic, instrumental in passive network mapping, troubleshooting, and security analysis.
Zone-Based Firewall

Definition: A firewall architecture that defines security zones and policies for traffic between these zones, enhancing network security by controlling inter-zone communication based on defined rules.
Service Map Logical Topology

Definition: An abstract view within a Service Map that illustrates how services interact and depend on each other logically, focusing on data flows and service relationships rather than physical connections.

31. OpenFlow
Definition: A protocol enabling communication between SDN controllers and network devices. It allows centralized management of traffic flows by defining how switches handle incoming packets based on flow tables.
32. Address Space Layout Randomization (ASLR)
Definition: A security technique that randomly arranges the memory address space of a process, making it difficult for attackers to predict target addresses for exploits, thereby mitigating buffer overflow attacks.
33. Data Execution Prevention (DEP)
Definition: A security feature that marks certain memory regions as non-executable, preventing the execution of malicious code injected into data segments and enhancing protection against exploits like buffer overflows.
34. Quality of Service (QoS)
Definition: A set of technologies that prioritize certain types of network traffic, ensuring optimal performance for critical applications like VoIP and video streaming by managing bandwidth and reducing latency.
35. Return-Oriented Programming (ROP)
Definition: An exploitation technique that chains existing code snippets ("gadgets") within a program to execute arbitrary commands, bypassing security measures like DEP by avoiding the injection of new code.
36. Stack Canary
Definition: A security mechanism placed between buffers and control data on the stack. It detects buffer overflows by checking if the canary value has been altered before function returns, preventing unauthorized code execution.
37. Managed Switch
Definition: A network switch offering advanced features like VLANs, QoS, SNMP monitoring, and security settings. It provides greater control and flexibility for managing network traffic and configurations.
38. Meterpreter
Definition: An advanced, extensible payload in Metasploit that provides an interactive shell with capabilities like file system access, network pivoting, and process manipulation, all while running in memory to evade detection.
39. Network Access Control (NAC)
Definition: A security solution enforcing policies on devices attempting network access. It ensures only authorized, compliant devices connect, enhancing network security through authentication, authorization, and compliance checks.
40. Network Topology
Definition: The physical or logical arrangement of network devices and connections. It defines how devices are interconnected and how data flows within the network, influencing performance, scalability, and fault tolerance.
41. Software-Defined Networking (SDN) Controller
Definition: The centralized component in SDN architecture that manages network behavior by communicating with network devices via protocols like OpenFlow, enabling dynamic and programmable network management.
42. Trunk Port
Definition: A switch port configured to carry traffic for multiple VLANs using VLAN tagging (e.g., IEEE 802.1Q). It facilitates inter-switch communication by distinguishing VLAN traffic over a single physical link.
43. Virtual Local Area Network (VLAN)
Definition: A logical subdivision of a network, creating separate broadcast domains within the same physical infrastructure. VLANs enhance security, reduce broadcast traffic, and improve network management by segregating traffic.
44. RADIUS (Remote Authentication Dial-In User Service) Server
Definition: A networking protocol providing centralized Authentication, Authorization, and Accounting (AAA) for users accessing network services. Commonly integrated with NAC to enforce access policies based on user roles.
45. Security Information and Event Management (SIEM)
Definition: A comprehensive solution aggregating and analyzing log data from various sources in real-time. SIEM systems detect, alert, and help respond to security incidents by correlating events and identifying threats.
46. Access Control List (ACL)
Definition: A set of rules on network devices that permit or deny traffic based on criteria like IP addresses, protocols, and ports. ACLs enhance security by controlling access to network resources and segments.
47. Network Protocol Analyzer
Definition: A tool like Wireshark that captures, inspects, and analyzes network traffic. It aids in troubleshooting, performance monitoring, and security analysis by providing detailed insights into data packets.
48. Intrusion Detection System (IDS)
Definition: A security solution monitoring network or system activities for malicious actions or policy violations. IDS alerts administrators upon detecting suspicious behavior, aiding in threat identification and response.
49. Man-in-the-Middle (MitM) Attack
Definition: A cyberattack where the attacker intercepts and possibly alters communication between two parties without their knowledge, compromising data confidentiality and integrity through techniques like ARP spoofing or DNS spoofing.
50. Dynamic Host Configuration Protocol (DHCP) Snooping
Definition: A security feature that filters DHCP messages, ensuring only authorized DHCP servers can assign IP addresses. It prevents rogue DHCP servers from disrupting network configurations and conducting attacks.

ASLR
Address Space Layout Randomization
A security technique that randomly arranges the memory address space of a process, making it difficult for attackers to predict target addresses for exploits, thereby mitigating buffer overflow attacks.

CIDR
Classless Inter-Domain Routing
A method for allocating IP addresses and routing Internet Protocol packets, allowing for more efficient use of IP address space compared to traditional class-based addressing.


IPsec
Internet Protocol Security
A suite of protocols designed to secure Internet Protocol (IP) communications by authenticating and encrypting each IP packet in a communication session.

MPLS
Multi-Protocol Label Switching
A routing technique in high-performance telecommunications networks that directs data from one node to the next based on short path labels rather than long network addresses.

NAC
Network Access Control
A security solution that enforces policies on devices attempting to access a network, ensuring only authorized and compliant devices can connect through authentication, authorization, and compliance checks.

NAT
Network Address Translation
A method of remapping one IP address space into another by modifying network address information in IP packet headers while they are in transit, improving security and reducing the number of IP addresses an organization needs.

ROP
Return-Oriented Programming
An exploitation technique that chains existing code snippets ("gadgets") within a program to execute arbitrary commands, bypassing security measures like DEP by avoiding the injection of new code.

RP
Remote Procedure
A protocol that one program can use to request a service from a program located in another computer on a network without having to understand the network's details.


