FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt \
RUM playwright install
COPY . .
CMD ["pytest"]
