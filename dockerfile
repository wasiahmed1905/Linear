# Use lightweight Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency definition and install requirements
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy application logic into container
COPY app.py .

# Expose API port 5000
EXPOSE 5000

# Execute the Flask application
CMD ["python", "app.py"]
