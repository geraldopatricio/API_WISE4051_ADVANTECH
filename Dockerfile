FROM python:3.10-alpine3.15
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add \
    curl gcc g++ gnupg unixodbc-dev \
    unixodbc-dev libffi-dev && \
    curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.8.1.1-1_amd64.apk && \
    curl -O https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.8.1.1-1_amd64.apk && \
    apk add --allow-untrusted msodbcsql17_17.8.1.1-1_amd64.apk && \
    apk add --allow-untrusted mssql-tools_17.8.1.1-1_amd64.apk && \
    apk update && \
    pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]