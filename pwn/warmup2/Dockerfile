FROM ubuntu:latest
ENV TZ=Asia/Yekaterinburg
EXPOSE 4241/tcp
COPY ./chall /chall

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez
RUN apt-get update
RUN apt-get install -y ncat
RUN chmod +x /chall/chall
RUN chmod +r /chall/flag*
RUN useradd -ms /bin/bash noob
RUN cd chall && mv flag2 /etc/flag

WORKDIR /chall
USER noob

CMD ncat -k -l -p 4241 -c "./chall"
