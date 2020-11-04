export PATH="$PATH:/opt/bin:/opt/sbin"

cd /root
opkg update
opkg install ncat
#echo 0 > /proc/sys/kernel/randomize_va_space
adduser -D -g "" user
#useradd -ms /bin/bash user
chmod 000 *
chmod +rx ./chall .
chmod +r flag
ncat -k -l -p 4242 -c "su user -c ./chall"
