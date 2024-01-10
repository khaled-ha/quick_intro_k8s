FROM python:3.10-alpine

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python", "app.py" ]
