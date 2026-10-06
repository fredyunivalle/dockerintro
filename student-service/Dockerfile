# syntax=docker/dockerfile:1.7
FROM python:3.11-slim

# Create non-root user for security
RUN groupadd --system app && useradd --system --gid app app

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create logs directory and set permissions
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

# Switch to non-root user
USER app

# Expose application port
EXPOSE 8080

# Healthcheck definition
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health', timeout=2)"

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]