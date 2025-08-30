# Stage 1: Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Environment variables
ENV THREADS_API_KEY=""
ENV OPENAI_API_KEY=""

# Run the application
CMD ["python", "main.py"]
