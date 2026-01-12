Ubuntu.md

There are two types of software found in Ubuntu: Debian packages and snaps. Snaps are self-contained applications running in a sandbox with mediated access to the host system.

.......
Snap is a software packaging and deployment system developed by Canonical for operating systems that use the Linux kernel and the systemd init system.


.......
Once you have installed and run Multipass, it is straightforward to launch a new VM. Let us launch a VM using the Ubuntu 24.04 LTS release (codename noble), and let’s give our VM the name tutorial using the following command in our terminal window:

    multipass launch noble --name tutorial


.......
The first thing we always want to do with a new system (whether a VM, container, bare metal, or cloud instance) is to make sure we have the latest versions of all the pre-installed software.

Debian packages, commonly referred to as debs, are the standard software package format in Ubuntu. They can be identified by the .deb file extension.







.......
Every Linux distribution has their own preferred package manager for installing, updating and removing packages. In Ubuntu, the default package manager is Advanced Packaging Tool (or APT, for short).




.......
In many places, you will see reference to apt-get and apt-cache instead of apt. Historically, the database part of APT was accessed using apt-cache (e.g. apt-cache show ipcalc), and the packages part of APT used apt-get (e.g. apt-get install ipcalc).

APT has recently been streamlined, so although it uses apt-get and apt-cache “behind the scenes” (and these commands do still work), we don’t need to worry about remembering which command to use – we can use the more convenient apt directly.




.......
Installing deb packages using APT is done using the apt install command. We can install either a single package or a list of packages at once by including their names in a space separated list after the install command in this format:

    sudo apt install <package1> <package2> <package3>



.......
Debian policy on binary dependencies
    depends: Absolutely required, the package won’t work without it. If we try to remove a package that is depended on by another, both will be removed!
    recommends
    suggests

.......
Debian policy on binary dependencies
    depends
    recommends: Strongly dependent, but not absolutely necessary (which means the package will work better with it, but can still function without it)
    suggests


.......
Debian policy on binary dependencies, 
    depends
    recommends
    suggests: Not needed, but may enhance the usefulness of the package in some way.







.......
In Ubuntu, the default configuration of apt install is set to install recommended packages alongside depends, so when we ran the apt install apache2 command, ssl-cert was included in the proposed packages to be installed. We can override this behavior by passing the --no-install-recommends flag to our command, like this:

    sudo apt install apache2 --no-install-recommends




.......
Removing dependencies can, at worst, cause a system to become unusable – you should always be careful when doing so. If you remove a dependency that is part of a chain, the removals will cascade up the chain as each dependency and the package that depends on it are removed. You can end up removing more than you originally anticipated!






.......
We might, in the future, uninstall Apache2 without uninstalling the redundant packages at the time. We might have found another use for ssl-cert, perhaps in a script that makes use of SSL certificates. We can solve this problem, and un-flag the ssl-cert package for removal, by manually installing it:

    sudo apt install ssl-cert





.......
If we find a file but we’re not sure what package it comes from, dpkg can help us there too! Let’s use the example of one of the files from the previous output: /usr/share/ssl-cert/ssleay.cnf and do a search for it using dpkg:

dpkg --search /usr/share/ssl-cert/ssleay.cnf




.......
Most of a package’s configuration is handled through configuration files (often known as conffiles). Conffiles often contain things like file paths, logs and debugging configuration, kernel parameters (which can be changed to optimize system performance), access control, and other configuration settings. 




.......
Package conffiles are different from all other files delivered in a package. A package may have any number of conffiles (including none!). Conffiles are explicitly marked by the package maintainer during development to protect local configuration from being overwritten during upgrades so that your changes are saved. 




.......
To remove an application with apt, including all conffiles, we add the --purge option to the apt remove command. Remember to use `sudo apt autoremove` to get rid of them.

sudo apt remove --purge apache2




.......
For every package, we can see what versions of it exist in the database:

    apt policy apache2

This will return a summary of all the versions that exist on our particular Ubuntu release, ordered by “most recent” first.




.......
We can install specific older versions if we want to, for example, to satisfy dependency requirements of another package. We can do that by specifying the package name and version:

    sudo apt install <package=version>
or 
    sudo apt install apache2=2.4.58-1ubuntu8





.......
The series is a set of packages that are released with a specific version of Ubuntu – they’re usually referred to by their codename (e.g., mantic, noble and oracular in our diagram). Each version of Ubuntu may have multiple releases (for example, an LTS will have an initial release when it launches (e.g. 24.04 LTS), and then “subsequent point releases” (e.g. 24.04.1 LTS) – these are all part of the same series (noble).




.......
Every Ubuntu series (noble, jammy, etc) is split into pockets, which are related to the software development/release lifecycle:

    -release contains the packages as they are at release time.

    -proposed contains package updates while they are being tested.

    Once an update is released, they come from either -security or -updates depending on whether they are a security-related update or not.

    And -backports, which contains packages that were not available at release time.






.......
Each pocket is split into four components, depending on whether the packages they contain are open source or closed source, and whether they are officially supported by Canonical or are maintained by the Ubuntu Community

...  | Open Source | Closed Source
Officially Supported | main | reestricted
Community supported | universe | multiverse




.......
We can install .deb files that aren’t in the APT repository using dpkg – all we need is to download the .deb file, and we can run a command like this to install it:

sudo dpkg -i <file-name.deb>





.......
Snaps are a newer, self-contained software format that were developed to be a more portable and easy-to-use alternative to debs. They come with all their dependencies pre-bundled so that there is no need for a package management tool to track dependencies, and they run inside sandboxed environments that limit their interactions with the rest of the system.






.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......





.......