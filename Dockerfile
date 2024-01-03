# PostGIS
FROM postgis/postgis:latest

ENV POSTGRES_DB=apirestflask
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=1234

RUN mkdir -p /etc/postgresql/12/main/ && echo "host    all    all    0.0.0.0/0    md5" >> /etc/postgresql/12/main/pg_hba.conf

