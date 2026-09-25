


15
Certified Kubernetes Administrator
# create a deployment named "source-ip-app" that uses the image 'registry.k8s.io/echoserver:1.4'
kubectl create deploy source-ip-app --image registry.k8s.io/echoserver:1.4

# list the deployment and the pods in that deployment
kubectl get deploy,po








16
Certified Kubernetes Administrator
For the deployment named source-ip-app , change the rollout strategy for a deployment to "Recreate".
# edit the deployment and change the rollout strategy to recreate
kubectl edit deploy source-ip-app






17
Certified Kubernetes Administrator
Running a Pod on a Specific Node
    create with kubectl run <podname> --dry-run=client -o yaml > pod.yaml
    edit pod.yaml
    add pod.spec.nodeName: <nodename>
    kubectl apply -f pod.yaml





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






