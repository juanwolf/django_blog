FROM ubuntu:xenial

MAINTAINER Jean-Loup Adde "jean-loup.adde@juanwolf.fr"

# Change dash to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
RUN apt-get install -y python3-dev python3-setuptools python3-pip libtiff-dev \
libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl-dev tk-dev python3-tk \
libpq-dev uwsgi-plugin-python3 libpcre3 libpcre3-dev
RUN pip3 install virtualenv
RUN pip3 install uwsgi
RUN virtualenv /opt/virtualenvs/juanwolf_fr
RUN source /opt/virtualenvs/juanwolf_fr/bin/activate
ADD . /opt/juanwolf_fr
WORKDIR /opt/juanwolf_fr/juanwolf_fr

RUN /opt/virtualenvs/juanwolf_fr/bin/pip install -r /opt/juanwolf_fr/requirements.txt

EXPOSE 8000
CMD uwsgi --ini=/opt/juanwolf_fr/juanwolf.fr.ini --pidfile=/opt/juanwolf_fr/site.pid


