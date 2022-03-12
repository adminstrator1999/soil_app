FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
ADD . /soil_app
WORKDIR /soil_app
EXPOSE 8000
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client zlib-dev jpeg-dev gcc && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /opt/venv/bin/pip install -r requirements.txt && \
    apk del .tmp-deps && \
    chmod +x entrypoint.sh && \
    chmod +x migrate.sh && \
    adduser --disabled-password --no-create-home soil_app_user && \
    mkdir -p /volume/web/static && \
    mkdir -p /volume/web/media && \
    chown -R soil_app_user:soil_app_user /volume && \
    chmod -R 755 /volume

ENV PATH="/opt/venv/bin:$PATH"
USER soil_app_user

