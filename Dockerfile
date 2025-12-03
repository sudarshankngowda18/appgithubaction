# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

# Install build tools (needed for some Python packages with C extensions)
RUN apk add --no-cache gcc musl-dev libffi-dev

WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Install dependencies into a temporary folder
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Final runtime image
FROM python:3.11-alpine

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy only necessary application files
COPY . .

# Expose ports
EXPOSE 7860
EXPOSE 5000

# Default command
CMD ["python", "ui.py"]