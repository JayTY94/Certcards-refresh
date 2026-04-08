1
Azure Policy
Azure Policy is a service that allows you to create, assign, and manage governance policies that enforce rules and effects over Azure resources to ensure that they stay compliant with your IT governance standards.





2
Azure Policy
Azure Policies are described in JSON format and are known as policy definitions.





3
Azure Policy
Azure Policy initiatives are a collection of Azure Policy definitions that are grouped together toward a specific goal or purpose.





4
Azure Policy
The five core disciplines of cloud governance:

Cost management – Evaluates and monitors costs, including controlling IT expenditures to establish well-defined cost management. It also includes adjusting resources according to demand. It's crucial to exercise control over cloud expenditure to derive greater value from your investments.





5
Azure Policy
The five core disciplines of cloud governance:

Security baseline – Ensures compliance with IT security requirements by applying a security baseline to all adoption efforts.






6
Azure Policy
The five core disciplines of cloud governance:

Resource consistency – Ensures consistency in resource configuration and enforcing practices for onboarding, recovery, and discoverability.





7
Azure Policy
The five core disciplines of cloud governance:

Identity baseline – Ensures that the baseline for identity and access is enforced by consistently applying role definitions and assignments.





8
Azure Policy
The five core disciplines of cloud governance:

Deployment acceleration – Accelerates the deployment of policies through centralization, consistency, and standardization across deployment templates.





9
Azure Policy
The five core disciplines of cloud governance are as follows:

    Cost management
    Security baseline
    Resource consistency
    Identity baseline
    Deployment acceleration 





10
Azure Policy
The compliance dashboard offered by Azure Policy presents an aggregated view of the environment's overall state, with the ability to examine details at each resource and each policy level.





11
Azure Policy
Some useful governance actions that you can enforce with Azure Policy include:

Ensure that your team deploys Azure resources only to allowed regions.
Enforce geo-replication rules to comply with your data residency requirements.






12
Azure Policy
Some useful governance actions that you can enforce with Azure Policy include:


Allow only certain virtual machine sizes for your cloud environment.
Enforce the consistent application of taxonomic tags across resources.
Recommend system updates on your servers.





13
Azure Policy
Some useful governance actions that you can enforce with Azure Policy include:

Allow multifactor authentication for all subscription accounts.
Require resources to send diagnostic logs to an Azure Monitor Logs workspace.





14
Azure Policy
In some cases, Azure Policy can automatically remediate noncompliant resources and configurations to ensure the integrity of the state of the resources. For example, if all resources in a specific resource group need to have the AppName tag with a value of SpecialOrders, Azure Policy can automatically apply that tag if it's missing.





15
Azure Policy
Azure Policy can prevent noncompliant resources from being created. Azure Policy comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring. 





16
Azure Policy
Azure provides four levels of management to establish proper governance: Management groups, Subscriptions, Resource groups, and Resources.





17
Azure Policy
Azure Policy initiatives, also known as a policy set, allow you to group several policy definitions to simplify assignments and management because you work with the initiatives as a single item. A JSON can be used to create a  policy initiative definition. 





18
Azure Policy
Use the Policy exemptions feature to exempt a resource hierarchy or an individual resource from evaluation of initiatives or definitions. Resources that are exempt count toward overall compliance but can't be evaluated or have a temporary waiver.





19
Azure Policy
An Azure Policy definition has two parts:

    A condition that compares a resource property field or value, accessed using aliases, to a required value.
    The effect determines what happens when the policy rule is evaluated to match the condition. For each new resource, an updated resource, or an existing resource, the effects behave differently.





20
Azure Policy
Multiple policies can be assigned to a single resource at the same scope or at different scopes. Each policy mostly has a different effect defined. The condition and effect for each policy is independently evaluated. The net result of layering policy definitions is considered cumulative most restrictive.







21
Azure Policy
Compliance scans through Azure policies are triggered by various methods:

    Automatic full scan - A full compliance scan is triggered automatically every 24 hours.
    Manual scan for Brownfield scenarios - In cases where a new policy is applied to existing resources (Brownfield scenarios), you can manually trigger a compliance scan by running az policy state trigger-scan.





22
Azure Policy






23
Azure Policy






24
Azure Policy






25
Azure Policy






26
Azure Policy






27
Azure Policy






28
Azure Policy






29
Azure Policy






30
Azure Policy






31
Azure Policy






32
Azure Policy






33
Azure Policy






34
Azure Policy






35
Azure Policy






36
Azure Policy






37
Azure Policy






38
Azure Policy






39
Azure Policy






40
Azure Policy