FROM python:3.10.7-slim

LABEL author='Kirill Yasnov'

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "cloudpass.wsgi:application", "--bind", "0.0.0.0:8000"]
