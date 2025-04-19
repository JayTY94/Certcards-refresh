Availability Set
A logical grouping that ensures VMs are distributed across different physical racks within a datacenter, improving resiliency by minimizing single points of hardware failure.



Availability Zone
A physically isolated datacenter location within an Azure region, designed for high availability by spreading resources across separate zones with independent power, cooling, and 


networking.
Custom Script Extension
A VM extension that allows you to run PowerShell or shell scripts post-deployment, useful for automation, configuration, or app installation after the VM is provisioned.



Cloud-Init
A Linux-native tool that enables automatic VM customization on boot using YAML config files, typically used to install packages, configure networking, or run scripts.



Startup Script / Bootstrap Script
A script (Bash or PowerShell) that sets up tools, environment variables, or dependencies on a VM right after it is created or logged into for the first time.



Run Command
A feature in the Azure Portal that lets you remotely execute shell or PowerShell commands directly on a VM without needing SSH or RDP access, often used for debugging or recovery.



Managed Identity
An Azure identity service that allows VMs and other resources to securely authenticate to Azure services without storing credentials in code or config files.



Azure Policy
A governance tool that defines and enforces organizational rules on Azure resources, such as restricting VM sizes, locations, or blocking public IP assignments.



Inbound NAT Rule
A networking rule used with load balancers to map a public-facing port to a specific VM's internal port, enabling external access to individual VMs in backend pools.



Persistent vs Ephemeral
A comparison between VMs that retain data and configurations across reboots (persistent) vs temporary VMs used for disposable environments like Codespaces (ephemeral).



Remote Development
A workflow where the code is executed and debugged on a remote machine (e.g., cloud VM), while edited locally through a tool like VS Code, keeping compute and environment remote.



Remote - SSH (VS Code)
A VS Code extension that allows seamless editing, terminal access, and debugging on a remote machine via SSH, making a remote system feel local.



SSH Config File
A local file (`~/.ssh/config`) used to define aliases and settings for SSH connections, making it easier to reuse hostnames, ports, and identities.



.ssh/known_hosts
A file used by SSH to store server fingerprints, preventing man-in-the-middle attacks by validating that the server hasn’t changed unexpectedly.



Port Forwarding
An SSH feature that lets you tunnel remote ports (e.g., a web app running on port 5000 on a VM) to your local machine for testing and access.



X11 Forwarding
An SSH technique that lets GUI applications run on a remote Linux machine but display on your local computer; requires an X server locally.



VS Code Workspace (.code-workspace)
A VS Code config file that defines multi-root folders, editor settings, and extension recommendations for a consistent project layout and experience.



Debugger Config (launch.json)
A JSON config file in VS Code that specifies how to run and debug an app, including which script to execute, arguments, environment variables, and breakpoints.



Dotfiles
A collection of personal configuration files (e.g., `.bashrc`, `.gitconfig`, `.vimrc`) that define your shell, editor, and tool preferences across machines.



Dev Containers
A container-based dev environment defined in `.devcontainer.json`, allowing full isolation and consistent tooling across developers, either locally or in Codespaces.



Systemd Service
A background service on Linux managed by `systemctl`, which can run your app as a daemon, restart on failure, and start automatically on boot.



.env File
A flat file storing environment variables (like `DEBUG=true`, `API_KEY=xyz`) for local development and testing, typically excluded from version control.



Language Runtime
The software layer that interprets and executes code written in a particular language (e.g., Python, Node.js, .NET Core), and must be installed in the dev environment.



Build Tool
A program used to automate the compilation, packaging, and dependency resolution of a software project (e.g., `make`, `npm`, `dotnet build`, `gradle`).



Package Manager
A tool for installing, updating, and managing external libraries your app depends on (e.g., `pip`, `npm`, `nuget`, `brew`).



Dependency Management
The process of tracking and resolving software dependencies, ensuring your project uses compatible versions of external libraries.



Linter
A code analysis tool that detects errors, bugs, and style violations before runtime; common examples include ESLint (JavaScript) and Pylint (Python).



Formatter
A tool that automatically reformats source code to follow a defined style guide, improving consistency and readability (e.g., Prettier, Black).



Pre-Commit Hook
A Git hook that runs scripts (e.g., formatters, tests) before committing code, helping catch issues early in the development workflow.



Makefile / Task Runner
A scriptable command list (via `make` or tools like `npm run`) used to automate tasks such as builds, tests, or environment setup in a dev workflow.



TDD (Test-Driven Dev)
A methodology where you first write failing tests, then write the minimum code to pass them, promoting cleaner, more reliable software.



Test Pyramid
A testing strategy that favors many fast unit tests, fewer integration tests, and minimal end-to-end tests to maintain speed and reliability.



REPL
Short for “Read-Eval-Print Loop,” an interactive shell that allows developers to run and evaluate code statements live (e.g., Python shell, Node.js REPL).



Debug Adapter Protocol
A VS Code protocol that enables consistent debugging experiences across languages by abstracting debugger backends from the editor interface.



Language Server Protocol (LSP)
A communication protocol between an editor and a language-specific server that provides smart features like autocomplete, go-to-definition, and linting.



12-Factor App
A set of best practices for building cloud-native apps, including stateless processes, config via environment variables, and dev/prod parity.



Telemetry / Observability
Practices and tooling that provide insight into app behavior through logs, metrics, and traces, often used for debugging, alerting, and performance tuning.



