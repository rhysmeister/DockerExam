Docker Certified Associate Exam Study Notes
-------------------------------------------

## Domain 1: Orchestration (25% of exam)

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
* Demonstrate tagging an image
* Utilize a registry to store an image
* Display layers of a Docker image
* Apply a file to create a Docker image
* Modify an image to a single layer
* Describe how image layers work
* Deploy a registry (not architect)
* Configure a registry
* Log into a registry
* Utilize search in a registry
* Tag an image
* Push an image to a registry
* Sign an image in a registry
* Pull an image from a registry
* Describe how image deletion works
* Delete an image from a registry

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
* Setup swarm, configure managers, add nodes, and setup backup schedule
* Create and manager user and teams
* Interpret errors to troubleshoot installation issues without assistance
* Outline the sizing requirements prior to installation
* Understand namespaces, cgroups, and configuration of certificates
* Use certificate-based client-server authentication to ensure a Docker daemon has the rights to access images on a registry
* Consistently repeat steps to deploy Docker engine, UCP, and DTR on AWS and on premises in an HA config
* Complete configuration of backups for UCP and DTR
* Configure the Docker daemon to start on boot

* Trivia
  * A 64 Bit OS is required.
  * Docker UCP requires Docker EE.

* Links
  * [Docker Stroage Drivers](https://docs.docker.com/storage/storagedriver/select-storage-driver/)

### Core Concepts

* https://docs.docker.com/config/containers/resource_constraints/
* https://en.wikipedia.org/wiki/Cgroups

* [Universal Control Plan](https://docs.docker.com/ee/ucp/)

## Domain 4: Networking (15% of exam)

## Domain 5: Security (15% of exam)

## Domain 6: Storage and Volumes (10% of exam)
