Linux

(Each block represents one notecard)



=============

Process
A running instance of a program with its own memory and resources. Each process is assigned a unique Process ID (PID). Processes can be foreground or background tasks and can spawn child processes.

=============

PID (Process ID)
A numeric identifier assigned to every running process. Useful for monitoring, debugging, and sending signals such as termination, reload, or stop via commands like kill or ps.


=============

systemd
The default system and service manager for many Linux distributions. It controls system startup, manages services, and provides tools like systemctl, journalctl, and unit files for configuration.

=============

Service
A long-running system process managed by systemd. Services can be started, stopped, enabled at boot, or viewed for logs using commands like systemctl start, systemctl enable, and journalctl.

=============

Root Directory (/)
The top-level directory in the Linux filesystem hierarchy. All files and subdirectories branch from /, including system, user, and device paths.

=============

Home Directory
The personal directory assigned to each user, typically under /home/username. It stores personal files, configuration settings, and user-specific application data.

=============

Permissions
Rules governing who can read, write, or execute a file. Divided into three groups: owner, group, and others. Displayed in formats like rwxr-x--- and modified with chmod.

=============

chmod
A command used to change file permissions. Supports both symbolic format (e.g., chmod g+w) and numeric format (e.g., chmod 755). Controls read, write, and execute access.

=============

chown
A command that changes file or directory ownership. It can modify the owner, group, or both (e.g., chown user:group file). Only the root user can change ownership.





=============

ps (Process Status)
A command that lists running processes. Often used with options like ps aux to view all processes across users or to locate PIDs for analysis or control.

=============

top
A real-time system monitor showing CPU usage, memory consumption, and process activity. Helpful for observing system behavior and identifying resource-heavy processes.

=============

journalctl
The command used to read logs managed by systemd. It allows filtering by service, time range, boot sessions, and priority levels.

=============

systemctl
The primary tool for managing systemd services. It starts, stops, enables, disables, and queries the status of services such as web servers or SSH.

=============

ls -l
A long-format directory listing that displays permissions, owners, file size, and timestamps. Essential for diagnosing permission or ownership problems.


=============

chmod 755 / chmod 644
Common permission settings. 755 typically applies to directories and executables, while 644 applies to files. These patterns control read, write, and execute privileges.

=============

chgrp
A command that changes the group ownership of a file or directory. Useful when coordinating access among multiple users or scripts.


=============

awk
A text-processing tool useful for extracting columns, performing simple calculations, or transforming structured text from logs or commands.

=============

sed
A stream editor used to modify text as it passes through a pipeline. It can replace words, delete lines, or rewrite patterns without opening an editor.



=============

redirect (>, >>)
Operators that send command output into files. > overwrites files, while >> appends to them. These are commonly used for capturing logs during small projects.

=============

cron job
A scheduled task defined in a crontab entry. Useful for running scripts at regular intervals, such as hourly cleanup or diagnostic logs.


=============

uptime
A command that displays how long the system has been running along with the load average. Useful during system-health exploration.

=============

df -h
A command that reports disk space usage in a human-friendly format. Helpful for diagnosing storage constraints and exploring filesystem layouts.

=============

du -sh
Displays the disk usage of a directory or file. Often used to identify large folders when cleaning up a system.

=============

nano / vim
Text editors available in the terminal. Nano is beginner-friendly, while Vim offers powerful text manipulation features for configuration and scripting tasks.


=============

User Data / Cloud-Init
A script or configuration passed to a newly created virtual machine that runs on first boot. Commonly used to install packages, create users, configure security rules, or start services automatically.



=============

SSH Config File
A local file (~/.ssh/config) that stores predefined connection settings, allowing quick access to remote servers with short, human-friendly commands.

=============

Cloud-init Log
A log file on a cloud instance (typically /var/log/cloud-init.log) that records the results of the initialization process. Useful for debugging failed provisioning steps.

=============

journalctl -u <service>
A command that displays logs for a specific systemd service. Helpful when diagnosing boot scripts, cloud-init actions, or service failures.

=============

systemctl enable
A command that configures a service to start automatically at boot. Often used after installing custom agents or scripts in a new server.

=============

htop
An interactive process viewer that offers a more detailed, user-friendly alternative to top. Helps visualize CPU, memory, and per-process activity.


=============

/proc Filesystem
A virtual pseudo-filesystem that exposes kernel and process information in real time. Contains details on CPU, memory, processes, and more.

=============

TTL Tag (Time-To-Live Tag)
A metadata tag on cloud resources used by automation to identify and automatically delete outdated or ephemeral infrastructure. Helps control cost and resource hygiene.

=============




