FROM alpine:latest

COPY co-co.sql /docker-entrypoint-initdb.d/

ARG HOST=database-1.c9yjy3nmd8az.us-east-1.rds.amazonaws.com
ENV HOST=$HOST

ARG USER=proyectocoandco
ENV USER=$USER

ARG PASSWORD=hola1234
ENV PASSWORD=$PASSWORD

CMD ["sh", "-c", "apk add --no-cache mysql-client && mysql -h $HOST -u $USER -p$PASSWORD < /docker-entrypoint-initdb.d/co-co.sql"]