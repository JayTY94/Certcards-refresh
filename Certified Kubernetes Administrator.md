




26
Certified Kubernetes Administrator







27
Certified Kubernetes Administrator
Kustomize is a tool for customizing Kubernetes configurations. It has the following features to manage application configuration files:

    generating resources from other sources
    setting cross-cutting fields for resources
    composing and customizing collections of resources





28
Certified Kubernetes Administrator
Use --kustomize or -k in kubectl commands to recognize resources managed by kustomization.yaml. Note that -k should point to a kustomization directory, such as

kubectl apply -k <kustomization directory>/






29
Certified Kubernetes Administrator
You can also use a shorthand alias for kubectl that also works with completion:

alias k=kubectl
complete -o default -F __start_kubectl k






30
Certified Kubernetes Administrator
The Metrics API offers a basic set of metrics to support automatic scaling and similar use cases. This API makes information available about resource usage for node and pod, including metrics for CPU and memory.
Run the command 
    k top no controlplane 





31
Certified Kubernetes Administrator
# show the pod and container metrics for the pod named `php-apache` sorted by memory
kubectl top po php-apache --containers --sort-by=memory






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






