ADMX & ADML in Intune — Study Notes
Quick-reference flashcards. Each entry is a standalone fact. Skim top to bottom, or jump to a section.

🖼️ The Big Picture (start here)
The light-switch analogy — A wall switch needs two things: the wiring behind the wall that does the real work, and the printed label ("Kitchen Lights") that tells a human what it does. ADMX = the wiring (policy logic + registry settings). ADML = the label (the readable text on screen). You always need both.

• • •
The old-world / new-world split — This is the single most important idea. On-premises Group Policy reads ADMX files. Modern cloud MDM (Intune) talks to CSPs. Almost everything else is a bridge between these two worlds.

📚 Foundations — The Files Themselves
ADMX file — Stands for Administrative Template XML. It's the "brains" of a policy: it defines what the policy is, what values it accepts, and exactly which registry keys/values get written. It contains no readable on-screen text.

• • •
ADML file — The language companion file (the "L" = language). It holds the friendly names, descriptions, and help text — for one specific language. Swap in a French ADML and the same ADMX shows French labels.

• • •
ADMX vs. ADML — ADMX = what the policy does (logic + registry mappings). ADML = what you read on screen (display strings). An ADMX with no matching ADML shows blank or cryptic labels in the editor.

• • •
"Language-neutral" — Describes ADMX files: they contain zero human words, only internal string IDs like $(string.EnableScreenSaver). The ADML maps that ID to real text. Separating logic from wording is why one ADMX can serve many languages.

• • •
ADM vs. ADMX — ADM is the old format (Windows XP era) that jammed logic and English text into one file. ADMX (introduced with Vista / Server 2008) split it into ADMX (logic) + ADML (language) — cleaner and translatable.

☁️ Bringing Them Into Intune
ADMX ingestion (a.k.a. ADMX consumption) — The process of importing custom / third-party ADMX + ADML files into Intune so their settings appear in the console and deploy like any other policy. Used for apps Microsoft didn't pre-load (Firefox, Adobe Reader, Zoom, in-house line-of-business apps).

• • •
Settings Catalog — Intune's modern, built-in library of settings (Windows, Edge, Office, Chrome, and more) — no downloads needed. It's the go-forward home for configuration. Your custom ADMX imports work right alongside it.

• • •
Import dependencies / order — Some templates depend on others. Import the dependency first. Example: upload mozilla.admx (and confirm status = Available) before firefox.admx, or the import fails with a "missing namespace" error. A very common parent dependency is Windows.admx.

• • •
Finding a template's dependencies — Open the ADMX in a text editor and look in the policyNamespaces node for a using prefix line — that reveals what it depends on.

• • •
Custom ADMX import limits (public preview) — Max 20 ADMX files; each ≤ 1 MB; one ADML per ADMX; only en-us ADML supported; combo-box setting type not supported.

• • •
Don't re-import built-in Windows ADMX — Templates in C:\Windows\PolicyDefinitions are already wired into Intune via CSPs. To configure them, use the Settings Catalog or a custom profile. Only import a built-in one when another template needs it as a required parent namespace.

• • •
The "(User)" tag — In the settings picker, a setting labeled (User) targets the signed-in user (HKEY_CURRENT_USER). No "(User)" tag = it targets the device (HKEY_LOCAL_MACHINE).

• • •
HKLM vs. HKCU — HKEY_LOCAL_MACHINE (HKLM) = the device, applies no matter who signs in. HKEY_CURRENT_USER (HKCU) = the individual user, applies when that user signs in.

🧩 The Neighborhood — Adjacent Concepts
CSP (Configuration Service Provider) — The built-in Windows interface that actually applies MDM settings on the device. If Intune is the manager sending orders from the cloud, the CSP is the worker inside Windows who carries them out. CSPs are to MDM what ADMX files are to Group Policy.

• • •
OMA-URI — Stands for Open Mobile Alliance – Uniform Resource Identifier. In plain English: a standardized address that points to one specific setting. "OMA" = the standards body; "URI" = address/path. Don't overthink the acronym — it just means "the address of a setting."

• • •
Reading an OMA-URI path — Read it left-to-right like a file path. Example: ./Device/Vendor/MSFT/Policy/Config/ControlPolicyConflict/MDMWinsOverGP

Piece	Meaning
./Device/	Apply to the device (./User/ = the user)
Vendor/MSFT/	Microsoft's section (MSFT = Microsoft)
Policy/Config/	"We're configuring a policy"
ControlPolicyConflict/	The category the setting lives in
MDMWinsOverGP	The actual setting being set
Reads as: "On the device → in Microsoft's policy area → configure → the ControlPolicyConflict category → the MDMWinsOverGP setting." It's just a structured address — like navigating folders to one file.

• • •
Group Policy analytics — An Intune migration tool. You export your on-prem GPOs as XML and import them; it analyzes them, shows which settings have cloud/MDM equivalents, flags deprecated or unsupported ones, and can migrate them into a Settings Catalog policy.

• • •
Default conflict winner — If the same setting is configured in both Group Policy and Intune, by default Group Policy wins. (Surprises people — the newer cloud tool does not win out of the box.) The default value is 0 = GPO wins.

• • •
MDMWinsOverGP (ControlPolicyConflict) — The Intune setting that flips the default so Intune/MDM wins the conflict. Set it to 1 (enabled). It's device-scoped and only covers standard Policy CSP settings — not Microsoft Defender or Windows Update settings, which must be moved separately.

• • •
Central Store — In an on-prem AD domain, the shared folder where ADMX/ADML files live so every domain controller uses one consistent copy. Path: \\<domain>\SYSVOL\<domain>\Policies\PolicyDefinitions.

• • •
Central Store vs. Intune Import ADMX — Same job (a shared home for templates), two different eras. 🏢 On-prem: the Central Store in SYSVOL. ☁️ Cloud: Intune's Import ADMX tab. Old world vs. new world.

• • •
"Administrative Templates" profile — deprecated — The old Intune Administrative Templates profile type is now read-only. The recommended replacement is the Settings Catalog (the unified settings platform). Custom ADMX import still works.

• • •
Why organizations prefer MDM/Intune over GPO — GPO needs line of sight to a domain controller to apply; MDM works over the internet, no domain controller required. MDM also gives better reporting and works for cloud-native / remote devices.

