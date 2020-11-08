#!/bin/bash
/bin/chown nginx: /app/kitties/db.sqlite
/usr/sbin/service nginx start
/usr/sbin/cron
/usr/bin/supervisord
