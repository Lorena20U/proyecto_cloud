FROM alpine:latest

COPY co-co.sql /docker-entrypoint-initdb.d/

CMD ["sh", "-c", "apk add --no-cache mysql-client && mysql -h database-1.c9yjy3nmd8az.us-east-1.rds.amazonaws.com -u proyectocoandco -phola1234 < /docker-entrypoint-initdb.d/co-co.sql"]