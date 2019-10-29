Docker Certified Associate Exam Study Notes
-------------------------------------------

## Domain 1: Orchestration (25% of exam)

* Complete the setup of a swarm mode cluster, with managers and worker nodes
  * [Getting started with swarm mode](https://docs.docker.com/engine/swarm/swarm-tutorial/)
  * [Create a Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/)
  * [Create a Docker Swarm with Vagrant & Ansible](https://github.com/rhysmeister/DockerSwarm)

* State the differences between running a container vs running a service
  * docker run is used to create a standalone container.
  * docker service create is used to create instances (called tasks) of that service running in a cluster (called swarm) of computers (called nodes). Those tasks are containers of course, but not standalone containers. In a sense a service acts as a template when instantiating tasks.
  * [Stackoverflow Link](https://stackoverflow.com/questions/43408493/what-is-the-difference-between-docker-service-and-docker-container)
  * [docker service is the new docker run](https://events.static.linuxfound.org/sites/events/files/slides/ContainerCon%20Berlin%20%28Goelzer%29%20-%20Upload%209-18-2016.pdf)
  * [How services work](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/)

* Demonstrate steps to lock a swarm cluster

Enable locking when creating the swarm cluster.

```
docker swarm init --autolock
```

Enable locking for an existing swarm cluster.

```
docker swarm update --autolock=true
```

Unlock a swarm cluster after a restart. You will be prompted for the key.

```
docker swarm unlock
```

You can retrieve the key with the following command.

```
docker swarm unlock-key
```

Rotate the key with...

```
docker swarm unlock-key --rotate
```

[Lock your swarm to protect its encryption key](https://docs.docker.com/engine/swarm/swarm_manager_locking/)

* Extend the instructions to run individual containers into running services under swarm
* Interpret the output of "docker inspect" commands
  * [Docker Inspect](https://docs.docker.com/engine/reference/commandline/inspect/)

* Convert an application deployment into a stack file using a YAML compose file with "docker stack deploy"
* Manipulate a running stack of services
* Increase # of replicas
  * [docker scale](https://docs.docker.com/engine/reference/commandline/service_scale/)

Live modification

```bash
docker service scale frontend=50
docker service scale backend=10 proxy=5
```

or

```
docker service update --replicas=20 mystack_web
```

It is probably a better idea to update the stack file and redeploy the stack...

```
docker stack  deploy --compose-file mystack-file.yml
```

* Add networks, publish ports

Publish a port

```
docker service update --publish-add published=8080,target=8080 myservice
```

* Mount volumes

Add a volume

```
docker service update --mount-add type=volume,source=web-vol,target=web-vol-dir myservice
```

List volumes

```
docker volume ls
```

* Illustrate running a replicated vs global service
  * [Replicated and global services](https://docs.docker.com/engine/swarm/how-swarm-mode-works/services/#replicated-and-global-services)

* Identify the steps needed to troubleshoot a service not deploying
  * [docker service logs](https://docs.docker.com/engine/reference/commandline/service_logs/)
* Apply node labels to demonstrate placement of tasks

Add a label

```
docker node update --label-add foo worker1
```

Add multiple labels

```
docker node update --label-add foo --label-add bar worker1
```

  * [docker node update](https://docs.docker.com/engine/reference/commandline/node_update/)

Add a constraint to a service

```
docker service create \
  --name redis_2 \
  --constraint 'node.labels.type == queue' \
  redis:3.0.6
```

Add a placement preference

```
$ docker service create \
  --replicas 9 \
  --name redis_2 \
  --placement-pref 'spread=node.labels.datacenter' \
  redis:3.0.6
```

* Sketch how a Dockerized application communicates with legacy systems
* Paraphrase the importance of quorum in a swarm cluster
* Demonstrate the usage of templates with "docker service create"

## Domain 2: Image Creation, Management and Registry (20% of exam)

* Describe Dockerfile options [add, copy, volumes, expose, entrypoint, etc)
    * [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
    * **FROM** - A Dockerfile must start with a FROM instruction. The FROM instruction specifies the base image from which you are building.
    * **ADD** - The ADD instruction copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.
    * **COPY** - The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
    * **VOLUME** - The VOLUME instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. The value can be a JSON array, VOLUME ["/var/log/"], or a plain string with multiple arguments, such as VOLUME /var/log or VOLUME /var/log /var/db. For more information/examples and mounting instructions via the Docker client, refer to Share Directories via Volumes documentation.
    * **EXPOSE** - The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified. The EXPOSE instruction does not actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To actually publish the port when running the container, use the -p flag on docker run to publish and map one or more ports, or the -P flag to publish all exposed ports and map them to high-order ports.
    * **ENTRYPOINT** - An ENTRYPOINT allows you to configure a container that will run as an executable.
    * **RUN** - The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.
    * **CMD** - There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect. The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.
    * **LABEL** - The LABEL instruction adds metadata to an image. A LABEL is a key-value pair. To include spaces within a LABEL value, use quotes and backslashes as you would in command-line parsing.

Example docker file

```
# Example Dockerfile
FROM centos:latest

LABEL "maintainer"="Rhys Campbell"
LABEL "version"="1.0"
LABEL "description"="Just a simple docker file example"

ADD test.txt /root/test.txt
VOLUME /data

RUN /bin/yum update -y

CMD ["/bin/bash"]
```

Build and run with...

```
docker build -t rhys:example .
docker run --rm -ti rhys:example
```


* Show the main parts of a Dockerfile
* Give examples on how to create an efficient image via a Dockerfile
* Use CLI commands such as list, delete, prune, rmi, etc to manage images
* Inspect images and report specific attributes using filter and format
  * [docker image inspect](https://docs.docker.com/engine/reference/commandline/image_inspect/)

Get Config section in json format

```
docker image inspect 486 --format='{{json .Config}}'
```

Get the hostname value from the Config section

```
docker image inspect 486 --format='{{.Config.Hostname}}'
```

We can also inspect containers with [docker container inspect](https://docs.docker.com/engine/reference/commandline/container_inspect/)

* Demonstrate tagging an image
  * [docker image tag](https://docs.docker.com/engine/reference/commandline/image_tag/)

* Utilize a registry to store an image
* Display layers of a Docker image
  * [docker history](https://docs.docker.com/engine/reference/commandline/history/)
  * [Digging into Docker layers](https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612)
* Apply a file to create a Docker image
* Modify an image to a single layer

This can be achieved in two ways...

1. Build image with squash option (current experimental feature that must be enabled)

```
docker build --squash -t rhys:new .
```

Note layers in new image...

```
docker image history rhys:new
```

There's only one (note merge message and <missing> flags)....

```
IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
7b348eee45aa        14 seconds ago                                                      87.1MB              merge sha256:ecb208515985bac886178ae2244bdefda65bd528734ce75a38213da6cebe00d2 to sha256:a2a15febcdf362f6115e801d37b5e60d6faaeedcb9896155e5fe9d754025be12
<missing>           4 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/sh" "-c" "\"/u…   0B                  
<missing>           4 weeks ago         /bin/sh -c apt-get -y install vim               0B                  
<missing>           4 weeks ago         /bin/sh -c apt-get update -y                    0B                  
<missing>           4 weeks ago         /bin/sh -c #(nop) ADD file:3e06daef2777a9a4a…   0B                  
<missing>           4 weeks ago         /bin/sh -c #(nop)  MAINTAINER rhys.james.cam…   0B                  
<missing>           6 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
<missing>           6 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B                  
<missing>           6 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   745B                
<missing>           6 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     987kB               
<missing>           6 weeks ago         /bin/sh -c #(nop) ADD file:c477cb0e95c56b51e…   63.2MB
```

2. The second exports an image from a running container

```
docker container export my_container > my_container.tar
```

This can then be imported into docker

```
docker image import my_container.tar
```

* Describe how image layers work

View the layers of an image...

```
docker image history rhys:latest
```

* Deploy a registry (not architect)

[Deploy a registry server](https://docs.docker.com/registry/deploying/)

```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

[Docker Trusted Registry overview](https://docs.docker.com/ee/dtr/)

* Configure a registry
* Log into a registry

Login to docker hub

```
docker login
```

Login to docker registry container (must be previously deployed)

```
doccker login localhost:5000
```

* Utilize search in a registry
  * [docker search](https://docs.docker.com/engine/reference/commandline/search/)

Search for ubuntu images

```
docker search ubuntu
```

Ubuntu images with 5 or more stars

```
docker search ubuntu --filter=stars=5
```

Limit to 5 results

```
docker search ubuntu --filter=stars=5 --limit=5
```

Official centos images

```
docker search centos --filter "is-official=true"
```

Official centos images with 50 or more stars

```
docker search centos --filter "is-official=true" --filter "stars=50"
```

* Tag an image
  * [docker tag](https://docs.docker.com/engine/reference/commandline/tag/)

* Push an image to a registry
  * [docker push](https://docs.docker.com/engine/reference/commandline/push/)

* Sign an image in a registry
* Pull an image from a registry
  * [docker pull](https://docs.docker.com/engine/reference/commandline/pull/)

* Describe how image deletion works
* Delete an image from a registry
  * [docker image rm](https://docs.docker.com/engine/reference/commandline/image_rm/)

## Domain 3: Installation and Configuration (15% of exam)

* Demonstrate the ability to upgrade the Docker engine
* Complete setup of repo, select a storage driver, and complete installation of Docker engine on multiple platforms

  * Repositories
    * [Docker Hub](https://docs.docker.com/docker-hub/repos/)

  * [Storage Drivers](https://docs.docker.com/storage/storagedriver/select-storage-driver/)
    * overlay2 is the preferred storage driver, for all currently supported Linux distributions, and requires no extra configuration.
    * aufs is the preferred storage driver for Docker 18.06 and older, when running on Ubuntu 14.04 on kernel 3.13 which has no support for overlay2.
    * devicemapper is supported, but requires direct-lvm for production environments, because loopback-lvm, while zero-configuration, has very poor performance. devicemapper was the recommended storage driver for CentOS and RHEL, as their kernel version did not support overlay2. However, current versions of CentOS and RHEL now have support for overlay2, which is now the recommended driver.
    * The btrfs and zfs storage drivers are used if they are the backing filesystem (the filesystem of the host on which Docker is installed). These filesystems allow for advanced options, such as creating “snapshots”, but require more maintenance and setup. Each of these relies on the backing filesystem being configured correctly.
    * The vfs storage driver is intended for testing purposes, and for situations where no copy-on-write filesystem can be used. Performance of this storage driver is poor, and is not generally recommended for production use.

  * Installing Docker on multiple platforms
    * [Docker Installation](https://docs.docker.com/install/)

* Configure logging drivers (splunk, journald, etc)
  * [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/)
  * The default logging driver is json-file.
  * The default can be changed in /etc/docker/daemon.json, i.e.

```
{
  "log-driver": "syslog"
}
```

  * We can change a container's default log driver when starting it...

```
  docker run -it --log-driver syslog alpine ash
```

* Setup swarm, configure managers, add nodes, and setup backup schedule
  * [Create a Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/)
  * [Create a Swarm Manager](https://docs.docker.com/swarm/reference/manage/)
  * [Add Nodes to the Swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/)
* Create and manager user and teams
  * [Create and Manage Users](https://docs.docker.com/v17.09/datacenter/ucp/2.2/guides/access-control/create-and-manage-users/)
  * [Create and Manage Teams](https://docs.docker.com/v17.09/datacenter/ucp/2.2/guides/access-control/create-and-manage-teams/)
* Interpret errors to troubleshoot installation issues without assistance
  * Common issue is only being able to run docker with root. Fix is to add user to docker group...
```
sudo usermod -aG docker $USER
```

* Outline the sizing requirements prior to installation
* Understand namespaces, cgroups, and configuration of certificates
  * [Namespaces](https://en.wikipedia.org/wiki/Linux_namespaces)
  * [cgroups](https://en.wikipedia.org/wiki/Cgroups)
  * [certificates](https://docs.docker.com/ee/ucp/admin/configure/use-your-own-tls-certificates/)
  * [Understanding Docker Internals](https://medium.com/@nagarwal/understanding-the-docker-internals-7ccb052ce9fe)

* Use certificate-based client-server authentication to ensure a Docker daemon has the rights to access images on a registry
* Consistently repeat steps to deploy Docker engine, UCP, and DTR on AWS and on premises in an HA config
* Complete configuration of backups for UCP and DTR
* Configure the Docker daemon to start on boot

* Trivia
  * A 64 Bit OS is required.
  * Docker UCP requires Docker EE.

* Links
  * [Docker Storage Drivers](https://docs.docker.com/storage/storagedriver/select-storage-driver/)

### Core Concepts

* https://docs.docker.com/config/containers/resource_constraints/
* https://en.wikipedia.org/wiki/Cgroups

* [Universal Control Plan](https://docs.docker.com/ee/ucp/)

## Domain 4: Networking (15% of exam)

[Docker Networks](https://success.docker.com/article/networking)

* Create a Docker bridge network for a developer to use for their containers

```bash
docker network create --driver bridge my-custom-net
```
[Use bridge networks](https://docs.docker.com/network/bridge/)

* Troubleshoot container and engine logs to understand a connectivity issue between containers
* Publish a port so that an application is accessible externally

Publish a port 8080 on the host to 80 on the container

```bash
docker container run -dit --rm -p 8080:80 nginx
```

Publish ports specified in the docker file with a random high port

```bash
docker container run -dit --rm -P nginx
```

* Identify which IP and port a container is externally accessible on

```bash
docker container port focused_davinci
```

```
80/tcp -> 0.0.0.0:32768
```

The inspect command will also show this information.

* Describe the different types and use cases for the built-in network drivers
  * bridge: The default network driver. If you don’t specify a driver, this is the type of network you are creating. Bridge networks are usually used when your applications run in standalone containers that need to communicate. See bridge networks.
  * host: For standalone containers, remove network isolation between the container and the Docker host, and use the host’s networking directly. host is only available for swarm services on Docker 17.06 and higher. See use the host network.
  * overlay: Overlay networks connect multiple Docker daemons together and enable swarm services to communicate with each other. You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons. This strategy removes the need to do OS-level routing between these containers. See overlay networks.
  * macvlan: Macvlan networks allow you to assign a MAC address to a container, making it appear as a physical device on your network. The Docker daemon routes traffic to containers by their MAC addresses. Using the macvlan driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host’s network stack. See Macvlan networks.
  * none: For this container, disable all networking. Usually used in conjunction with a custom network driver. none is not available for swarm services. See disable container networking.
  * Network plugins: You can install and use third-party network plugins with Docker. These plugins are available from Docker Hub or from third-party vendors. See the vendor’s documentation for installing and using a given network plugin.
  * [Docket native networking drivers](https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/)
* Understand the Container Network Model and how it interfaces with the Docker engine and network and IPAM drivers
* Configure Docker to use external DNS
* Use Docker to load balance HTTP/HTTPs traffic to an application (Configure L7 load balancing with Docker EE)

[Use a Load Balancer](https://docs.docker.com/ee/ucp/admin/configure/join-nodes/use-a-load-balancer/)
[Docker Swarm Load Balancing with NGINX and NGINX Plus](https://www.nginx.com/blog/docker-swarm-load-balancing-nginx-plus/)
[How to get started with load balancing Docker Swarm mode](https://upcloud.com/community/tutorials/load-balancing-docker-swarm-mode/)

* Understand and describe the types of traffic that flow between the Docker engine, registry, and UCP controllers
  * [Docker EE Architecture](https://docs.docker.com/ee/docker-ee-architecture/)
* Deploy a service on a Docker overlay network

Create a new overlay network

```bash
docker network create --driver overlay my-overlay-network
```

Create a service on this new network using the nginy container

```bash
docker service create --network=my-overlay-network --name=rhys1 --replicas=6 nginx
```

List the newly created service

```bash
docker service ls
```

Inspect the newly create service

```bash
docker service inspect rhys1
```

* Describe the difference between "host" and "ingress" port publishing mode

## Domain 5: Security (15% of exam)

[Docker Security](https://docs.docker.com/engine/security/security/)

* Describe the process of signing an image
* Demonstrate that an image passes a security scan
* Enable Docker Content Trust
  * [Content trust in Docker](https://docs.docker.com/engine/security/trust/content_trust/)

```bash
export DOCKER_CONTENT_TRUST=1
```

* Configure RBAC in UCP
* Integrate UCP with LDAP/AD
* Demonstrate creation of UCP client bundles
* Describe default engine security
* Describe swarm default security
* Describe MTLS
* Identity roles
* Describe the difference between UCP workers and managers
  * Swarm Managers
    * Maintain cluster state.
    * Schedule services.
    * Serve as swarm http endpoints.
  * Swarm Workers
    * Sole purpose is to execute container workloads.
* Describe process to use external certificates with UCP and DTR

## Domain 6: Storage and Volumes (10% of exam)

* State which graph driver should be used on which OS
* Demonstrate how to configure devicemapper
  * [Device Mapper Storage Driver](https://docs.docker.com/storage/storagedriver/device-mapper-driver/)
* Compare object storage to block storage, and explain which one is preferable when available
  * [Object Storage versus Block Storage: Understanding the Technology Differences](https://www.druva.com/blog/object-storage-versus-block-storage-understanding-technology-differences/)
  * [An Introduction to Storage for Docker Enterprise](https://success.docker.com/article/an-introduction-to-storage-solutions-for-docker-enterprise)
  * [Block Storage, Object Storage, and File Systems: What They Mean for Containers](https://rancher.com/block-object-file-storage-containers/)
* Summarize how an application is composed of layers and where those layers reside on the filesystem
* Describe how volumes are used with Docker for persistent storage
  * Volumes are easier to back up or migrate than bind mounts.
  * You can manage volumes using Docker CLI commands or the Docker API.
  * Volumes work on both Linux and Windows containers.
  * Volumes can be more safely shared among multiple containers.
  * Volume drivers let you store volumes on remote hosts or cloud providers, to encrypt the contents of volumes, or to add other functionality.
  * New volumes can have their content pre-populated by a container.
  * [Docker Volumes](https://docs.docker.com/storage/volumes/)
  * [Managing Persistence for Docker Containers](https://thenewstack.io/methods-dealing-container-storage/)
  * [Additional: Bind Mounts](https://docs.docker.com/storage/bind-mounts/)
* Identify the steps you would take to clean up unused images on a filesystem, also on DTR

Prune dangling images

```bash
docker image prune
```

Prune unused volumes

```bash
docker volume prune
```

Prune all stopped containers, unused networks, dangling images and all build caches

```bash
docker system prune
```

* Demonstrate how storage can be used across cluster nodes
