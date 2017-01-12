FROM python:3.5-alpine

ENV DEBUG=False

ADD . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-binary --no-use-wheel --no-cache-dir --disable-pip-version-check -r ./requirements.txt

EXPOSE 7766

CMD ["python", "api.py"]