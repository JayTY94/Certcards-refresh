Docker Container ID

A unique SHA256 identifier assigned to each container instance, used to reference, stop, inspect, or execute commands within a specific container.

Docker Build Context

The folder and contents sent to Docker during docker build. Dockerfile must be inside this context, and relative paths are resolved against it.

CMD in Dockerfile

Specifies the default command to run when the container starts. Only one CMD is allowed; using shell form allows chaining multiple commands, exec form runs a single binary directly.

Docker Port Mapping

-p host_port:container_port exposes a container port to the host, allowing services like XRDP to be reachable from Windows via localhost.

Docker exec

Runs commands inside a running container, useful for troubleshooting, updating passwords, or starting/stopping services without rebuilding the image.

XRDP Daemon

The main process handling RDP connections in a container. Must be running alongside xrdp-sesman for Windows Remote Desktop to connect successfully.

XRDP Session Manager (xrdp-sesman)

Handles user sessions for XRDP. Runs in the foreground to keep the container alive, coordinating session authentication and desktop environment startup.

Noninteractive apt

Setting DEBIAN_FRONTEND=noninteractive prevents apt from prompting during package installs, avoiding build hangs when installing desktop environments like XFCE inside Docker.

RDP Connection Troubleshooting

Verify container is running, ports are mapped correctly, XRDP daemon is active, and Windows firewall permits connections. Test connectivity via Test-NetConnection localhost -Port 3389.

WSL2 Networking

Docker inside WSL2 exposes container ports to Windows via localhost. Containers listen on 0.0.0.0, but RDP may require explicit 127.0.0.1:3389 for Windows clients.

Container Daemons Startup

Multiple services inside a container require either chaining in a shell-form CMD or a process manager. Only one CMD is allowed per Dockerfile; shell form allows starting XRDP + sesman simultaneously.

I can also add a few more “best practice” notes for running GUI Linux containers on WSL2 to make this a full troubleshooting cheat sheet, if you want. Do you want me to do that?

You said:
do so please
ChatGPT said:

Here’s an expanded set of notes, in the same ~30-word style as your examples, covering best practices and troubleshooting for running GUI Linux containers on WSL2/Windows:

Docker GUI Containers on WSL2

Run Linux GUI apps in Docker on Windows by exposing necessary ports (e.g., 3389 for RDP) and using a lightweight desktop environment. WSL2 enables near-native performance with Docker Desktop.

XFCE in Docker

A minimal desktop environment suitable for RDP in containers. Install with DEBIAN_FRONTEND=noninteractive to prevent interactive prompts during builds. Avoid heavier desktops to reduce build time and resource usage.

Starting Multiple Daemons

Containers only allow one CMD. Use shell-form CMD (bash -c "cmd1 && cmd2") to start multiple services like xrdp and xrdp-sesman simultaneously.

Avoiding Interactive Prompts in Docker Builds

Set ENV DEBIAN_FRONTEND=noninteractive and chain commands to prevent apt package installs from pausing for keyboard layout, locale, or timezone prompts during automated builds.

Exposing Ports for RDP

Use -p host_port:3389 in docker run to map the container’s XRDP port to Windows. Access with 127.0.0.1:3389 to ensure Windows RDP connects correctly to the container.

Verifying XRDP Status

Check with ps aux | grep xrdp. Both xrdp and xrdp-sesman must be running. Start manually with service xrdp start if needed.

RDP Troubleshooting Steps

Confirm container is running (docker ps)

Confirm port mapping is correct

Confirm XRDP daemon is active

Test connectivity with Test-NetConnection localhost -Port 3389

Check Windows firewall or WSL2 networking

Updating Container Passwords

Use docker exec -it <container> passwd root to set a root password for XRDP login. Avoid empty passwords to prevent RDP client rejection.

WSL2 Networking Notes

Docker containers in WSL2 expose ports via 0.0.0.0. Some Windows clients require explicit 127.0.0.1:port connections. Networking issues often appear as “cannot connect” errors in RDP.

Container Persistence

Containers are ephemeral; changes inside are lost unless committed or volumes are used. Keep configuration in Dockerfile for reproducible builds of GUI environments.