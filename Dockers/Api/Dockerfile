#Django Dockerization for IOGYM app
#Made by Sergio Antonio Becerra Cobian 26/08/2020
#made for docker 19.03
FROM python:3
WORKDIR /App
COPY requirements.txt /App
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONUNBUFFERED 1
