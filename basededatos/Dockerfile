FROM alpine:latest

COPY co-co.sql /docker-entrypoint-initdb.d/

ARG HOST

ARG USER

ARG DB_PASSWORD

CMD ["sh", "-c", "apk add --no-cache mysql-client && mysql -h $HOST -u $USER -p$PASSWORD < /docker-entrypoint-initdb.d/co-co.sql"]