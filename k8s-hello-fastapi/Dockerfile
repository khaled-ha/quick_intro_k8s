FROM python:3.10-alpine

COPY . /src

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
