FROM python:3.8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor cron

RUN pip3 install uwsgi

COPY conf/requirements.txt /root/requirements.txt
COPY app /app
RUN pip3 install -r /root/requirements.txt
RUN chmod +x /app/run.sh
RUN useradd --no-create-home nginx

RUN chown -R nginx: /app/*

RUN mkdir /etc/nginx/certs
COPY conf/certs /etc/nginx/certs
RUN rm -r /root/.cache
RUN rm /etc/nginx/sites-enabled/default
COPY conf/nginx/* /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/kitties.com.conf /etc/nginx/sites-enabled/kitties.com.conf
RUN ln -s /etc/nginx/sites-available/beta_dev.kitties.com.conf /etc/nginx/sites-enabled/beta_dev.kitties.com.conf
RUN ln -s /etc/nginx/sites-available/flag.kitties.com.conf /etc/nginx/sites-enabled/flag.kitties.com.conf
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
COPY conf/uwsgi/uwsgi_1.ini /app/kitties/
COPY conf/uwsgi/uwsgi_2.ini /app/kitties_beta/
COPY conf/supervisord.conf /etc/
COPY conf/mycron /tmp/
RUN crontab /tmp/mycron
RUN cd /app && python3 install.py ; python3 install2.py
WORKDIR /app
EXPOSE 443

CMD ["/app/run.sh"]
