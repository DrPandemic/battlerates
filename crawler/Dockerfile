FROM python:3

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY app.py ./
COPY src/ ./src/

CMD ["python", "app.py"]
