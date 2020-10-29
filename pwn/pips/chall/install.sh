#!/bin/bash -i

rm -rf arm_now
cp /arm_now . -a
e2rm ./arm_now/rootfs.ext2:/etc/inittab
e2cp -G 0 -O 0 -P 555 ./inittab ./arm_now/rootfs.ext2:/etc/inittab
#mipsel-linux-gnu-gcc main.c -o chall -z execstack  -fno-stack-protector
