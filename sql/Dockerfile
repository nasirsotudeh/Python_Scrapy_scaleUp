FROM postgres:latest As PG_DB
# add the 'postgres' admin role
# expose Postgres port
EXPOSE 5431
ENV POSTGRES_USER=nasir
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_DB=web_links
ENV LANG=en_US.utf8
COPY *.sql /docker-entrypoint-initdb.d/
# bind mount Postgres volumes for persistent data
#VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
