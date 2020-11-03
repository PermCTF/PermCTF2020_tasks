#!/bin/bash
docker build -t postfinal .
docker run -d -P --name srop-box postfinal
docker port srop-box 22
docker-machine ip
echo "creds -> stranger:Am1sTrAng@r"