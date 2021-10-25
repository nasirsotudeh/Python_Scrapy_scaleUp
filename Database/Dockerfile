FROM postgres:latest As PG_DB
# add the 'postgres' admin ENV POSTGRES_USER=nasir
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_USER=nasir
ENV POSTGRES_DB=RSS_DB
ENV LANG=en_US.utf8
COPY ./sql/*.sql /docker-entrypoint-initdb.d/
# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
