FROM ubuntu:16.04
MAINTAINER Allyson Ramkissoon <allys-99.github.io>

RUN apt-get update
RUN cat /etc/lsb-release

RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
