kubectl config get-users



Write all kubeconfig context names into /course/1/contexts, one per line

Write the name of the current context into /course/1/current-context

Write the client-certificate of user account-0027 base64-decoded into /course/1/cert
*I can't figure out this one.


Install cert-manager using Helm in Namespace cert-manager. Then configure and create a ClusterIssuer resource:

    Create Namespace cert-manager

    Install Helm chart jetstack/cert-manager (with crds.enabled=true) into the new Namespace. The Helm Release should be called cert-manager
    I don't know this one

    Update the ClusterIssuer resource in /course/2/cluster-issuer.yaml to include crlDistributionPoints: ["http://example.com/crl"] under spec.selfSigned

    Create the ClusterIssuer resource from /course/2/cluster-issuer.yaml

I totally forget how to get the names of pods and pipe them into other arguments to say, get the qos of them or get their top pods --containers info