FROM python:3.7-alpine

# Install all build dependencies
# Add bash for debugging purposes
RUN apk update \
    && apk add --virtual build-dependencies \
        build-base \
        gcc \
        wget \
        git \
    && apk add \
        bash
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

VOLUME /yaci

ENV PYTHONPATH /yaci

CMD /bin/bash
