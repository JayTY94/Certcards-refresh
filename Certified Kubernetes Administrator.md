




47
Certified Kubernetes Administrator
Mental checklist for node scheduling failures:

    kubectl get nodes — is the node Ready ?
    kubectl describe node <name> — check Conditions and Events for root cause
    SSH to the node → sudo systemctl status kubelet
    Read kubelet logs: sudo journalctl -u kubelet
    Check scheduling events: kubectl get events -n <namespace>






48
Certified Kubernetes Administrator
On the CKA exam, node-level failures are a common troubleshooting topic. Always follow the checklist: 
node status 
→ kubelet service 
→ kubelet logs 
→ scheduling events





49
Certified Kubernetes Administrator
# List recent events in the default namespace
kubectl events

# List recent events in all namespaces
kubectl events --all-namespaces

# List recent events for the specified pod, then wait for more events and list them as they arrive
kubectl events --for pod/web-pod-13je7 --watch





50
Certified Kubernetes Administrator
The HTTPRoute kind specifies routing behavior of HTTP requests from a Gateway listener to backend network endpoints. For a Service backend, an implementation may represent the backend network endpoint as a Service IP or the backing EndpointSlices of the Service. An HTTPRoute represents configuration that is applied to the underlying Gateway implementation.










1
Certified Kubernetes Administrator
For a cluster you're managing yourself, the officially supported tool for deploying Kubernetes is kubeadm.





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






