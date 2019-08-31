# Example Dockerfile
FROM centos:latest

LABEL "maintainer"="Rhys Campbell"
LABEL "version"="1.0"
LABEL "description"="Just a simple docker file example"

ADD test.txt /root/test.txt
VOLUME /data

RUN /bin/yum update -y

CMD ["/bin/bash"]
