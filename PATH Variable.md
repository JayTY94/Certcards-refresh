PATH Variable


System PATH vs User PATH
System PATH: Applies to all users on the computer. Editing it requires administrative privileges.
User PATH: Applies only to your account. You can edit it without elevation. Both are combined when a shell session starts.



Session Scope
Changes made to environment variables that only last for the current shell session. For example, modifying $env:Path in PowerShell or using set in CMD affects only that window and disappears when you close it.


Permanent Scope
Changes that persist across sessions and reboots. These are applied by editing environment variables through the GUI or using commands like setx. Permanent changes are stored in the Windows registry.


$env:Path
A PowerShell variable that represents the current PATH for the active session. You can read or modify it directly, but changes here are temporary unless you use setx or the GUI.


setx
A command-line tool that writes environment variables permanently to the user or system scope. Unlike set, which is temporary, setx updates the registry so changes persist after reboot. However, it does not affect the current session immediately.


set
A CMD command that modifies environment variables temporarily for the current session. Once you close the CMD window, the changes are lost.



Delimiter
The character used to separate multiple entries in the PATH variable. On Windows, this is a semicolon (;). Each directory in PATH must be separated by this character.


Get-ChildItem Env:
A PowerShell command that lists all environment variables currently available in the session. It’s useful for inspecting variables beyond PATH.


-split ';'
A PowerShell operator that splits a string into an array based on a delimiter. For PATH, this is used to break the long PATH string into individual directory entries for easier inspection.


Test-Path
A PowerShell command that checks whether a given path exists on disk. It’s commonly used when auditing PATH entries to verify if directories are valid.


Duplicate Entries
When the same directory appears multiple times in PATH. This adds clutter and can slightly slow down command resolution.


PATH Length Limit
Historically, Windows had a limit of around 2048 characters for PATH. Modern versions allow much longer strings, but tools like setx may truncate if the PATH is extremely long.


Backup
Saving the current PATH before making changes to avoid accidental loss. Example in PowerShell:
    PowerShell
    $env:Path | Out-File "$env:USERPROFILE\path_backup.txt"Show more lines


Temporary PATH Change
A modification that applies only to the current session. Example in PowerShell:
    PowerShell
    $env:Path = "C:\Tools;" + $env:PathShow more lines


Permanent PATH Change
A modification that persists across sessions and reboots. Example in PowerShell:
    PowerShell
    setx PATH "$env:Path;C:\Tools"Show more lines


Order Matters
Windows searches PATH entries from left to right. Placing frequently used directories earlier can speed up command resolution.


Validation
The process of checking whether each PATH entry points to an existing directory. Example in PowerShell:
    PowerShell
    $env:Path -split ';' | Where-Object { Test-Path $_ }Show more lines



Environment Scope
Defines where and how environment variables apply:

Process Scope: Variables exist only for the current process.
User Scope: Variables apply to the current user account.
System Scope: Variables apply to all users on the machine.



Registry Storage
Permanent environment variables are stored in the Windows Registry:

System Variables: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
User Variables: HKEY_CURRENT_USER\Environment



Profile Scripts
PowerShell uses profile scripts to customize sessions:
Location: $PROFILE
Purpose: Add commands or modify $env:Path automatically when PowerShell starts.




Execution Policy
Controls what scripts can run in PowerShell:
Common values: Restricted, RemoteSigned, Unrestricted.
Check with:
PowerShellGet-ExecutionPolicyShow more lines



PATH Resolution Order
When you type a command:
Current directory
PATH entries (left to right)
Windows system directories (e.g., System32)






Command Precedence
If two executables share the same name:
The one in the first matching PATH directory wins.
Use where.exe <command> or Get-Command <command> to check which one runs.






Environment Variable Expansion
Variables can reference other variables:
Example:
BATset PATH=%PATH%;%JAVA_HOME%\binShow more lines

In PowerShell:
PowerShell$env:Path += ";$env:JAVA_HOME\bin"Show more lines








PATH Pollution
Occurs when installers add unnecessary or duplicate entries to PATH, making it long and inefficient.






PATH Injection Risk
If a malicious directory is added early in PATH, it can override trusted executables.
Best practice: Keep system directories first and avoid adding writable folders.






Session vs Persistent Variables

Session: $env:Path changes vanish after closing PowerShell.
Persistent: Use setx or GUI to make changes permanent.


PowerShell Profiles vs CMD Autoexec

PowerShell uses $PROFILE scripts for customization.
CMD uses autoexec.bat historically (rare today).







PATH Length and Performance
Very long PATH can slow down command resolution.
Tip: Remove unused entries and keep essential ones first.






where.exe and Get-Command

where.exe <command> (CMD) → shows all matching executables in PATH.
Get-Command <command> (PowerShell) → shows the resolved command and its path.






Environment Variable Precedence
Order of evaluation:

Process variables override User variables.
User variables override System variables.






%PATH% vs $env:Path

%PATH% → CMD syntax.
$env:Path → PowerShell syntax.