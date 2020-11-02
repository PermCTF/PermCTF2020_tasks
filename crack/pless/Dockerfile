FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# User pass
RUN useradd admin -m 
RUN echo 'admin:admin' | chpasswd

# Add pubkey
RUN mkdir /home/admin/.ssh
RUN echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDD6BYiNdv677AYEPku0Ox9Ol8hNiLYc5URRNAq5uIRPm9PgAkPOpBJB5wElRb2iT6Wape+0lVSabXi+g43PpSZyuKUzo8x5YQL8DcdYxyxt9Bi9YfrHUTc/UoGCrHTzfPO1s9Bf7geVVV/99NilYlItaKnIt3IyKAJuhyCcUvLJFIxtHWMRAR4ZCXcmJJq601KzyUxF2NwVsUOy63ieKM5dGbu5s7EGfPMJBzkBHRKvLnTDEcCbIot4+r0X1bPP90kpsVOT3lyh4tuQAc9rBoZUCFfKuBDkZLuzNGjCon0fN6YxWIj/5YHbmzfYsf3UREznm4T3XaI0bV4D6itziwJ ' > /home/admin/.ssh/authorized_keys

# Disable password auth
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

RUN echo 'PermCTF{who_needs_passwords_now}' > /home/admin/flag
RUN chmod a-w /home/admin

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

