FROM ubuntu:latest

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timez

COPY ./chall /chall

# installing&configuring ssh_server
RUN apt-get update && apt-get install -y openssh-server net-tools
RUN mkdir /var/run/sshd
RUN echo 'root:!Supe4sec3re!' | chpasswd
RUN useradd -p Am1sTrAng@r stranger
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
ENV NOTVISIBLE="in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile


#test
RUN netstat -tulpn
# installing pwn stuff
RUN apt-get install -y python gcc python-dev curl vim nano
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py
RUN rm get-pip.py 
RUN pip install pwntools 

# configuring access  
RUN chown root:root /chall/flag
RUN chown root:root /chall/stupid-rope
RUN chown stranger:stranger /chall/makefile
RUN chmod +s /chall/stupid-rope

WORKDIR /etc/ssh
USER root

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]