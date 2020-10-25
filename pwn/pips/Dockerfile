FROM ubuntu:latest
ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez
EXPOSE 4242:4242/tcp
RUN apt-get update && apt-get install -y python3 python3-pip wget
RUN apt-get install -y e2tools qemu unzip qemu-system
RUN apt-get install -y gcc-mipsel-linux-gnu
RUN pip3 install arm_now
COPY ./chall /chall
RUN arm_now install mips32el
RUN cd /chall && ./install.sh

WORKDIR /chall
RUN chmod 777 -R /chall
CMD ["./run.sh"]
