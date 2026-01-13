eDiscovery.md



1
eDiscovery
eDiscovery is a process used to identify, collect, and produce electronically stored information (ESI) during legal proceedings, internal investigations, audits, or regulatory reviews. This could include emails, chat messages, documents, or anything else stored digitally that's relevant to a case.







2
eDiscovery
Microsoft Purview integrates with Microsoft 365 services like Exchange, SharePoint, OneDrive, Teams, and Microsoft Defender to centralize the eDiscovery process. Instead of relying on manual collection or disconnected searches, Purview allows each step to be tracked, governed, and carried out consistently.





3
eDiscovery
A case brings together everything related to the investigation. It consolidates the searches, review sets, and any applied holds used throughout the lifecycle. You can also assign people to the case to control who has access.







4
eDiscovery
With the case created, the next step is to run searches to find relevant content. You can search across Exchange, SharePoint, OneDrive, and Teams using keywords or other filters. Search statistics help refine results, and you can preview content to make sure you're capturing what matters. 





5
eDiscovery
Depending on how responsibilities are structured in your organization, tasks might be split across different roles:

    eDiscovery Admins configure the overall setup, assign permissions, and manage global settings.
    eDiscovery Managers create and manage cases, run searches, and review content.





6
eDiscovery
1. A legal investigator at your organization needs to find emails and files related to a specific employee as part of an internal case. Which feature in Microsoft Purview should they use to organize searches, holds, and review actions?
    eDiscovery case






7
eDiscovery
Your organization is deciding whether to use the classic or new eDiscovery experience. They want to take advantage of automatic indexing and review sets. Which experience should they use?
    New eDiscovery





8
eDiscovery
A compliance officer needs to preserve all mailbox content for specific users while an investigation is ongoing. What should they do in Microsoft Purview?
    Add a legal hold






9
eDiscovery
A user in the eDiscovery Manager role group can't access a specific eDiscovery case. What is the most likely reason?    
    They haven't been added to the case






10
eDiscovery
Your organization uses Microsoft 365 E3 licensing. What eDiscovery capability would require an upgrade to E5 or an equivalent add-on?
    Using review sets to tag and filter content






11
eDiscovery
Standard eDiscovery features are included with Microsoft 365 and Office 365 E1, E3, and E5 plans. It supports case creation, content search, holds, and basic exports.
Premium eDiscovery features add capabilities like review sets, analytics, optical character recognition (OCR), and better export controls. It requires additional licensing.






12
eDiscovery
Certain Microsoft 365 apps must be enabled for eDiscovery to work correctly. These apps allow eDiscovery to access the content and features it needs to search and analyze across workloads.
ComplianceWorkbenchApp	92876b03-76a3-4da8-ad6a-0511ffdf8647
MicrosoftPurviewEDiscovery	b26e684c-5068-4120-a679-64a5d2c909d9
Microsoft Exchange Online Protection	00000007-0000-0ff1-ce00-000000000000
Office365Zoom	0d38933a-0bbd-41ca-9ebd-28c4b5ba7cb7






13
eDiscovery
To create a case:

    Go to the Microsoft Purview portal and sign in as a user with eDiscovery permissions.

    Select Solutions > eDiscovery to go to the Cases page.

    Select Create case.





14
eDiscovery
Access control is essential in Microsoft Purview eDiscovery. Case access is restricted to designated users and role groups, helping ensure sensitive investigations stay secure and traceable. Before someone can contribute to or review case content, they must have the appropriate permissions and be added to the case.







15
eDiscovery
Only users in the eDiscovery Administrator role group can remove other users from a case. Even if you originally created the case or are part of the eDiscovery Manager role group, you won't be able to remove users without elevated permissions.







16
eDiscovery
From the Case settings page, select Data sources, then choose one or more of the following options:

All people and groups including unlicensed, on-premises, and guest users
All people and groups including shared Teams channels
All people and groups including departed users






17
eDiscovery
A compliance officer needs to start an investigation into potential data leaks. What should they do first in Microsoft Purview eDiscovery?
    Create a new eDiscovery case.






18
eDiscovery
A legal team wants to ensure only certain users can access a case and its contents. What should they do after assigning eDiscovery permissions?

Add users to the appropriate case under Case settings.






19
eDiscovery
An organization wants to use review sets, analytics, and OCR in eDiscovery. What licensing requirement must they meet?

Assign Premium eDiscovery licenses to users whose data will be reviewed.






20
eDiscovery
A security analyst wants to include data from shared Teams channels and departed users in their search. What should they do?

Enable more data sources in the case settings.





21
eDiscovery
A reviewer is overwhelmed with duplicate emails in a large review set. What case setting should be enabled to help streamline their workflow?

Enable near duplicate and email threading in the Search and analytics settings.





22
eDiscovery
When you add a user or group to a case, eDiscovery automatically identifies and includes related locations. Data sources can include:

User mailboxes (email and calendar items)
OneDrive sites (files owned by the user)
SharePoint sites (including Teams channel files)
Teams messages (captured in Exchange mailboxes)
Yammer messages (if Yammer is enabled)
Public folders






23
eDiscovery
You can scope data sources in two ways:

Specific sources let you select individual users, groups, or sites
Tenant-wide sources include options like All people and groups or All public folders






24
eDiscovery
eDiscovery uses real-time sync to track changes in associated content. If a user's data locations change, such as when a new Teams private channel is created, you'll see an alert in the data source panel so you can include the new location.








25
eDiscovery
Sync also captures when content is removed or reassigned, such as:

OneDrive sites that are deleted or replaced
SharePoint sites that are moved or renamed
Mailboxes that are deactivated or reassigned





