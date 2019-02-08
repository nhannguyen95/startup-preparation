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

If a node dies, the pods inside that node die with it. The deployment will create new ones with different IPs. Service solves this problem, it is an abstraction which defines a logical set of Pods. When created, each Service is assigned a unique IP address (also called Cluster-IP - the one shown when we describe the service). This address is tied to the lifespan of the Service, and will not change while the Service is alive. The traffic will be load-balanced to the target Pods.

Pod's IP is not exposed outside without a Service.

Services match *a set of Pods* using labels and selectors.

Different types of services:
- Cluster IP: Exposes the Service on an internal IP in the cluster. This type makes the Service only reachable from within the cluster.
 
- NodePort - Exposes the Service on the same port of each selected Node in the cluster using NAT. Makes a Service accessible from outside the cluster using `<NodeIP>:<NodePort>`. Superset of ClusterIP.
  
  The K8s Master will allocate a same port (the `nodePort`, default range in 30000-32767) on every Node (regardless of whether the Node contains the target Pod or not, the traffic will be load-balanced), and each Node will proxy that port into the Service. 

- LoadBalancer - Creates an external load balancer in the current cloud (if supported) and assigns a fixed, external IP to the Service. Superset of NodePort.

  Cloud providers will provision a load balancer for the Service. This means the traffic will travel through the `port` that maps to the pods, not through `nodePort`.

Services will monitor continuously the running Pods using Endpoints, to ensure the traffic is sent only to available Pods (when they are scaled). Each Endpoint is a pair of Pod's IP address and the port that is mapped to the Service (you can enquire this using `kubectl describe svc <svc_name>`.

---

**Job**

A job creates one or more pods and ensures that a specified number of them successfully terminate. As pods successfully complete, the job tracks the successful completions. When a specified number of successful completions is reached, the job itself is complete. Deleting a Job will cleanup the pods it created.

A simple case is to create one Job object in order to reliably run one Pod to completion. The Job object will start a new Pod if the first pod fails or is deleted (for example due to a node hardware failure or a node reboot).

---

Defining a Deployment:

```yaml
apiVersion: apps/v1  # When Kubernetes has a release that updates what is available for you to use—changes something in its API—a new apiVersion is created.
kind: Deployment
metadata:
 name: my-nginx  # Deployment's label
spec:
 selector:  # how the Deployment finds which Pods to manage
  matchLabels:
   run: my-nginx
 replicas: 2
 template:
  metadata:
   labels:
    run: my-nginx  # pods' label
  spec:
   containers:
   - name: my-nginx
     image: nginx
     imagePullPolicy: Always  # the image is pulled every time the pod is started
     resources:
      requests:
       cpu: 100m  # (milicores) = 0.1 core = 0.1 K8s CPU = 0.1 GCP vCPU
       memory: 64Mi  # (mebi) = 64 * 1024^2 (bytes)
     env:
     - name: ENV_NAME
       value: ENV_VALUE
     - name: ENV_NAME_SEC
       valueFrom:
        secretKeyRef:
         name: env_name_abc
         key: env_key_abc
     ports:
     - containerPort: 80  # Expose and map container's port 80 to pod's port 80
 
```

Defining a Service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nginx  # this service is assigned an IP address
  labels:
    run: my-nginx
spec:
  type: ClusterIP  # default service type is ClusterIP
  selector:
    run: my-nginx  # labels of the target set of Pods
  ports:
  - protocol: TCP  # TCP is default
    port: 8080  # port of the service
    targetPort: 80  # exposed port of the set of Pods,
                    # by default it takes the same value as port
```

Defining a Job:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
 name: <job_name>
spec:
 template:
  spec:
   containers:
   - name: <container_name>
     image: <container_image>
     command: <command_when_container_starts>
   restartPolicy: Never  # This applies for all containers in the Pod.
                         # For a Job, only 2 values are accepted: Never and OnFailure.
                         # If restartPolicty=Never, the Job will retry (in case it fails)
                         # by spin up new pods.
 backoffLimit: 4  # specify the number of retries before considering a Job as failed

```

---

**References**:
- [Networking with Kubernetes](https://www.youtube.com/watch?v=WwQ62OyCNz4)
- [K8s API docs](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13)
- [Which Kubernetes apiVersion Should I Use?](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-apiversion-definition-guide.html)
