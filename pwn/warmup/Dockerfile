FROM ubuntu:latest
ENV TZ=Asia/Yekaterinburg
EXPOSE 4240/tcp
COPY ./chall /chall

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez
RUN apt-get update
RUN apt-get install -y  ncat
RUN chmod +x /chall/chall
RUN chmod +r /chall/flag*
RUN adduser noob
RUN cd chall && mv flag2 /etc/flag

WORKDIR /chall
USER noob

CMD ncat -k -l -p 4240 -c "./chall"
