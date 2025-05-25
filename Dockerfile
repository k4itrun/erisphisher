FROM python:3.13-alpine

LABEL maintainer="k4itrun <tsx@billoneta.xyz>"

WORKDIR /app

COPY . .

RUN apk update && \
    apk add --no-cache \
        bash \
        php \
        curl \
        wget \
        unzip

CMD ["bash", "eris.sh"]
