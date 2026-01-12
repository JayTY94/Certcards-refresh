https://documentation.ubuntu.com/server/tutorial/managing-software/#managing-software

If you are new to Ubuntu, you may be wondering what to do after installation. After all, Ubuntu is endlessly customizable according to your needs. There are two types of software found in Ubuntu: Debian packages and snaps -- we will learn about both!

To help you get the most from your Ubuntu experience, this tutorial will walk you through managing the software on your Ubuntu machine. This tutorial can be completed using either Ubuntu Server or Ubuntu Desktop. 

To avoid making changes to your computer we will set up a virutal machine, which will provide us with a safe environment to run the commands in. Mutipass is great for quickly creating Ubuntu virtual machines, so we'll use that.

Prerequisites

Knowledge
    None! You don't even need to use an Ubuntu machine -- Muitpass will give us an Ubuntu environment to play with

Hardware
    The default Multipass VM will need 5 GB of disk space, and 1 GiB of memmory.

Software: Multipass
    On Ubuntu, you can install mutipass by running the following command in your terminal (you can open a terminal window by pressing [ctrl] + [alt] + [T] together):
    `sudo snap install multipass`
    Or you can install it directly from the Multipass page in the online snap store (make sure to select the "latest/stable" version from the dropdown menu next to the install button).
    Multipass can be installed on Windows, Mac and other Linux distributions with these instructions.
    
Create the virtual machine

Once you have installed and run Multipass, it is straightforward to launch a new VM. Let us launch a VM using the Ubuntu 24.04 LTS release (codename noble), and let's give our VM the name tutorial using the following command in our terminal window:

    multipass launch noble --name tutorial

Multipass will download the most recent daily image and create the VM for us. It may take a little time, depending on the speed of yoru internet connection. 

An Ubuntu image is a collection of files we need to install and run Ubuntu. We don't need to specify "server" or desktop" anywhere in our command, because the image is the same for both. The only difference between Ubuntu Server and Ubuntu Desktop is the subset of software packages we use form the Ubuntu Archive - we will see this later!

Now we can acces the Vm by running 

    multipass shell tutorial

We will get a "Welcome to Ubuntu" message. Notice that when we run this command, the terminal username changes to `ubuntu  ` and the hostname changes to tutorial:

    ubuntu@tutorial

This shows that we are inside the VM, and this is where we will run all our commands.

Updating the system with APT

The first thing we always want to do with a new system (whether a VM, container, bare metal, or cloud instance) is to make sure we have the latest versions of all the pre-installed software.

Debian package, commonly referred to as debs, are the standard software package format in Ubuntu. They can be identified by th .deb file extension.

Every Linux distribution has thier own preferred paackage manager for installing, updating and removing packages. In Ubuntu, the default package manager is Advanced Packaging Tool (or APT for short).

APT handles all of your system software (and other deb packages). It provides an interface to the Ubuntu Archive repository, so it can access both the database of all the packages available in Ubuntu and the means to handle the packages themselves.

There are two APT commands we need ot update our system: update and upgrade, which we will always run in that order.


...

Installing deb packages

For the examples for this section, we're going to use the popular web server package Apache2.

APT gives us a lot of details about what will be included in the installation, and it's always important tounderstand the implications of a command before we run it. We'll be taking a close look at the details APT gives us, so we need to be careful in this section.

When we run a command that asks us "Do you want to continue? [Y/n]", make sure to type [N] for "no" and then press [Enter] unless instructed otherwise - This will let us see the output of the commands without making changes that then need to be undone.

Installing deb packages using APT is done using the apt install command. We can install either a single package or a list of packages at once by including their names in a space separated list after the install command in this format:

    sudo apt install <package1> <package2> <package3>

About sudo
We've seen the sudo prefix in a couple of commands already, and you may be wondering what that's about. In Linux, system tasks (like installing softare) need elevated administrator permissions. These permissions are often called "root access", and a user with root access is called a root user.

However, it can be dangerous to operate your machine as a root user -- since root access gives you full system control the whole time, it allows you to change or delete important system files. It's very easy to accidentally break your system in root mode.

Instead, we use sudo (short for superuser do). This command is a safety feature that grants regular users temporary (per command) admin privileges to make system changes. It's still important for us to always understand what a command does before we run it, but using sudo means we purposefully limit any potential mistakes to a single command.

About dependencies

As we hinted earlier, packages often come with dependencies - other packages that your package needs so it can function. Sometimes, a package might depend on a specific version of another package. If a package has dependencies, then installing a package via apt will also install any dependencies, which ensures the software can function properly.

