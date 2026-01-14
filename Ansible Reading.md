
https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html

Installing Ansible

Ansible is an agentless automation tool that you install on a single host (referred to as the control node). From the control node, Ansible can manage an entire fleet of machines and other devices (referred to as managed nodes) remotely with SSH, Powershell remoting, and numerous other transports, all from a simple command-line interface with no databases or daemons required.

Control node requirements
Managed node requirements
Node requirement summary
Selecting an Ansible package and version to install 
Installing and updating Ansible with pipx
    Installing Ansible
    Upgrading Ansible
    Installing Extra Python Dependencies
Installing and upgrading Ansible with Pip
    Locating Python
    Ensuring pip is available
    Installing Ansible
    Upgrading Ansible
Installing for development
    Installing devel from GitHub with pip
    Running the devel branch from a clone
Confirming your installation
Adding Ansible command shell completion
    Installing argcomplete
    Configuring argcomplete
        Global configuration
        Per command configuration
        Using argcomplete with zsh or tcsh

Control node requirement

For your control node (the machine that runs Ansible), you can use nearly any UNIX-like machine with Python installed. This includes Red Hat, Debian, Ubuntu, macOS, BSDs, and Windows under a Windows Subsystem for Linux (WSL) distribution. Windows without WSL is not natively supported as a control node; see Matt Davis' blog post for more information.

Managed node requirements

The managed node (the machine that Ansible is managing) does not require Ansible to be installed, but requires Python to run Ansible-generaged Python code. The managed node also needs a user account that can connect through SSH to the node with an interactive POSIX shell.

note
There can be exceptions in module requirements. For example, network modules do not require Python on the managed device. See documentation for modules you can use.

Node requirement summary

You can find details about control and managed node requirements, including Python versions, for each Ansible version in the ansible-core contreol node Python support and ansible-core support matrix sections.

Selecting an Ansible package and version to install

Ansible's community packages are distributed in two ways:
    ansible-core: a minimalist language and runtime package containing a set of built-in modules and plugins.
    ansible: a much larger "batteries included" package, which adds a community-curated selection of Ansible Collections for automating a variety of devices.

