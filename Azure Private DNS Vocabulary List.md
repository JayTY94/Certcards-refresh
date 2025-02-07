Azure Private DNS Vocabulary List with Features

Private DNS Zone:
Definition: A container within Azure that holds DNS records for a private domain, resolvable only within the associated Azure Virtual Networks (VNets).
Feature: Azure Private DNS Zones allow automatic DNS resolution for internal resources within Azure, simplifying DNS management for internal services.

Public DNS Zone:
Definition: A DNS zone used for resolving publicly accessible resources on the internet.
Feature: While Azure Private DNS is for internal use, Public DNS Zones can be used in conjunction to handle external-facing resources.

Record Set:
Definition: A collection of DNS records for a specific hostname within a DNS zone.
Feature: Azure allows you to create and manage various types of record sets, including A, AAAA, CNAME, MX, PTR, and SOA, within Private DNS Zones.

A Record (Address Record):
Definition: A DNS record that maps a domain name to an IPv4 address.
Feature: You can add A records in your Private DNS Zone to associate domain names with internal Azure resources (like VMs and load balancers).

CNAME Record (Canonical Name Record):
Definition: A DNS record that maps one domain name to another domain name (aliasing).
Feature: Azure supports CNAME records, which allow you to alias internal resources, like services, within a Private DNS Zone.

AAAA Record:
Definition: A DNS record that maps a domain name to an IPv6 address.
Feature: Just like A records, AAAA records are supported in Private DNS Zones to handle IPv6 addresses for internal resources.

MX Record (Mail Exchange Record):
Definition: A DNS record that specifies the mail servers responsible for receiving email on behalf of a domain.
Feature: You can use MX records in your Private DNS Zone to manage email services for internal applications.

PTR Record (Pointer Record):
Definition: A DNS record that resolves an IP address to a domain name, typically used for reverse lookups.
Feature: Azure supports PTR records for reverse DNS lookups within a Private DNS Zone, which helps with troubleshooting and security.

SOA Record (Start of Authority Record):
Definition: A DNS record that defines the authoritative DNS server for a domain, along with other administrative data.
Feature: Azure automatically manages SOA records for each Private DNS Zone to define the authoritative source for that zone.
Virtual Network Link:

Definition: A configuration that links an Azure Virtual Network to a Private DNS Zone, enabling DNS resolution for resources within that VNet.
Feature: Virtual Network Links are a key feature that enables integration between Azure VNets and Private DNS Zones, allowing internal resources to resolve DNS names.

DNS Resolution:
Definition: The process by which a domain name is converted into an IP address.
Feature: Azure's Private DNS service automatically resolves domain names within the linked VNets, providing seamless internal DNS resolution without the need for custom DNS servers.

Registration-Enabled:
Definition: A setting that allows Azure to automatically create DNS records (e.g., A records) for VMs in the linked Private DNS Zone.
Feature: Registration-Enabled enables automatic DNS record creation for VMs that are deployed within a linked VNet, making it easier to resolve VM hostnames without manual intervention.

Resource Group:
Definition: A container in Azure that holds related resources.
Feature: Private DNS Zones are created within a Resource Group, simplifying the management and access control of DNS records and associated resources.

DNS Forwarding:
Definition: The process of forwarding DNS queries from one DNS server to another.
Feature: Azure Private DNS supports DNS forwarding to custom DNS servers or external DNS resolvers for scenarios involving hybrid DNS setups.

DNS Proxy:
Definition: A feature that allows DNS queries to be redirected from Azure resources to custom DNS servers.
Feature: DNS Proxy provides greater flexibility by enabling the use of your own DNS servers within your Azure environment.

Azure DNS Resolver:
Definition: The internal DNS resolver provided by Azure for resolving domain names within Azure services.
Feature: The Azure DNS Resolver resolves DNS queries for resources in the linked VNets and provides an efficient mechanism for internal DNS management.

Split-Horizon DNS:
Definition: A DNS setup where different DNS records are provided based on the requester's location.
Feature: Azure Private DNS can be used to implement split-horizon DNS, where the same domain name resolves differently for internal (private) and external (public) users.

DNS TTL (Time To Live):
Definition: The amount of time a DNS record is cached by DNS resolvers before a new lookup is performed.
Feature: You can configure DNS TTL values for records in your Private DNS Zone to control the caching behavior of DNS queries.

Azure Network Security Groups (NSG):
Definition: A set of rules used to control network traffic to and from Azure resources.
Feature: While NSGs are not directly involved in DNS, they are often used to secure the traffic to DNS servers (whether private or custom) in Azure, including DNS queries.

Hybrid DNS:
Definition: A DNS architecture that combines Azure DNS (Private and Public) with on-premises DNS services.
Feature: Azure Private DNS allows integration with hybrid DNS setups, where DNS queries can be resolved both within Azure and on-premises, facilitating a seamless DNS experience across environments.

DNS Zones Delegation:
Definition: The process of delegating authority for a DNS zone to another DNS server.
Feature: Delegation in Azure enables hybrid DNS setups and can be used to delegate the management of specific domains within your DNS infrastructure.

Custom DNS Server:
Definition: A DNS server specified for use in the VNet settings instead of the default Azure DNS.
Feature: Custom DNS servers can be used in combination with Azure Private DNS if you need to resolve DNS queries using on-premises or third-party DNS infrastructure.

Dynamic DNS (DDNS):
Definition: A DNS service that automatically updates DNS records when an IP address changes.
Feature: Dynamic DNS in Azure Private DNS helps automatically update DNS records (e.g., when VM IP addresses change) without manual intervention.

DNS Conditional Forwarding:
Definition: A feature that forwards DNS queries based on the domain being requested.
Feature: Azure supports DNS conditional forwarding to allow DNS queries for specific domains to be forwarded to a designated DNS server, often useful in hybrid cloud scenarios.

Automatic DNS Record Management:
Definition: A feature of Azure Private DNS that automatically manages DNS records for Azure resources.
Feature: Automatic DNS Record Management makes it easier to manage internal DNS records by automatically registering records for Azure resources such as VMs or load balancers in the Private DNS Zone.
