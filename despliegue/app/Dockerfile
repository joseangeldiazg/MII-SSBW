FROM frolvlad/alpine-python3
# Reference https://docs.docker.com/engine/reference/builder/#label
LABEL maintainer "joseangeldiazg"

RUN apk update && apk upgrade \
    && apk add git supervisor gcc linux-headers python3-dev musl-dev freetype-dev libjpeg-turbo-dev lcms2-dev openjpeg-dev tiff-dev libwebp-dev libxml2-dev libxslt-dev zlib-dev \
    && pip install uwsgi  \
    && pip install requests  \
    && git clone https://github.com/joseangeldiazg/restaurapp /home/restaurapp  \
    && cd /home/restaurapp  && pip install -r requirements.txt  \
    && apk del git gcc linux-headers

EXPOSE 8000

COPY models.py /home/restaurapp/restaurantes/
COPY settings.py /home/restaurapp/sitio_web/
COPY app.ini /home/restaurapp/uwsgi/
COPY supervisord.conf /etc/

CMD ["supervisord", "-n"]
