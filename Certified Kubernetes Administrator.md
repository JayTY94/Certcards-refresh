





20
Certified Kubernetes Administrator
Create an Ingress resource that will allow you to resolve the domain name hello.com to the service named apache-svc over port 80 .
Remember that the domain resolution is handled with Ingress/spec/- host: "hello.com"




21
Certified Kubernetes Administrator
# view the config that kubelet uses to authenticate to the Kubernetes API
cat /etc/kubernetes/kubelet.conf > kubelet-config.txt

# view the certificate using openssl. Get the certificate file location from the 'kubelet.conf' file above. 
openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text -noout







22
Certified Kubernetes Administrator
# using 'auth can-i', verify that you can create deployments as the 'secure-sa' service account in the default namespace
kubectl auth can-i create deploy --namespace default --as=system:serviceaccount:default:secure-sa

# using 'auth can-i', verify that you CANNOT delete daemonSets as the 'secure-sa' service account in the kube-system namespace 
kubectl auth can-i delete ds --namespace kube-system --as=system:serviceaccount:default:secure-sa







23
Certified Kubernetes Administrator
# create a role binding named 'acme-corp-role-binding', add 'acme-corp-clusterrole' role and 'secure-sa' serviceaccount
kubectl -n default create rolebinding acme-corp-role-binding --clusterrole=acme-corp-clusterrole --serviceaccount=default:secure-sa









24
Certified Kubernetes Administrator
# create a role binding named 'acme-corp-role-binding', add 'acme-corp-clusterrole' role and 'secure-sa' service account
kubectl -n default create rolebinding acme-corp-role-binding --clusterrole=acme-corp-clusterrole --serviceaccount=default:secure-sa

I was missing the namespace stuff when I did this in an exercise.









25
Certified Kubernetes Administrator
# using 'auth can-i', verify that you can create deployments as the 'secure-sa' service account in the default namespace
kubectl auth can-i create deploy --namespace default --as=system:serviceaccount:default:secure-sa

# using 'auth can-i', verify that you CANNOT delete daemonSets as the 'secure-sa' service account in the kube-system namespace 
kubectl auth can-i delete ds --namespace kube-system --as=system:serviceaccount:default:secure-sa





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






