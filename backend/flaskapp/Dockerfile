# Dockerfile for Flask application
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Run Flask server
CMD ["flask", "run", "--host=0.0.0.0"]