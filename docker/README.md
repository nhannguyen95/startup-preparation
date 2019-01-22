`django_container` is a Django project. To see how it is containerized, refer to `Dockerfile` and `docker-compose.yml` files.

Notice that we have 2 containers here: `postgres` and `django`. Deploying with `docker-compose` helps those two containers communicate over the network, this means `django` can resolve the DNS name of `postgres` service into the IP of the `postgres` container.

`django` cannot resolve `postgres` service name if we deploy those 2 containers separatedly.


## Volumes

2 types of mount I learned:
- **Volumes**: mount a volume into a container, this volume is created and managed by Docker. 2 types of volumes: named volume and anonymous volume.
- **Bind mounts**: mount a file or directory on the host machine into a container.


## docker run

For example to run only `postgres` container:

```
docker run
  -d                                       # Detach mode, run container in background
  -it                                      # https://gist.github.com/nhannguyen95/4ca36bc6ec43e7543dc4589cd437a844
  --rm                                     # Automatically remove the container after it exits
  --env KEY1=VALUE1                        # Set environment variables, will override Dockerfile
  --env KEY2=VALUE2
  -p HOST_PORT:CONTAINER_PORT              # Map host port with container port, ex 8080:80/tcp                      
  -v VOLUME_NAME:SOME_PATH_IN_CONTAINER    # Mount a volume into container, type: volume
  -v ABSOLUTE_PATH:SOME_PATH_IN_CONATINER  # Mount a file/directory into container, type: bind mount
```

Next: Put environment variables into separated env files.
