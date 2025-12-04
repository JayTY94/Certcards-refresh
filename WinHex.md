
Logical Block Addressing (LBA)
LBA is a linear numbering system for disk sectors, replacing older Cylinder/Head/Sector addressing. Each sector is assigned a unique number starting at 0.
Formula:
Offset (bytes) = LBA × Bytes per sector

Common sector sizes: 512 bytes (legacy) or 4096 bytes (4Kn).
=============
Sector
The smallest addressable unit on a disk.

512 bytes per sector is standard for most drives.
4096 bytes per sector (4Kn) is used on newer disks for efficiency.

=============
Offset
The byte position from the start of the disk.

Calculated as LBA × Bytes per sector.
Example:

LBA 922,617,558 × 512 = 472,364,197,376 bytes ≈ 0x6DFC0DAC00

=============
MBR (Master Boot Record)
Legacy partition table at LBA 0.

Contains boot code and partition entries.
Ends with signature 55 AA.
If wiped, this sector should be all zeros.

=============
GPT (GUID Partition Table)
Modern partitioning system for large disks.

Primary GPT header: LBA 1
Partition array: Starts at LBA 2
Backup GPT header: Last LBA of the disk
Signature: "EFI PART"

=============
Boot Sector
First sector of a filesystem (NTFS, FAT32, exFAT).

NTFS signature: EB 52 90 and "NTFS    "
FAT32 signature: "FAT32   "
exFAT signature: "EXFAT   "

=============
HPA (Host Protected Area) & DCO (Device Configuration Overlay)
Firmware features that hide sectors from the OS.

Common in OEM setups or RAID environments.
Can reduce visible capacity without affecting physical size.

=============
USB Bridge Limitation
Older USB-to-SATA adapters often cap capacity at 32-bit LBA, limiting disks to ~2.2 TB.

Symptom: 4 TB disk shows as ~1.8 TB or 2 TB.
Fix: Use direct SATA or modern UASP bridge.

=============
WinHex Navigation Commands

Open Disk:
Tools → Open Disk → Physical media → \\.\PhysicalDriveN
Go To Sector:
Position → Go To Sector… → Enter LBA number.
Go To Offset:
Position → Go To Offset… → Enter byte offset (decimal or hex).
Check Properties:
Tools → Disk Tools → Interpret Image/File → Properties
Search for Signatures:
Search → Find Text… or Find Hex Values… → Tick “Search entire medium.”

=============
Capacity Reference Table (512 B/sector)

Capacity | LBA | HexOffset
1TB | 1,953,125,000 | 0xE8D4A51000
2 TB | 3,906,250,000 | 0x1D1A94A2000
4 TB | 7,812,500,000 | 0x3A352944000


=============
Key Formula
Offset (bytes) = LBA × Bytes per sector
Hex Offset = Convert Offset to hex

=============
Advanced Adjacent Terms
Zoned Bit Recording (ZBR)
A technique where outer tracks on a disk store more sectors than inner tracks, increasing capacity. Modern drives use ZBR to optimize storage density.
=============
Advanced Format (AF)
A disk technology that uses 4K physical sectors internally while emulating 512-byte logical sectors (512e). Improves error correction and efficiency.
=============
Logical vs Physical Sector Size

Logical sector size: What the OS sees (commonly 512 bytes).
Physical sector size: Actual size on disk (often 4096 bytes in AF drives).

=============
Native Command Queuing (NCQ)
A SATA feature that optimizes the order of read/write commands to improve performance on spinning disks.
=============
TRIM Command
Used by SSDs to inform the drive which blocks are no longer in use, allowing efficient garbage collection and maintaining performance.
=============
Entropy Check
A method to verify sanitization by measuring randomness in disk data. High entropy suggests random overwrite; low entropy (zeros or patterns) suggests deterministic wipe.
=============
Write Amplification
Phenomenon in SSDs where actual writes exceed requested writes due to internal block management. Relevant for secure erase and performance tuning.
=============
Secure Erase vs Crypto Erase

Secure Erase: Overwrites all user-accessible sectors.
Crypto Erase: Deletes encryption keys, rendering all data unrecoverable instantly.

=============
Zoned Namespace (ZNS)
An NVMe feature that organizes storage into zones for better performance and endurance, especially in large-scale SSDs.
=============