FROM python:3.12

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

COPY . /app

CMD []