Public Key Authentication (SSH)
A method where the client proves identity using a private key while the server checks the corresponding public key in ~/.ssh/authorized_keys. No password is sent; authentication succeeds if the key pair matches and permissions are correct.
=============
authorized_keys
A file on the destination host that lists allowed public keys (one per line) for a user. OpenSSH reads it during login; incorrect permissions or ownership will cause key rejection.
=============
known_hosts
A file on the client that caches server host key fingerprints. When you first connect, SSH records the server’s fingerprint and later verifies it to prevent man‑in‑the‑middle attacks.
=============
Host Key Fingerprint
A short, unique summary of a server’s public host key (e.g., ED25519 SHA256 fingerprint). It lets you verify you’re talking to the same server you trusted previously.
=============
Identity File (-i)
The private key file path used by ssh/scp for authentication. It must be the private key (e.g., ~/.ssh/id_rsa), not authorized_keys.
=============
OpenSSH Private Key Format
A text format starting with -----BEGIN OPENSSH PRIVATE KEY----- and ending with -----END OPENSSH PRIVATE KEY-----. It encodes the private key (optionally encrypted with a passphrase).
=============
PEM vs OpenSSH Keys
PEM is a generic container often used for TLS/SSH keys (.pem). OpenSSH can read PEM and its own modern OpenSSH format. Cloud tools sometimes expect PEM; PuTTY expects PPK.
=============
SSH Agent
A local process that holds decrypted private keys in memory so you don’t re‑enter passphrases. Programs like ssh can ask the agent to perform signatures without touching the key file again.
=============
Passphrase vs Password (SSH)
A passphrase secures the private key file itself. A password is an account credential used for interactive login. With key auth, you usually don’t need the account password.
=============
Required Permissions for SSH Keys
~/.ssh must be 700; private keys must be 600; authorized_keys must be 600. Too‑open permissions cause OpenSSH to reject key auth (security feature).
=============
SCP vs SFTP vs rsync
SCP: simple copy over SSH; minimal features.
SFTP: SSH file transfer protocol; resumes, remote listing, better tooling.
rsync: efficient delta copy, preserves metadata; can use SSH as transport.
=============
Recursive Copy with SCP
Use -r to copy directories. Example:
scp -r -i ~/.ssh/id_rsa /home/azureuser user@host:/home/azureuser/target/
=============
Preserving Permissions via Archive
Create a tarball to preserve ownership/perms:
sudo tar -czf /tmp/home.tgz /home → transfer → tar -xzf /path/home.tgz -C /
=============
ED25519 vs RSA
ED25519: modern, fast, small keys, strong security with short fingerprints.
RSA: widely compatible; larger keys; still common but ED25519 preferred when supported.
=============
Key Exchange (KEX)
Algorithms used during SSH handshake to derive shared secrets securely (e.g., curve25519‑sha256). Strong KEX protects against interception during session setup.
=============
Ciphers and MACs (SSH)
Ciphers like aes128-gcm or chacha20‑poly1305 encrypt data; MACs (or AEAD modes) ensure integrity. Prefer modern AEAD ciphers for speed and security.
=============
~/.ssh/config
Per‑user SSH configuration file. You can set defaults:
Host myvm
  HostName 13.91.121.65
  User azureuser
  IdentityFile ~/.ssh/id_rsa

Then connect with ssh myvm.
=============
StrictModes (sshd)
A server‑side option that enforces safe file permissions on user home and .ssh files. If perms are too open, pubkey auth is refused to prevent key theft.
=============
PasswordAuthentication (sshd)
Server setting controlling whether SSH allows password login. If disabled, only key‑based login works; you must have your public key in authorized_keys.
=============
PermitRootLogin (sshd)
Controls whether root can log in directly over SSH. Commonly disabled for security; use sudo from a normal user instead.

=============
Tilde Expansion (~)
A shell shorthand: ~ → current user’s home directory (e.g., /home/azureuser). ~user references another user’s home if allowed.
=============
ssh -v/-vv/-vvv
Verbose flags that show handshake details, which identity files are offered, whether the server accepts the key, and the reason for failures (very helpful for debugging).
=============
Azure VM NSG (Network Security Group)
Firewall rules controlling traffic to/from NICs/subnets. Ensure inbound TCP 22 is allowed from your source IP to reach SSH before auth can even occur.
=============
Azure “Reset password” (Portal)
Portal action that can reset a user’s SSH public key on the VM. Useful when authorized_keys is broken or inaccessible; it writes a new public key for the target username.

=============
Public Key Comment Field
The trailing text on a public key line (after the Base64 blob). It’s optional metadata (e.g., jay@host) to identify the key’s origin; not used for authentication.
=============
SCP Error: “Permission denied (publickey)”
A failure in authentication (not file permissions). The destination didn’t accept the key you offered—usually because the public key is missing/mismatched or perms/username are wrong.
=============
SFTP Interactive Copy
Start an interactive session with:
sftp -i ~/.ssh/id_rsa user@host → then put file, get file, mkdir, ls. Supports resume and better error messages compared to scp.
=============
Key Fingerprint Verification
Compare the server’s displayed fingerprint with a trusted value before typing yes. This prevents trusting an impostor server in the first connection.
=============
SSH Multiplexing (ControlMaster)
Reuses a single TCP connection for multiple SSH sessions to the same host, speeding up repeated commands and SCP. Configure in ~/.ssh/config with ControlMaster auto.