FROM python:3.9-slim-buster
RUN apt update -y  &&  apt upgrade -y && apt-get update 
WORKDIR /app
COPY app.py requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["streamlit","run","app.py"]