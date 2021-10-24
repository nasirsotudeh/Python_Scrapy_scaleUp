# set base image (host OS)
FROM python:3.8 As pythonApp
# set the working directory in the container
# copy the content of the local src directory to the working directory
COPY /app/*.py /app/
WORKDIR /app/
# copy the dependencies file to the working directory
RUN apt-get update && apt-get install python3
COPY requirements.txt .
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
# command to run on container start

