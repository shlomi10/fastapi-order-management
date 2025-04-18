# Use an official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements if you have it
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your entire app code
COPY . .

# Expose port (FastAPI runs on 8000 by default)
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