26
eDiscovery
In Microsoft Purview eDiscovery, preserve content that could be relevant to the case by placing content locations such as mailboxes, SharePoint sites, and OneDrive accounts on hold. This action prevents data from being permanently deleted until the hold is removed or the case is closed.







27
eDiscovery
You create a hold by defining a policy in an eDiscovery case. The policy determines which content to preserve and how long it should be retained. Depending on the investigation, a hold can preserve everything in a source or only content that matches a specific query.







28
eDiscovery
Each hold policy has a status that reflects its current state:

    Draft: The policy has been created but not applied. Navigating away before applying it discards the draft.
    On: The hold is active and content is being preserved.
    Off: The hold is no longer active, but the policy still exists.
    In progress: The policy is still applying or updating.
    Pending deletion: The policy is being deleted and is no longer preserving content.






29
eDiscovery
The Recoverable Items folder is a hidden mailbox location in Exchange Online used to store:

    Deleted items that haven't reached the end of their retention period
    Items retained by Litigation Hold, eDiscovery hold, or retention policies
    Metadata such as Bcc fields and expanded distribution group membership, if the mailbox is on hold

By default, users can't access this folder directly. It serves as a protected area for compliance and investigation purposes.





30
eDiscovery
When you remove a hold from a mailbox, Microsoft Purview applies a delay hold to prevent immediate data loss:

This hold lasts 30 days.
It gives you time to verify or recover data before permanent deletion.
You can remove a delay hold manually using PowerShell if needed.
Delay holds help avoid accidental data loss when changing hold configurations.







31
eDiscovery
You're setting up an eDiscovery search and want to include all content from a specific user's mailbox and OneDrive. What should you do?

Add the user as a data source






32
eDiscovery
You add a Microsoft 365 group as a data source, but you need to make sure chat messages and shared files from individual members are also preserved. What should you do?

Add individual group members as separate sources





33
eDiscovery
A hold was applied last week, but one user's OneDrive URL changed after a UPN update. What should you do?

Update the source path to reflect the new URL




34
eDiscovery
You remove a user's mailbox from a hold policy. What happens next?

A delay hold is applied for 30 days





35
eDiscovery
You're troubleshooting a hold and see an error for a SharePoint site. The hold status says 'read-only site.' What should you do?

Make the site writable, then retry the policy





36
eDiscovery
When configuring a search, you'll specify:

    • A search name and optional description
    • One or more data searches, such as users, groups, or sites
    • A query using conditions, keywords, or Keyword Query Language (KQL)






37
eDiscovery
The Condition builder lets you define filters to narrow the results returned by your search. You can use simple matching logic or combine conditions to focus on specific types of content.







38
eDiscovery
Available options in Condition builder incldue:
    KeyQL: Write advanced queries using Keyword Query Language.
    Date: Filter content based on sent, received, or modified dates.
    Subject/Title: Match specific terms in email subjects or document titles.
    Participants: Filter by sender, recipient, or other participants.
    Type: Filter by message kind, such as Email, Chat, or Teams.






39
eDiscovery
If you're working with evidence like chat logs, documents, or audit exports, you can use the Search by file option to find related content. This preview feature lets you upload sample data and use it as the basis for your search instead of writing manual queries.







40
eDiscovery
Why is every eDiscovery search in Microsoft Purview associated with a case?

To control access and provide an auditable investigation workspace.






1
eDiscovery
What roles are required to access and manage eDiscovery cases in Microsoft Purview?

eDiscovery Manager or eDiscovery Administrator





2
eDiscovery
What does the Search by file feature in eDiscovery allow you to do?

Upload sample content to find similar or referenced items.





3
eDiscovery
What is the purpose of the Statistics result type in eDiscovery search?

To view how many items matched your query and where they were found.






4
eDiscovery
What happens when you export search results in Microsoft Purview eDiscovery?

Results are packaged with reports and made available for download.





5
eDiscovery
In Microsoft Purview eDiscovery, review sets play a central role in managing the content you need to examine during a legal or compliance investigation. A review set is a static, organized collection of data that has been added to a case for deeper analysis.







6
eDiscovery
In Microsoft Purview eDiscovery, review sets are created as containers for holding static copies of content you want to analyze. You can create a review set on its own and add data later, or you can create one directly from a search.







7
eDiscovery
By default, review set items appear in pages of 50. Use the navigation controls to move between pages or enter a page number directly. If you prefer to scroll through all content without breaks, go to Manage and select Turn pagination off.







8
eDiscovery
When you apply a keyword filter, you can search across document content using search terms or even structured KQL-like syntax. Use Boolean operators such as AND, OR, NOT, and NEAR, and wildcards like ? and * to find partial matches. Keyword filters work well for narrowing down to items that mention specific terms in the body of emails or documents.







9
eDiscovery
Here are some of the things analytics can do for review sets:

Remove duplicate documents
Identify the most inclusive emails in a thread
Group near-duplicate files together
Organize content by theme
Flag potentially privileged material using machine learning






10
eDiscovery
A legal team is reviewing content in a case and wants to maintain a consistent, auditable record of data added for analysis. Why would they use a review set in Microsoft Purview eDiscovery?

To store a static set of content for focused review and tagging.





11
eDiscovery
You're analyzing a large volume of email data in a review set. What's the benefit of running analytics before starting manual review?

It reduces review volume by grouping near-duplicates and identifying key emails.





12
eDiscovery
You're reviewing tagged documents in a case and want to apply a consistent tagging structure across future cases. What should you do?

Import a predefined tag template created by an eDiscovery administrator.





13
eDiscovery
A case reviewer is using the filter panel in a review set to identify documents that are missing tags. What condition should they use?

Tag field with the 'Is empty' operator.





14
eDiscovery
Your team is preparing for export but wants to include all related items such as attachments and chat messages. Which export option should you enable?

Include associated family and conversation items




