











1
Certified Kubernetes Administrator
# List a single replication controller with specified NAME in ps output format
  kubectl get replicationcontroller web
  
# List deployments in JSON output format, in the "v1" version of the "apps" API group
  kubectl get deployments.v1.apps -o json






2
Certified Kubernetes Administrator
# list the API CRDs and grep out the ones installed for Gateway API
    kubectl get crds | grep gateway





3
Certified Kubernetes Administrator
In Linux, the sysctl interface allows an administrator to modify kernel parameters at runtime. To get a list of all parameters, you can run

  sudo sysctl -a






4
Certified Kubernetes Administrator
Kubernetes classes sysctls as either safe or unsafe. In addition to proper namespacing, a safe sysctl must be properly isolated between pods on the same node. This means that setting a safe sysctl for one pod

  must not have any influence on any other pod on the node
  must not allow to harm the node's health
  must not allow to gain CPU or memory resources outside of the resource limits of a pod.






5
Certified Kubernetes Administrator
Kubernetes – Run a Single Pod

kubectl run nginx --image=nginx:1.25

Creates one bare pod. There is no "kubectl create pod." Use run for a quick one-off container; use create deployment for a managed, self-healing workload.





6
Certified Kubernetes Administrator
kubectl run vs. kubectl create deployment

run: creates a single unmanaged Pod. Dies for good if deleted.
create deployment: creates a Deployment (ReplicaSet + self-healing). Reschedules pods automatically. Supports --replicas.





7
Certified Kubernetes Administrator
Kubernetes – Generate a Manifest Without Creating It

kubectl create deployment web --image=nginx --dry-run=client -o yaml > web.yaml

The dry-run scaffold prints valid YAML without touching the cluster. When you can't recall exact YAML, generate it, then edit. This single habit saves enormous time on the exam.







8
Certified Kubernetes Administrator
Kubernetes – Scale a Deployment

kubectl scale deployment frontend --replicas=5

The flag is --replicas (never --count). Works on replicaset and statefulset too. Conditional form: --current-replicas=2 --replicas=5.







9
Certified Kubernetes Administrator
Kubernetes – Update a Container Image

kubectl set image deployment/web web=nginx:1.26

Syntax is resource/name containerName=newImage. The container name is on the LEFT, which trips people up when it matches the deployment name. Triggers a rolling update automatically.







10
Certified Kubernetes Administrator
Kubernetes – Roll Back a Deployment

kubectl rollout undo deployment/web

The rollout family: status, history, undo, restart. Add --to-revision=3 to target a specific revision. There is no "rollback" command.







11
Certified Kubernetes Administrator
Kubernetes – Expose a Deployment as a Service

kubectl expose deployment api --port=80 --target-port=8080

--port is the Service's port; --target-port is the container's port. Note the flag is kebab-case (--target-port), not the camelCase targetPort used inside YAML.







12
Certified Kubernetes Administrator
CLI Flags vs. YAML Fields

Command-line flags are kebab-case: --target-port, --node-selector, --dry-run.
YAML fields are camelCase: targetPort, nodeSelector, restartPolicy. When a syntax looks "off," check whether the two worlds are being mixed. A camelCase flag is almost always the wrong answer.






13
Certified Kubernetes Administrator
Kubernetes – Add a Taint to a Node

kubectl taint nodes worker-3 gpu=true:NoSchedule

Format is key=value:Effect. The :Effect suffix is unique to taints and does not appear on labels.







14
Certified Kubernetes Administrator
Taint Effects

NoSchedule: blocks new pods that lack a matching toleration.
PreferNoSchedule: soft version; scheduler avoids the node if it can.
NoExecute: blocks new pods AND evicts running pods that don't tolerate it.






15
Certified Kubernetes Administrator
Removing Taints and Labels – Trailing Hyphen

Remove a taint: kubectl taint nodes worker-3 gpu=true:NoSchedule-
Remove a label: kubectl label nodes worker-1 disk- There is no --remove flag. Appending a hyphen to the key is the universal "delete" gesture for metadata.






16
Certified Kubernetes Administrator
Kubernetes – Label a Node

kubectl label nodes worker-1 disk=ssd

Labels use key=value with an equals sign, not a colon. Used later by nodeSelector and Service selectors to target the object.







17
Certified Kubernetes Administrator
Labels vs. Annotations

Labels: identifying key/value pairs you can SELECT on (nodeSelector, Service selectors, -l). Used for scheduling.
Annotations: free-form metadata you CANNOT select on. Used for notes, tooling hints, and build info.






18
Certified Kubernetes Administrator
Kubernetes – Filter Objects by Label

kubectl get pods -l app=web

-l (long form --selector) reads objects by label. Extensions: -l 'env in (prod,stage)', -l '!canary' (label absent), -l app=web,tier=front (AND).







