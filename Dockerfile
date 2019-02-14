FROM ubuntu:16.04
MAINTAINER Allyson Ramkissoon <allys-99.github.io>

RUN apt-get update
RUN cat /etc/lsb-release
RUN apt-get install -y vim
RUN apt-get -y install python3
RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
ADD our_csv_parser_file.py /
ADD hello.py /
ADD housing.data.txt /
ENTRYPOINT ["python3"]
CMD ["./our_csv_parser_file.py"]
