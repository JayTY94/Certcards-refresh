In Terraform, modules are reusable components that group resources together. You call them from the root module and pass in variables. Modules don't run independently; they're included via the module block in your main configuration.

Example:

hcl
Copy
Edit
module "vm" {
  source = "./modules/ephemeral"
  vm_name = "dev-vm"
}
=============
The terraform init command initializes the project in the current directory by downloading providers and preparing modules. You only run it once per project, from the root — not inside each module.

=============
Terraform provider blocks declare which cloud or service you're configuring. You must include a provider block like azurerm in the root module, even if the actual resources are defined in submodules.

Example:

hcl
Copy
Edit
provider "azurerm" {
  features {}
  use_cli = true
}
=============
path.module in Terraform refers to the directory containing the module being evaluated. It is used when loading template files (e.g., cloud-init.yaml.tpl) from the same folder.

Example:

hcl
Copy
Edit
templatefile("${path.module}/cloud-init.yaml.tpl", {...})
=============
In a Terraform module, names like "main" or "this" are user-defined labels for a resource block. They are not reserved words — you can choose meaningful names to reference resources elsewhere in your config.

Example:

hcl
Copy
Edit
resource "azurerm_storage_account" "this" { ... }
# Reference: azurerm_storage_account.this.name
=============
Azure Files can be used to persist your coding workspace outside the lifecycle of a virtual machine. It is mounted via SMB on the VM, and can be referenced in Terraform using azurerm_storage_share.

Example:

h
Copy
Edit
mount -t cifs //<storage_account>.file.core.windows.net/<share> /mnt/exercism ...
=============
Terraform allows you to target specific parts of your infrastructure using -target. This makes it possible to destroy or apply only a specific module like a VM while keeping persistent resources like storage intact.

Example:

bash
Copy
Edit
terraform destroy -target=module.ephemeral
=============
The az login command authenticates your local environment with Azure CLI. Terraform can use these credentials by enabling use_cli = true in your provider block.

=============
The cloud-init mechanism in Azure allows Terraform to provision the VM on first boot, such as installing software, mounting storage, or configuring files.

Example inside VM block:

hcl
Copy
Edit
custom_data = base64encode(templatefile("${path.module}/cloud-init.yaml.tpl", {...}))
=============
GitHub imposes a 100 MB file size limit on pushes. Terraform's .terraform/ directory can include large provider binaries and should always be added to .gitignore to avoid push errors.

Example .gitignore:

markdown
Copy
Edit
.terraform/
*.tfstate
*.tfstate.*


=============
The .terraform/ directory stores provider binaries and module cache for your Terraform project. It should never be committed to version control, as it may contain large files or local-only paths.

=============
.gitignore is used to tell Git which files or folders not to track. In Terraform projects, this prevents large or sensitive files like .terraform/ and .tfstate from being added accidentally.

Example:

markdown
Copy
Edit
.terraform/
*.tfstate
*.tfstate.*
=============
The terraform.tfvars file allows you to define values for input variables. It’s automatically loaded during terraform plan or terraform apply, so you don’t have to pass variables via CLI every time.

Example:

hcl
Copy
Edit
ssh_public_key_path = "~/.ssh/id_rsa.pub"
allowed_ssh_cidr    = "192.168.1.0/24"
=============
In Terraform, the output block allows you to print values after apply. Outputs can include public IP addresses, SSH commands, or resource IDs for chaining with other systems.

Example:

hcl
Copy
Edit
output "ssh_command" {
  value = "ssh azureuser@${azurerm_public_ip.main.ip_address}"
}
=============
A cloud-init.yaml.tpl file is a template for provisioning Linux VMs. You use Terraform’s templatefile() function to inject variables and base64-encode it for the VM’s custom_data.

=============
The base64encode() function is used in Terraform to convert the rendered cloud-init template into the format expected by the custom_data field of a VM resource.

=============
use_cli = true in the Azure provider configuration tells Terraform to use your Azure CLI login session instead of manually configured service principals or credentials.


=============
SSH keys are used to securely authenticate to a VM. Terraform expects you to pass the public key path and inject it into the VM at creation, enabling key-based access instead of passwords.

Example in variables.tf:

hcl
Copy
Edit
variable "ssh_public_key_path" {
  default = "~/.ssh/id_rsa.pub"
}
=============
In Windows PowerShell, RSA SSH keys can be generated using ssh-keygen. The key pair should be placed in C:\Users\<YourName>\.ssh\, with the public key path passed into Terraform.

Command:

powershell
Copy
Edit
ssh-keygen -t rsa -b 4096 -f $env:USERPROFILE\.ssh\id_rsa
=============
Terraform modules allow you to organize and reuse code. You can define a VM, network, or storage module once and use it in multiple places with different variables passed in.

Example root call:

hcl
Copy
Edit
module "ephemeral" {
  source = "./modules/ephemeral"
  vm_name = "devbox"
}
=============
The templatefile() function loads a local file and injects variables, often used to populate dynamic scripts, like cloud-init.

Example:

hcl
Copy
Edit
templatefile("${path.module}/cloud-init.yaml.tpl", {
  share_name = var.share_name
})


=============
Data sources in Terraform let you read existing cloud resources without managing them. You use them when you want to reference things created outside of Terraform.

Example:

hcl
Copy
Edit
data "azurerm_client_config" "current" {}
=============
Remote backend lets Terraform store its state file in the cloud (e.g., in Azure Storage) instead of locally. It enables collaboration and avoids losing state when switching machines.


=============
Output values expose key info (like public IPs) after apply. They can be used to chain modules or help humans connect to deployed infrastructure.

Example:

hcl
Copy
Edit
output "ip" {
  value = azurerm_public_ip.this.ip_address
}
=============
Lifecycle blocks let you fine-tune resource behavior — for example, prevent Terraform from destroying something with prevent_destroy = true.

Example:

hcl
Copy
Edit
lifecycle {
  prevent_destroy = true
}


=============
Bastion Host is a secure jump box VM that provides SSH access to private resources. Not required for public VMs but useful in production setups.

=============
Terraform Registry is where official and community-built modules live. You can browse or install modules like Azure/network/azurerm to save time.

Site: https://registry.terraform.io/

=============
TF_LOG=DEBUG is an environment variable that makes Terraform print detailed internal logs. Use this for deep debugging when plan or apply behaves unexpectedly.

=============
ARM Template vs Terraform: Both are infrastructure-as-code for Azure, but Terraform is multi-cloud, more modular, and readable. ARM is native to Azure and more verbose.


=============
VS Code Remote - SSH extension allows you to edit files and run terminals directly inside a remote VM. Great when you can’t install tools locally.

=============
Azure Files vs Blob Storage:

Azure Files: mountable like a network drive, good for persistent shared workspaces

Blob Storage: object store, best for archives, backups, large binaries

=============
Terraform apply -target= allows you to apply or destroy specific modules. Useful when testing or when you want to keep persistent components like storage.

Example:

bash
Copy
Edit
terraform apply -target=module.ephemeral
=============
Resource Naming: Use formatdate() or timestamp() to dynamically add creation dates to resources like VMs.

Example:

hcl
Copy
Edit
locals {
  creation_date = formatdate("YYYYMMDD", timestamp())
}
=============
Cloud-init is a standard way to initialize Linux VMs. Azure reads the custom_data field during VM provisioning and runs your script on first boot.

=============

Let me know if you’d like this grouped into categories (e.g. state, networking, provisioning) or delivered as a study-friendly format (like flashcards, PDF, or Anki deck).