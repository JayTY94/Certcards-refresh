Ansible.md

.......
Ansible is an agentless automation tool that you install on a single host (referred to as the control node).

From the control node, Ansible can manage an entire fleet of machines and other devices (referred to as managed nodes) remotely with SSH, Powershell remoting, and numerous other transports



.......
For your control node (the machine that runs Ansible), you can use nearly any UNIX-like machine with Python installed. This includes Red Hat, Debian, Ubuntu, macOS, BSDs, and Windows under a Windows Subsystem for Linux (WSL) distribution. Windows without WSL is not natively supported as a control node



.......
The managed node (the machine that Ansible is managing) does not require Ansible to be installed, but requires Python to run Ansible-generated Python code. The managed node also needs a user account that can connect through SSH to the node with an interactive POSIX shell.





.......
Instead of installing Ansible content manually, you can simply build an execution environment container image or use one of the available community images as your control node. See Getting started with Execution Environments for details.





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




.......




.......




.......




.......




.......




.......






