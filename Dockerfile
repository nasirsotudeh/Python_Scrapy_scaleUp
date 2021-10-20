# set base image (host OS)
FROM python:3.8 As pythonApp
# set the working directory in the container
# copy the content of the local src directory to the working directory
COPY /app/*.py /app/
WORKDIR /app/
# copy the dependencies file to the working directory
RUN apt-get update && apt-get install -y python3 python3-pip
COPY requirements.txt .
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
# command to run on container start
FROM postgres:latest As PG_DB
# add the 'postgres' admin role
# expose Postgres port
EXPOSE 5440
USER postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=source_links
ENV LANG=en_US.utf8
COPY /sql/*.sql /docker-entrypoint-initdb.d/
# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]