Azure Functions Fundamentals

Azure Functions Host – The runtime that actually executes your function code. It’s a .NET application that loads language workers (like Python) and manages triggers/bindings.

Azure Functions Core Tools – The CLI used for local development and testing; wraps the Functions host so you can run and debug locally.

Worker Runtime – The component responsible for running your language (Python, Node, etc.). For Python it uses the Python Worker, which communicates with the .NET host via gRPC.

local.settings.json – Configuration for local execution; emulates Azure app settings and connection strings.

⚙️ .NET Runtime & Assemblies

.NET Runtime (CoreCLR) – The actual execution engine for .NET apps (like the Functions host). Multiple versions can coexist (6, 8, 9, etc.).

.NET SDK vs Runtime – SDK includes compilers and tools; Runtime just runs apps.

Shared Frameworks – Versioned directories like Microsoft.NETCore.App and Microsoft.AspNetCore.App that provide assemblies shared by multiple apps.

Assembly Binding – The process by which .NET finds and loads DLLs. The error Could not load file or assembly 'Microsoft.Extensions.Logging, Version=8.0.0.0' means the host couldn’t locate that exact version of the library.

🧩 PATH and Environment Configuration

PATH – The OS environment variable listing directories where executables are searched. Determines which dotnet, func, or python runs.

DOTNET_ROOT – Overrides the path the .NET host uses to find its runtimes. If mis-set, .NET apps can’t find installed runtimes.

User vs Machine Environment Variables – On Windows, these are scoped differently; conflicts can cause commands to resolve inconsistently.

Cache Directories –

%LOCALAPPDATA%\AzureFunctionsTools → Extracted host binaries

%USERPROFILE%\.azure-functions-core-tools → Cached dependencies

%USERPROFILE%\.nuget → NuGet package cache

🧠 Python & Virtual Environments

venv (Virtual Environment) – Isolated Python environment with its own interpreter and site-packages; prevents dependency bleed.

Worker Version Compatibility – Azure Functions supports specific Python versions; check documentation for GA vs Preview versions.

🧰 Troubleshooting & Tools

Get-Command (PowerShell) – Finds which executable a command resolves to.

where.exe – Windows-native path resolver; shows all matches for a command.

NuGet – .NET’s package manager; clearing its cache (dotnet nuget locals all --clear) can fix stale dependencies.

MSI vs npm Core Tools – Two distribution methods for Core Tools; the MSI is self-contained and preferred on Windows (npm can cause PATH conflicts).

🔄 System Interactions

You run func start
→ Core Tools (CLI) starts the Functions Host (.NET app).

The host finds .NET runtimes via DOTNET_ROOT and PATH.

The host spawns a Python Worker that runs your code.

Logs and triggers are routed through Microsoft.Extensions.Logging.

If any of those assemblies can’t be found → the host throws a .NET assembly load error.