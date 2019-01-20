`django_container` is a Django project. To see how it is containerized, refer to `Dockerfile` and `docker-compose.yml` files.

Notice that we have 2 containers here: `postgres` and `django`. Deploying with `docker-compose` helps those two containers communicate over the network, this means `django` can resolve the DNS name of `postgres` service into the IP of the `postgres` container.

`django` cannot resolve `postgres` service name if we deploy those 2 containers separatedly.

Next: Put environment variables into separated env files.