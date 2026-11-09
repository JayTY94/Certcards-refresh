



30
Certified Kubernetes Administrator
Since Kubernetes doesn't have a "user" resource, all that's required is a client certificate and key with the common name (CN) to match the user's name.

In our case, when we created the RoleBinding, we assigned it to the user "carlton", so that user will assume the permissions from the Role for that resource.

As long as the CN in the key is "carlton", we will be able to use this to access the Kubernetes API.





31
Certified Kubernetes Administrator
Let's create a Certificate Signing Request (CSR) for the Kubernetes API using our private key and insert the common name and output that to a file named carlton.csr with the following command

openssl req -new -key carlton.key -subj "/CN=carlton" -out carlton.csr 





32
Certified Kubernetes Administrator






33
Certified Kubernetes Administrator






34
Certified Kubernetes Administrator






35
Certified Kubernetes Administrator






36
Certified Kubernetes Administrator






37
Certified Kubernetes Administrator






38
Certified Kubernetes Administrator






39
Certified Kubernetes Administrator






40
Certified Kubernetes Administrator






41
Certified Kubernetes Administrator






42
Certified Kubernetes Administrator






43
Certified Kubernetes Administrator






44
Certified Kubernetes Administrator






45
Certified Kubernetes Administrator






46
Certified Kubernetes Administrator






47
Certified Kubernetes Administrator






48
Certified Kubernetes Administrator






49
Certified Kubernetes Administrator






50
Certified Kubernetes Administrator











1
Certified Kubernetes Administrator






2
Certified Kubernetes Administrator






3
Certified Kubernetes Administrator






4
Certified Kubernetes Administrator






5
Certified Kubernetes Administrator






6
Certified Kubernetes Administrator






7
Certified Kubernetes Administrator






8
Certified Kubernetes Administrator






9
Certified Kubernetes Administrator






10
Certified Kubernetes Administrator






11
Certified Kubernetes Administrator






12
Certified Kubernetes Administrator






13
Certified Kubernetes Administrator






14
Certified Kubernetes Administrator






15
Certified Kubernetes Administrator






16
Certified Kubernetes Administrator






17
Certified Kubernetes Administrator






18
Certified Kubernetes Administrator






19
Certified Kubernetes Administrator






20
Certified Kubernetes Administrator






21
Certified Kubernetes Administrator






22
Certified Kubernetes Administrator






23
Certified Kubernetes Administrator






24
Certified Kubernetes Administrator






25
Certified Kubernetes Administrator






26
Certified Kubernetes Administrator






27
Certified Kubernetes Administrator






28
Certified Kubernetes Administrator






29
Certified Kubernetes Administrator






30
Certified Kubernetes Administrator






31
Certified Kubernetes Administrator






32
Certified Kubernetes Administrator






33
Certified Kubernetes Administrator






34
Certified Kubernetes Administrator






35
Certified Kubernetes Administrator






36
Certified Kubernetes Administrator






37
Certified Kubernetes Administrator






38
Certified Kubernetes Administrator






39
Certified Kubernetes Administrator






40
Certified Kubernetes Administrator






41
Certified Kubernetes Administrator






42
Certified Kubernetes Administrator






43
Certified Kubernetes Administrator






44
Certified Kubernetes Administrator






45
Certified Kubernetes Administrator






46
Certified Kubernetes Administrator






47
Certified Kubernetes Administrator






48
Certified Kubernetes Administrator






49
Certified Kubernetes Administrator






50
Certified Kubernetes Administrator






