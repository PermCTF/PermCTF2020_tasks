FROM ubuntu:latest
ENV TZ=Asia/Yekaterinburg
EXPOSE 4240/tcp
COPY ./chall /chall

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez
RUN apt-get update
RUN apt-get install -y build-essential ncat
RUN chmod 777 -R /chall
RUN adduser noob
RUN cd chall && gcc -o chall main.c
RUN cd chall && rm main.c
RUN cd chall && mv flag2 /etc/flag

WORKDIR /chall
USER noob

#CMD ./ynetd  -p "0.0.0.0:4241 localhost:4241" ./chall
CMD ncat -k -l -p 4241 -c "./chall"
