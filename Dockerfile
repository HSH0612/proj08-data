# Use official Python 3.10 slim image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy your batch pipeline script into container
COPY batch_pipeline.py /app/

# Install pandas + pyarrow
RUN pip install --no-cache-dir pandas pyarrow

# Default command (optional)
CMD ["python3", "/app/batch_pipeline.py"]
