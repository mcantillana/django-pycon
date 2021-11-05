FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --update \
    python3 \
    python3-dev \
    gcc \
    py-pip \
    build-base \
    mariadb-dev \
    wget \
    libxslt-dev \
    xmlsec-dev \
    # Pillow dependencies
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 8000
CMD gunicorn -b 0:8000 main.wsgi
