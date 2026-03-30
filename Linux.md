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






19
Linux






20
Linux






21
Linux






22
Linux






23
Linux






24
Linux






25
Linux






26
Linux






27
Linux






28
Linux






29
Linux






30
Linux






31
Linux






32
Linux






33
Linux






34
Linux






35
Linux






36
Linux






37
Linux






38
Linux






39
Linux






40
Linux






