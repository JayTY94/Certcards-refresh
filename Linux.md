1
Linux
/bin
/bin is the directory that contains binaries, that is, some of the applications and programs you can run. There are more bin directories in other parts of the file system tree, but we’ll be talking about those in a minute.







2
Linux
/boot
The /boot directory contains files required for starting your system. Do I have to say this? Okay, I’ll say it: DO NOT TOUCH!. If you mess up one of the files in here, you may not be able to run your Linux and it is a pain to repair. 





3
Linux
/dev
/dev contains device files. Many of these are generated at boot time or even on the fly. For example, if you plug in a new webcam or a USB pendrive into your machine, a new device entry will automagically pop up here.







4
Linux
/etc
Nowadays, it would be more appropriate to say that etc stands for “Everything to configure,” as it contains most, if not all system-wide configuration files. For example, the files that contain the name of your system, the users and their passwords, the names of machines on your network and when and where the partitions on your hard disks should be mounted are all in here





5
Linux
/lib
/lib is where libraries live. Libraries are files containing code that your applications can use. They contain snippets of code that applications use to draw windows on your desktop, control peripherals, or send files to your hard disk.







6
Linux
/lib
There are more lib directories scattered around the file system, but this one, the one hanging directly off of / is special in that, among other things, it contains the all-important kernel modules. The kernel modules are drivers that make things like your video card, sound card, WiFi, printer, and so on, work.







7
Linux
 /opt
The /opt directory is often where software you compile (that is, you build yourself from source code and do not install from your distribution repositories) sometimes lands. Applications will end up in the /opt/bin directory and libraries in the /opt/lib directory.







8
Linux
/proc
/proc, like /dev is a virtual directory. It contains information about your computer, such as information about your CPU and the kernel your Linux system is running. As with /dev, the files and directories are generated when your computer starts, or on the fly, as your system is running and things change.







9
Linux
/root
/root is the home directory of the superuser (also known as the “Administrator”) of the system. It is separate from the rest of the users’ home directories BECAUSE YOU ARE NOT MEANT TO TOUCH IT. Keep your own stuff in your own directories, people.







10
Linux
/run
/run is another new directory. System processes use it to store temporary data for their own nefarious reasons. This is another one of those DO NOT TOUCH folders.







11
Linux
/sbin
/sbin is similar to /bin, but it contains applications that only the superuser (hence the initial s) will need. You can use these applications with the sudo command that temporarily concedes you superuser powers on many distributions. /sbin typically contains tools that can install stuff, delete stuff and format stuff.







12
Linux
/srv
The /srv directory contains data for servers. If you are running a web server from your Linux box, your HTML files for your sites would go into /srv/http (or /srv/www). If you were running an FTP server, your files would go into /srv/ftp.







13
Linux
/sys
/sys is another virtual directory like /proc and /dev and also contains information from devices connected to your computer.

In some cases you can also manipulate those devices. I can, for example, change the brightness of the screen of my laptop by modifying the value stored in the /sys/devices/pci0000:00/0000:00:02.0/drm/card1/card1-eDP-1/intel_backlight/brightness file (on your machine you will probably have a different file). 





14
Linux
/var contains things like logs in the /var/log subdirectories. Logs are files that register events that happen on the system. If something fails in the kernel, it will be logged in a file in /var/log; if someone tries to break into your computer from outside, your firewall will also log the attempt here. It also contains spools for tasks.





15
Linux
You can list running processes using the ps command (ps means process status). The ps command displays your currently running processes in real-time.
This will display the process for the current shell with four columns:

    PID returns the unique process ID

    TTY returns the terminal type you're logged into

    TIME returns the total amount of CPU usage

    CMD returns the name of the command that launched the process.








16
Linux
This ps works by reading the virtual files in /proc.  This ps does
not need to be setuid kmem or have any privileges to run.  Do not
give this ps any special permissions.

CPU usage is currently expressed as the percentage of time spent
running during the entire lifetime of a process.  This is not
ideal, and it does not conform to the standards that ps otherwise
conforms to.  CPU usage is unlikely to add up to exactly 100%.





17
Linux
If you’d like a quick way of checking both the OS and kernel, enter the following command into your Linux terminal:

hostnamectl

When entered, this should output a list of information from the Systemd logs associated with your system’s hostname. Included in this information, you should find a line marked Operating System which contains the name of your Linux distribution, and a line below it marked Kernel, containing information on your Linux Kernel’s version number





18
Linux
ss 
    used to dump socket statistics. It allows showing information similar to netstat.  It can display more TCP and state information than other tools.
    When no option is used ss displays a list of open non-listening sockets (e.g. TCP/UNIX/UDP) that have established connection.




19
Linux
ss -t -a
        Display all TCP sockets.

ss -t -a -Z
        Display all TCP sockets with process SELinux security
        contexts.





