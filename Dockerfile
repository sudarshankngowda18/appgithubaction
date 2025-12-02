# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port if your app runs a web server (optional)
EXPOSE 7860
EXPOSE 5000

# Default command to run your app
CMD ["python", "ui.py"]