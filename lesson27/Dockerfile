FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
#RUN pip install flask
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt
CMD ["make"]