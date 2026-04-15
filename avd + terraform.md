Desktop Virtualization User (DVU) role
Azure RBAC role that allows a user to see and launch desktops or apps in AVD.
✅ Must be scoped to the Application Group, not the resource group.
......................................
Microsoft Entra ID (Azure AD)
Cloud identity provider used by AVD for authentication. Can authenticate directly to Windows VMs when properly enabled.
......................................
Entra ID–joined VM
A VM joined directly to Entra ID (not AD).
Verified with dsregcmd /status → AzureAdJoined : YES.
......................................
AADLoginForWindows extension
Azure VM extension that enables Entra ID authentication for Windows logon.
Registers CloudAP credential providers and allows Entra users to sign in to Windows.
......................................
System‑assigned managed identity
A VM identity required for Entra login + RBAC evaluation.
Required by AADLoginForWindows.
......................................
Virtual Machine Administrator Login role
Azure RBAC role that allows interactive Windows logon with admin rights via Entra ID.
✅ Must be assigned at VM, resource group, or subscription scope.
......................................
Virtual Machine User Login role
Same as above, but for non‑admin Windows access.
......................................
Two‑plane access model (AVD)

Broker plane – can I see/launch a desktop? → DVU @ App Group
OS plane – can I sign in to Windows? → VM User/Admin Login @ VM/RG
✅ Both are required.

......................................
NTLM authentication
Legacy Windows auth method.
Seeing NtLmSsp in logs means Entra auth was not used or not available.
......................................
CloudAP authentication
Modern Entra ID authentication provider for Windows.
Seeing CloudAP in Event Log = Entra login is working correctly.
......................................
Event ID 4625
Windows logon failure.
With NtLmSsp + 0xc0000064, it means Windows could not resolve the Entra user.
......................................
Event ID 4624
Successful Windows logon.
Look for non‑NTLM authentication packages to confirm Entra login.
......................................
RBAC propagation delay
Azure role assignments are cached.
Logging out of AVD or reconnecting too fast can reuse old tokens.
......................................
Local administrator account
Local SAM account on the VM.
Works even when Entra login is broken; should be treated as break‑glass only.
......................................
AVD Web Client
https://client.wvd.microsoft.com
Preferred test path because it avoids legacy RDP configuration issues.
......................................
LSASS (Local Security Authority Subsystem Service)
Windows component that handles authentication.
Does not fully reload new credential providers until reboot.
......................................
Why reboot matters
The Entra login extension hooks into LSASS.
✅ Reboot forces credential provider reload and activates Entra login.
......................................
Common root cause (this case)
Correct Entra join + extension + RBAC, but Windows still uses NTLM because the VM hasn’t rebooted since enabling Entra login.
......................................
count meta‑argument
Terraform mechanism to create multiple instances of a resource using an index (count.index). Forces list-style addressing.
......................................
count.index
Zero‑based index automatically provided when count is used. Used for naming, indexing resources, and parallel construction.
......................................
Splat expression (resource.*.id)
Produces a list of attribute values from a counted resource. Often combined with [count.index] to select the matching instance.
......................................
for_each vs count
count creates indexed lists; for_each creates key‑addressed maps.
for_each is preferred for optional singletons and stable identities.
......................................
Optional resource pattern (Terraform)
Terraformfor_each = var.enable_feature ? { enabled = true } : {}Show more lines
Creates zero or one resource without index drift.
......................................
Boolean feature flag
Input variable (enable_bastion, enable_feature) used to conditionally create resources in Terraform.
......................................
Azure RBAC plane vs OS auth plane
Terraform provisions RBAC, but Windows authentication still depends on VM extensions + reboot + credential providers.
......................................
azurerm_virtual_machine_extension
Terraform resource that installs post‑deployment capabilities on Azure VMs (e.g. AAD login, DSC, agents).
......................................
AADLoginForWindows extension
Azure VM extension enabling Microsoft Entra ID authentication for Windows logon.
......................................
Extension side effects
Some extensions modify LSASS / credential providers and require a reboot to fully activate.
......................................
LSASS (Windows)
Local Security Authority process responsible for authentication. Does not reload auth providers until reboot.
......................................
Terraform does not imply reboot
Installing an extension in Terraform does not automatically reboot the VM unless explicitly configured.
......................................
type_handler_version
Version of the VM extension handler. Incorrect or unhealthy versions can silently break functionality.
......................................
auto_upgrade_minor_version = true
Allows Azure to patch extension handler bugs without Terraform changes.
......................................
Managed identity dependency
Some VM extensions (AAD login) depend on identity { type = "SystemAssigned" }.
......................................
Role assignment ≠ authentication
Azure RBAC grants permission, but authentication still fails if Windows cannot validate the identity.
......................................
azurerm_role_assignment scope matters
The same role behaves differently depending on scope (Application Group vs Resource Group).
......................................
Desktop Virtualization User (DVU)
AVD role used only for brokering access.
✅ Must be scoped to the Desktop Application Group.
......................................
Virtual Machine Administrator Login
Azure RBAC role that enables interactive Windows logon via Entra ID.
✅ Scoped at VM / RG / subscription.
......................................
Role definition lookup mistake
Using the wrong name in data azurerm_role_definition silently applies the wrong permissions.
......................................
Safer RBAC pattern
Use role_definition_name = "…"  directly instead of data lookups when possible.
......................................
RBAC propagation delay
Permission changes are not instant; cached tokens can cause confusing “still broken” behavior.
......................................
Terraform applies ≠ runtime state
Terraform ensures desired configuration, not immediate OS behavior.
......................................
AVD Web Client
Best test path for Entra login because it avoids legacy RDP credential behavior.
......................................
NTLM fallback
If Entra auth is unavailable, Windows silently falls back to NTLM — a key diagnostic signal.
......................................
Event Viewer as ground truth
Windows Security logs show which authentication method actually occurred, regardless of intent.
......................................
Fix sequencing matters
Correct order is:

Join VM to Entra
Install AADLoginForWindows
Assign RBAC roles
Reboot VM

......................................
Local admin = break‑glass
Local admin access working while Entra fails is expected and should not be used as proof of success.
