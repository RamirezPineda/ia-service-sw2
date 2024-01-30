# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

# WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt


# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# COPY . /app

# EXPOSE 80

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
