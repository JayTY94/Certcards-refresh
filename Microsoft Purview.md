1
Microsoft Purview
Federated governance provides a centralized place to develop data safety, quality, and standards, but provides tools to create self-service access control, discoverability, and maintenance.







2
Microsoft Purview
Data access is about quickly providing the right access and enforcing the right use to balance safety and innovation.

Data curation is about organizing, annotating, and publishing your data so that it's safely accessible, reuseable, and protected.





3
Microsoft Purview
Data discovery is about ensuring users can find the data they need for day-to-day business and innovation.

Data health is about ensuring data quality standards are maintained across your estate, and having an active data lifecycle keeping your data fresh and secure.





4
Microsoft Purview
Data understanding is about ensure data has quality descriptors that help users understand what the data is and how it should be used.







5
Microsoft Purview
For organization-wide data consumers:
    Data discovery - helps you easily find the data you need.
    Secure access - facilitates safe access to your data.
    Data understanding - providing what you need to know about the data.






6
Microsoft Purview
For data owners and stewards:
    Data curation and management - helps you deliver high quality data that's easy to understand and safely access for organization-wide applications.
    Responsible data use - helps you ensure that your data is used by intended users for intended purposes.
    Impact analysis - understand actions on the data that may impact your data.






7
Microsoft Purview
For data officers and CxO stakeholders:
    Data value creation - maximize value creation from your data while reducing operations spend.
    Data estate standardization - create common controls across your data estate with federated accountability so your data is healthy and safe.






8
Microsoft Purview
Governance domains: Governance domains are a new way of organizing your data estate through business concepts, like Marketing or Finance, providing context for your data assets. A governance domain is a boundary that enables the common governance, ownership, and discovery of data products and business concepts like glossary terms, OKRs, or critical data.





9
Microsoft Purview
Related to business domains are data products. A data product is a business construct with a name, description, owners, and most importantly a list of associated data assets. The data product provides context for the assets that are included within it, and provides a use case for data consumers.







10
Microsoft Purview
A governance domain can house many data products but a data product is managed by a single governance domain and can be discovered across many domains.







11
Microsoft Purview
OKRs (objectives and key results) in Microsoft Purview are trackable business objectives tied to governance domains and data products to emphasize the value of business data.







12
Microsoft Purview
Microsoft Purview includes:
Sensitive information types to identify sensitive items by using built-in or custom regular expressions, or a function.
Trainable classifiers 
Data classification 






13
Microsoft Purview
Microsoft Purview includes:
Sensitive information types 
Trainable classifiers to identify sensitive items by using examples of the data you're interested in rather than identifying elements in the item.
Data classification 






14
Microsoft Purview
Microsoft Purview includes:
Sensitive information 
Trainable classifiers 
Data classification provides a graphical identification of items in your organization that have a sensitivity label, a retention label, or have been classified and the actions your users are taking on them






15
Microsoft Purview
Sensitivity labels provide users and admins with visibility into the sensitivity of the data that they're using, and the labels themselves can apply protection actions that include encryption, access restrictions, and visual markings. 





16
Microsoft Purview
In a data loss prevention policy, you:

    Define the sensitive information you want to monitor for, like financial, health, medical, and privacy data.
    Where to monitor, like Microsoft 365 services or Windows and macOS devices.
    The conditions that must be matched for a policy to be applied to an item, like items containing credit card, driver's license, or social security numbers.
    The actions to take when a match is found, like audit, block the activity, and block the activity with override.






17
Microsoft Purview
Microsoft Purview Privileged Access Management helps protect your organization from breaches and helps to meet compliance best practices by limiting standing access to sensitive data or access to critical configuration settings. Instead of administrators having constant access, just-in-time access rules are implemented for tasks that need elevated permissions.





18
Microsoft Purview
As you work with Data Map and Unified Catalog, keep these points in mind:

    All data in Data Map and Unified Catalog is metadata, not the underlying data itself.
    None of the permissions or roles in Data Map or Unified Catalog provide access to underlying data itself.






19
Microsoft Purview
Create the labels. Create and name your sensitivity labels according to your organization's classification taxonomy for different sensitivity levels of content. Use common names or terms that make sense to your users. You can then use sublabels to group similar labels by category.







20
Microsoft Purview
Define what each label can do. Configure the protection settings you want associated with each label. For example, you might want lower sensitivity content (such as a "General" label) to have just a header or footer applied, while higher sensitivity content (such as a "Confidential" label) should have a watermark and encryption.







21
Microsoft Purview
Publish the labels. After your sensitivity labels are configured, publish them by using a label policy. Decide which users and groups should have the labels and what policy settings to use. A single label is reusable—you define it once, and then you can include it in several label policies assigned to different users.





22
Microsoft Purview
Members of your compliance team who will create and sensitivity labels need permissions to the Microsoft Purview portal. You can use the following role groups:

    Information Protection
    Information Protection Admins
    Information Protection Analysts
    Information Protection Investigators
    Information Protection Readers






23
Microsoft Purview
The most effective end-user documentation will be customized guidance and instructions you provide for the label names and configurations you choose. You can use the label policy setting Provide users with a link to a custom help page to specify an internal link for this documentation.







24
Microsoft Purview
Extend SharePoint protection when files are downloaded when you configure a default sensitivity label for SharePoint document libraries and select the option to extend protection for unencrypted files. Then, when these files are downloaded, the current SharePoint permissions travel with the labeled file.







25
Microsoft Purview
Because a Sensitivity Label is stored in clear text in the metadata for files and emails, third-party apps and services can read it and then apply their own protective actions, if required.







26
Microsoft Purview
When viewed by users in your organization, an applied sensitivity label appears like a tag on apps and can be easily integrated into their existing workflows. Your sensitivity labels aren't visible in apps to users from other organizations, or to guests.







27
Microsoft Purview
When you create a sensitivity label, you're asked to configure the label's scope, which determines two things:

    Which label settings you can configure for that label
    The availability of the label to apps and services, which includes whether users can see and select the label






28
Microsoft Purview
The Groups & sites scope becomes available and selected by default when you enable sensitivity labels for containers and synchronize labels. This option lets you protect content in SharePoint sites, Teams sites, and Loop workspaces by labeling those containers but doesn't label the items in them.





29
Microsoft Purview
When you create your sensitivity labels in the Microsoft Purview portal, they appear in a list on the Labels page from Information Protection. In this list, the order of the labels is important because it sets their priority. You want your most restrictive sensitivity label, such as Highly Confidential to appear at the bottom of the list and your least restrictive sensitivity label, such as Personal or Public, to appear at the top.






30
Microsoft Purview
You can apply just one sensitivity label to an item such as a document, email, or container. If you use the option that requires your users to provide a justification for changing a label to a lower sensitivity for files, emails, and meetings, the order of this list identifies the lower sensitivity.





31
Microsoft Purview






32
Microsoft Purview






33
Microsoft Purview






34
Microsoft Purview






35
Microsoft Purview






36
Microsoft Purview






37
Microsoft Purview






38
Microsoft Purview






39
Microsoft Purview






40
Microsoft Purview