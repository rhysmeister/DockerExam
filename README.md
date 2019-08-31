Docker Certified Associate Exam Study Notes
-------------------------------------------

## Domain 1: Orchestration (25% of exam)

## Domain 2: Image Creation, Management and Registry (20% of exam)

* Describe Dockerfile options [add, copy, volumes, expose, entrypoint, etc)
..* [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
..* FROM - A Dockerfile must start with a FROM instruction. The FROM instruction specifies the base image from which you are building.
..* ADD - The ADD instruction copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.
..* COPY - The COPY instruction copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>.
..* VOLUMES - The VOLUME instruction creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers. The value can be a JSON array, VOLUME ["/var/log/"], or a plain string with multiple arguments, such as VOLUME /var/log or VOLUME /var/log /var/db. For more information/examples and mounting instructions via the Docker client, refer to Share Directories via Volumes documentation.
..* EXPOSE - The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified. The EXPOSE instruction does not actually publish the port. It functions as a type of documentation between the person who builds the image and the person who runs the container, about which ports are intended to be published. To actually publish the port when running the container, use the -p flag on docker run to publish and map one or more ports, or the -P flag to publish all exposed ports and map them to high-order ports.
..* ENTRYPOINT - An ENTRYPOINT allows you to configure a container that will run as an executable.
..* RUN - The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.
..* CMD - There can only be one CMD instruction in a Dockerfile. If you list more than one CMD then only the last CMD will take effect. The main purpose of a CMD is to provide defaults for an executing container. These defaults can include an executable, or they can omit the executable, in which case you must specify an ENTRYPOINT instruction as well.
..* LABEL - The LABEL instruction adds metadata to an image. A LABEL is a key-value pair. To include spaces within a LABEL value, use quotes and backslashes as you would in command-line parsing.

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

## Domain 4: Networking (15% of exam)

## Domain 5: Security (15% of exam)

## Domain 6: Storage and Volumes (10% of exam)
