FROM python:2.7

RUN mkdir -p /home/project/P3
WORKDIR /home/project/P3
COPY requirements.txt /home/project/P3
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/P3
