FROM ubuntu

COPY . /opt/mynotebook/

WORKDIR /opt/mynotebook/

RUN apt update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y libmysqlclient-dev

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/opt/mynotebook/

ENTRYPOINT ["python3", "app.py"]