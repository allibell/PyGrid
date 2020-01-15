FROM python:3.7-slim
ARG PREINSTALL_TORCH
RUN apt-get update
RUN apt-get install -y git python3-pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN ${PREINSTALL_TORCH}
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["sh", "entrypoint.sh"]
