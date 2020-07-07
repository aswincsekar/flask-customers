FROM tiangolo/meinheld-gunicorn-flask:python3.7

RUN pip install --upgrade pip

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt