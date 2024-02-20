FROM ubuntu
RUN apt-get update && apt install nginx
EXPOSE 80
VOLUME data
WORKDIR /devops