...

Types of dependencies

The relationship between a package and any other packages follows the Debian policy on binary dependencies, which we'll briefly look at here. The most common ones you might come across are: depends, reocommends, and suggests (although there are others!), so we'll take a look at these three.

    depends: Absolutely required, the package won't work wihtout it. If we try to remove a pakcage that's depended on by another, both will be removed!
    recommends: Strongly dependent, but not absolutely necessary (which means the package will work better with it, but can still function without it)
    Suggests: Not needed, but may enhance the usefulness of the package in some way.

We can see, using apt show, exactly which pakcages fall into each of these categories. Let's use Apache2 as our example again:

    apt show apache2

If we look only at the sections on dependencies, we can see that ssl-cert is a recommonded package:

    [...]
    Provides: httpd, httpd-cgi
    Pre-Depends: init-system-helpers (>= 1.54~)
    Depends: apache2-bin (= 2.4.58-1ubuntu8.4), apache2-data (= 2.4.58-1ubuntu8.4), apache2-utils (= 2.4.58-1ubuntu8.4), media-types, perl:any, procps
    Recommends: ssl-cert
    Suggests: apache2-doc, apache2-suexec-pristine | apache2-suexec-custom, www-browser, ufw
    [...]

In Ubuntu, the default configuration of apt install is set to install recommended packages alongside depends, so we when we ran the apt install apache2 command, ssl-cert was included in the proposed packages to be installed (even though it's only recommended, not strictly needed).

We can override this behavior by passing the --no-instaall-recommends flag to our command, like this:

    sudo apt install apache2 --no-intall-recommends

...

What if we remove a dependency?

We'll go into more detail about removing packages later, but for now, let's see what happens if we remove a required dependency. First, we shoul (finally!) install the apache2 package. Let's run the following command agian, but this tim when we are asked whether we want to continue, let's press [Y] and then [Enter] to confirm, and APT will install the package:

    sudo apt install apache2 -y

One of the required dependencies is the apache2-data package. Let's try removing it using pat remove:

    sudo apte remove apache2-data

Once again, apt won't proceed without confirmation, so we get the following output-let's taka  look before choosing anything:

    [...]

...

We might, in the future, uninstall Apache2 without uninstalling the redundant packages at the time. We might have found another use for ssl-cert, perhaps in a script that makes use of SSl certificates. So how can we keep the ssl-cert package, even though it's flagged for auto-removal?

We can solve this problem and un-flat the ssl-cert package for removal by manually installing it:

    sudo apt install ssl-cert

This sets ssl-cert to manually isntalled. We might well wonder "why didn't APT ask us to confirm anything this time?". In this case, it's because ssl-cert is already present on the system, so APT doesn't need to install anything new.

[...]

If the ssl-cert package is manually installed on our system, by us, then apt knows the package is wanted, and we can see that it has been removed from the autoremove list so our next autoremove will not uninstall it. Let's test this, just to make sure!

    sudo apt autoremove

...

Conffiles

Most of a package's configuration is handled through configuration files (often known as conffiles). Conffiles often contain things like file paths, logs, and debugging configuration, kernel parameters (which can be changed to optimize system performance), access control, and other configuration settings. The actual parameters available will vary from one package to another. 

Package conffiles are different from all other files delivered in a package. A package might have a number of conffiles (including none!). Conffiles are explicitly marked by the package maintainer during development to protect local configuration from being overwritten during upgrades so that your changes are saved. This will not be the case for any other type of files - changes you make to regular files in the package will be overwritten during an upgrade. 

How upgrades are handled

Since a conffile can be changed by us, we migth end up with conflicts when the package maintainer changes those same files. Therefore, it's important ot understand how such conflicts are handled.

We can show the four possible upgrade scenarios using the following table. What happens durin gna upgrade depends on whether the conffile on our system has been changed by us ("changed/not changed by user"), and whether the version's default content has been changed by the package maintainer ("changed/not changed by the maintainer"):

The conf file is... | Not changed by Maintainer | Changed by Maintainer
...changed by user | Keeps user's changes | Ask user
...not changed by user | No changes to make | Apply changes from update

So we can see that if we do make changes to a conffile, APT will never overwrite our changes without asking us first. 

Identifying conffiles

Out of the list of files in a package, how do we know which ones are the conffiles?

After all, they are not marked in any particular file extension, and although they are often found in the /etc/ directory, they don't have to be there. As we saw before, the only thing conffiles have in common is that the package maintianer decided to mark them as such.

...

Removing packages

Since we have just reinstalled the Apache2 package, we know it is in good shape. But what if we deicde we're done with it and just want to remove it? Then we can run:

    sudo apt remove apache2

Which gives us an output like this:
[...]

Let's type [Y] and proceed.

As before, we see that the dependencies will still be there even when apache2 has been removed. Let's check with dpkg...

    dpkg --listfiles apache2 

...and see what else mightbe left behind...

[...]

This looks suspiciously like the list of conffiles we saw earlier, right?

Also removing configuration

As it turns out, removing a package doesn't automatically remove the conffiles. But-this is intentional, for oru convenience.

By leaving the conffiles in palce, if we decide to reinstall apache2 again in the future, we don't need to spend time setting up all our configuration again.

Let's see the difference in installing apache2 after it has been installed (and removed) compared to the first time we installed it:

    sudo apt install apache2

Notice that it didn't ask us to confirm if we wanted to proceed this time. Why not? As we saw earlier, they "Y/n" confirmation is shown when there are dependencies, and we know that Apache2 has dependencies.

...Ah! But this time, we didn't run the autoremove when we uninstalled apache2, so the dependencies are still installed on our system. This means that when we ask apt to install apache2 now, there is nothing missing and we are getting exactly what we are askng for.

Since dependencies and conffiles are still there, wan use our former config immediately. It even retains the changes we made before, which we can verify by lookingat the checksum again:

    md5sum /etc/apache2/apache2.conf

...

APT warns us that the version of apache2 we want to install depends on earlier versions of the dependencies, but it helpfully tell su which dependency verisons we need to successfully install on the package we want.

[...]

So, all we need to do is first install the dependencies and then run the install command again. Remember that we can install multipla packages at one by separating them with spaces:

    sudo apt install apache2-bin=2.4.58-1ubuntu8 \
        apache2-data=2.4.58-1ubuntu8 \
        apache2-utils=2.4.58-1ubuntu8 \
        apache2=2.4.58-1ubuntu8

In this case we're also breaking the command over multiple lines using backslashes (\) to make it easier to read, but it will still be run as a single command.

APT will warn us that we are downgrading teh apckage, but let us press [Y] to confirm (when prompted), and it will go ahead and downgrade us anyway. Let's run the ofllowing command again:

    apt policy apache2

And we'll get confirmation that we're running on an older version:

[...]

Where do packages come from?

You may be wondering now "where exactly do all these packages come from?". We've spotted a few sources very briefly through this tutorial, but haven't paid direct attention to them yet. Let's take a little time now to define what we eman by all these different sourcess that APT can pull packages from.

The source behind APT is the Ubuntu Package Archive. This Archive splits into many layers, each with its own terminology. The different terminology is quite confusing at first, but we've seen a few of the terms already. So if we take a look, layer-by-layer, we'll see not jsut what all the terms mean, but how they all fit together.

...

Pockets

Every Ubuntu series (noble, jammy, etc) is split into pockets, which are related to the softare development/release lifecycle:

    -release contains the packages as they were at release time
    -proposed contains the package updates while they are being tested.
    Once an update is released, they come from either -security or -updates depending on whether they are security-related or not
    And -backports, which contain packages that were not available at release time.

This is why earlier, we saw that some updates came from noble-updates or noble-security. These refer to updates and security updates form the noble series (respectively). Pockets are usually appended to the end of the series, and it's quite common to see the hyphen (-) included when referring to pockets.

Remember--the original version of the apache2 package we saw came from noble. The -release pocket only includes the software that was part of the original LTS release, and so it makes the name of the Ubuntu series by default (i.e. The -release pocket is implied).

Components
Each pocket is split into four components, depending on whether the packages they contain are open source or closed source, and whether they are officially supported by Canonical or are maintained by the Ubuntu Community

...  | Open Source | Closed Source
Officially Supported | main | reestricted
Community supported | universe | multiverse

main contains the open-source packages thata re officially supported by Canonical. These packages are either installed on every Ubuntu machine or are very widely used for various types of systems and use-cases.

universe holdsd all other open-source packages in Ubuntu, which are typically maintained by the Debian and Ubuntu communities, but may also include additional security coverage from Canonical under Ubuntu Pro, which is available free for personal use on up to five machines.

restricted contains the packages that are officially supported by Canonical but are not available under a completely free license.

...
