**Cluster**

Kubernetes cluster contains master and nodes. 

Master is responsible for managing the cluster.

Nodes and end users communicate with Master via Kubernetes API (kubectl)

---

**Pod**

Containers in a Pod can share resources: volumes, an IP address (each pod in a cluster has a unique IP address), port space and run on the same node. Replicas of pods can span on multiple nodes.

In case of a Node failure, identical Pods are scheduled on other available Nodes in the cluster.

Pods' networking model: each Pod initially has its own cluster-private-IP address. This means:
- Containers within a Pod can all reach each other’s ports on localhost.
- All pods in a cluster can see each other without NAT (no need to know the IP of the Cluster the Pod is deployed on).

---
 
**Node**

A node can have multiple Pods. The Master handles scheduling pods across Nodes.

Each node runs kubelet to communicate with Master and container runtime like Docker to pull images etc.   

---

**Service**

Pod's IP is not exposed outside without a Service.

Services match *a set of Pods* using labels and selectors.

Different types of services:
- Cluster IP: Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
- NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using <NodeIP>:<NodePort>. Superset of ClusterIP.
- LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.

Services will monitor continuously the running Pods using endpoints, to ensure the traffic is sent only to available Pods (when they are scaled)

---

Defining a service:

```yaml
kind: Service
apiVersion: v1
metadata:
  name: my-service  # this service is assigned an IP address
spec:  # default service type is ClusterIP
  selector:
    app: MyApp  # labels of the target set of Pods
  ports:
  - protocol: TCP  # TCP is default
    port: 80  # port of the service
    targetPort: 9376  # exposed port the the set of Pods,
                      # by default it takes the same value as port
    
```

---

**References**:

- [Networking with Kubernetes](https://www.youtube.com/watch?v=WwQ62OyCNz4)