19
Certified Kubernetes Administrator
Kubernetes – Create a ConfigMap From Literals

kubectl create configmap app-config --from-literal=ENV=prod --from-literal=TIER=web

One --from-literal per key; you repeat the flag rather than comma-separating. Related: --from-file=path and --from-env-file=file.







20
Certified Kubernetes Administrator
Kubernetes – Create a Secret

kubectl create secret generic db --from-literal=password=s3cret

Same flag pattern as ConfigMap. Values are base64-encoded automatically. Use --from-file to load a key from a file (e.g. a TLS cert).







21
Certified Kubernetes Administrator
Kubernetes – Create an RBAC Role

kubectl create role pod-reader --verb=get,list,watch --resource=pods

The flags are --verb and --resource. Mnemonic: RBAC rules are "verbs on resources," so the flags are literally --verb and --resource.







22
Certified Kubernetes Administrator
Kubernetes – Bind a Role to a Subject

kubectl create rolebinding readers --role=pod-reader --user=jay

Bind with --user, or --serviceaccount=namespace:sa-name. Cluster-wide equivalents are create clusterrole and create clusterrolebinding.







23
Certified Kubernetes Administrator
Kubernetes – View Logs of a Crashed Container

kubectl logs db --previous

--previous (short -p) shows the last TERMINATED container's logs, where a crash-loop's root cause lives. Plain kubectl logs only shows the current running instance.







24
Certified Kubernetes Administrator
Kubernetes – Open a Shell Inside a Pod

kubectl exec -it tools -- /bin/sh

-it is interactive + TTY. The -- separator marks "everything after is the container's command," not flags for kubectl. Add -c <name> to target one container in a multi-container pod.







25
Certified Kubernetes Administrator
kubectl describe vs. kubectl explain

describe: state of a LIVE object — events, status, conditions. Example: kubectl describe pod db
explain: schema and docs of a FIELD path. Example: kubectl explain deployment.spec.strategy (add --recursive to dump the whole field tree).





26
Certified Kubernetes Administrator
Kubernetes – List Resources Across All Namespaces

kubectl get pods -A

-A equals --all-namespaces. First move when you don't know which namespace a resource lives in.







27
Certified Kubernetes Administrator
Kubernetes – Troubleshoot the Kubelet

systemctl status kubelet

The kubelet is a systemd service, not a pod. Restart with systemctl restart kubelet; read its logs with journalctl -u kubelet. A NotReady node almost always starts here.







28
Certified Kubernetes Administrator
crictl – The Runtime's "docker ps"

crictl ps: list running containers.
crictl logs <id>: read a container's logs.
crictl pods: list pods known to the runtime. Use crictl when the API server or kubelet is down and kubectl can't reach the cluster.





29
Certified Kubernetes Administrator
Kubernetes – Drain a Node for Maintenance

kubectl drain worker-2 --ignore-daemonsets

Drain cordons AND evicts pods. --ignore-daemonsets is almost always required; add --delete-emptydir-data when pods use emptyDir volumes.







30
Certified Kubernetes Administrator
cordon vs. drain

cordon: only marks the node unschedulable. Existing pods keep running.
drain: cordons AND evicts all pods off the node. After maintenance, kubectl uncordon worker-2 re-enables scheduling.






31
Certified Kubernetes Administrator
Kubernetes – Back Up and Restore etcd

ETCDCTL_API=3 etcdctl snapshot save snap.db --endpoints=... --cacert=... --cert=... --key=...

The verb is snapshot save, not backup (that was etcd v2). Restore with etcdctl snapshot restore snap.db. The cert flags are required against a live cluster.







32
Certified Kubernetes Administrator
Kubernetes – Upgrade a Cluster With kubeadm

kubeadm upgrade plan

Flow: upgrade plan (shows target versions) → upgrade apply v1.33.x on the control plane → upgrade node on workers. Each node is wrapped in drain → upgrade kubelet/kubectl packages → uncordon.







33
Certified Kubernetes Administrator
JSONPath Output – Braces Required

kubectl get nodes -o jsonpath='{.items[*].metadata.name}'

-o jsonpath wraps the expression in { }. A List (get nodes) starts at .items[*]; a single object (get node worker-1) starts at .metadata.







34
Certified Kubernetes Administrator
--sort-by – Leading Dot, No Braces

kubectl get pods --sort-by=.status.containerStatuses[0].restartCount

--sort-by also takes a JSONPath, but with NO braces and a leading dot. This inconsistency with -o jsonpath (which uses braces) is the top output-formatting trip-up — memorize both side by side.







35
Certified Kubernetes Administrator
Quick Output Flags

-o wide: extra columns (node, IP).
-o yaml: full manifest of a live object — fast way to see a real spec.
-o name: names only, ideal for scripting and xargs.






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