20
Linux
ss -u -a
        Display all UDP sockets.

ss -o state established '( dport = :ssh or sport = :ssh )'
        Display all established ssh connections.





21
Linux
Command to check ssh in the journalctl log

    sudo journalctl -u ssh --since "2 hours ago"





22
Linux
With journalctl, if two different fields are matched, only entries matching both expressions at the same time are shown:

    journalctl _SYSTEMD_UNIT=avahi-daemon.service _PID=28097






23
Linux
With journalctl, if two matches refer to the same field, all entries matching
either expression are shown:

    journalctl _SYSTEMD_UNIT=avahi-daemon.service _SYSTEMD_UNIT=dbus.service






24
Linux
The cloud-init main log (/var/log/cloud-init.log)
This file is the golden source of truth: a detailed, chronological record of every stage and module. When you need to know exactly what happened, look here. Searching this file for ERROR or WARNING will often lead you directly to the problem.

less /var/log/cloud-init.log





25
Linux
The cloud-init output log (/var/log/cloud-init-output.log)
This log captures the full stdout and stderr of all scripts executed by cloud-init (e.g., from runcmd). If a module ran but your script within it failed, the error message will be in this file.

less /var/log/cloud-init-output.log





26
Linux
Added to my cloud-init.yaml.tpl file to add another user to practice file ownership
users:
  - default
  - name: labuser
    gecos: Local-only lab user (no SSH)
    shell: /usr/sbin/nologin
    lock_passwd: true
    create_home: true
    home: /home/labuser
    ssh_authorized_keys: []





27
Linux
Your Linux system keeps a detailed record of its activity, and most of it lives in one place: /var/log. It’s the go-to directory when something breaks, slows down, or behaves oddly. For anyone working in DevOps—or even just getting started with Linux—knowing your way around system logs isn’t optional. It’s part of the job.







28
Linux
/var/log/syslog or /var/log/messages	
    General system messages	
    Boot information, device changes, system services
/var/log/auth.log or /var/log/secure	
    Authentication events	
    Login attempts, sudo commands, SSH access





29
Linux
/var/log/kern.log	
    Kernel messages	
    Hardware issues, driver problems
/var/log/dmesg	
    Boot messages	
    Device initializations, hardware detection





30
Linux
# View entire file
cat /var/log/syslog

# View last 10 lines
tail /var/log/syslog





31
Linux
# Follow log in real-time (great for troubleshooting)
tail -f /var/log/syslog

# Search for specific terms
grep "error" /var/log/syslog






32
Linux
typical syslog entry:
Jan 15 14:23:01 myserver sshd[12345]: Failed password for invalid user admin from 192.168.1.5 port 43210 ssh2

Breaking this down:
    Jan 15 14:23:01 - Timestamp showing when the event occurred
    myserver - The hostname of the machine
    sshd[12345] - The program name and process ID
    Failed password for invalid user admin... - The actual message describing what happened






33
Linux
journalctl option
--rotate
    Asks the journal daemon to rotate journal files. This call
    does not return until the rotation operation is complete.
    Journal file rotation has the effect that all currently active
    journal files are marked as archived and renamed, so that they
    are never written to in future. New (empty) journal files are
    then created in their place. This operation may be combined
    with --vacuum-size=, --vacuum-time= and --vacuum-file= into a
    single command, see above.





34
Linux
journalctl options
--vacuum-size=, --vacuum-time=, --vacuum-files=
    --vacuum-size= removes the oldest archived journal files until
    the disk space they use falls below the specified size.
    Accepts the usual "K", "M", "G" and "T" suffixes (to the base
    of 1024).

    --vacuum-time= removes archived journal files older than the
    specified timespan. Accepts the usual "s" (default), "m", "h",
    "days", "weeks", "months", and "years" suffixes, see
    systemd.time(7) for details.

    --vacuum-files= leaves only the specified number of separate
    journal files.






35
Linux
Start apache2 service and then check if it's running

azureuser@exercism-vm-20260403:/mnt/exercism$ sudo systemctl start apache2
azureuser@exercism-vm-20260403:/mnt/exercism$ sudo systemctl is-active apache2
active





36
Linux
Stop apache2 service and then check if it's running
azureuser@exercism-vm-20260403:/mnt/exercism$ sudo systemctl stop apache2
azureuser@exercism-vm-20260403:/mnt/exercism$ sudo systemctl is-active apache2
inactive





37
Linux
# Enable a service to start at boot (creates a symlink in the target directory)
sudo systemctl enable nginx

# Start it now AND enable it (common pattern)
sudo systemctl enable --now nginx






38
Linux
# Disable a service (removes the symlink, does not stop the running service)
sudo systemctl disable nginx

# Disable and stop in one command
sudo systemctl disable --now nginx






39
Linux






40
Linux






