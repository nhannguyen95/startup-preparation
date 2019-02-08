```bash
kubectl get pods -o wide  # more information
```

```bash
kubectl get ep <svc_name>  # endpoints of a service
```

```bash
# Use two dashes (--) to separate your command's flags/arguments
kubectl exec <pod_name> -c <container_name> -- ls -al
```
