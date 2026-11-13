





32
Certified Kubernetes Administrator
If a user deletes a PVC in active use by a Pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any Pods. Also, if an admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC.





33
Certified Kubernetes Administrator
The Retain reclaim policy allows for manual reclamation of the resource. When the PersistentVolumeClaim is deleted, the PersistentVolume still exists and the volume is considered "released". But it is not yet available for another claim because the previous claimant's data remains on the volume. An administrator can manually reclaim the volume with the following steps.





34
Certified Kubernetes Administrator
By specifying a PersistentVolume in a PersistentVolumeClaim, you declare a binding between that specific PV and PVC. 
The binding happens regardless of some volume matching criteria, including node affinity.

kind: PersistentVolumeClaim
metadata:
  ...
spec:
  storageClassName: "" # Empty string must be explicitly set otherwise default StorageClass will be set
  volumeName: foo-pv
  ...



35
Certified Kubernetes Administrator
yaml syntax to reserve a PV for a specific PVC

kind: PersistentVolume
metadata:
  name: foo-pv
spec:
  storageClassName: ""
  claimRef:
    name: foo-pvc
    namespace: foo





36
Certified Kubernetes Administrator
# Set a deployment's nginx container image to 'nginx:1.9.1', and its busybox container image to 'busybox'
kubectl set image deployment/nginx busybox=busybox nginx=nginx:1.9.1

# Update all deployments' and rc's nginx container's image to 'nginx:1.9.1'
kubectl set image deployments,rc nginx=nginx:1.9.1 --all





37
Certified Kubernetes Administrator
# Update image of all containers of daemonset abc to 'nginx:1.9.1'
kubectl set image daemonset abc *=nginx:1.9.1

# Print result (in yaml format) of updating nginx container image from local file, without hitting the server
kubectl set image -f path/to/file.yaml nginx=nginx:1.9.1 --local -o yaml





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






