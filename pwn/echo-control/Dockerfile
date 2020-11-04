FROM ubuntu:latest
ENV TZ=Asia/Yekaterinburg
EXPOSE 6661/tcp
COPY ./chall /chall

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez
RUN apt-get update
RUN apt-get install -y ncat
RUN chmod +x /chall/echo-control
RUN chmod +r /chall/flag
RUN adduser winner

WORKDIR /chall
USER winner

CMD ncat -k -l -p 6661 -c "./echo-control"
