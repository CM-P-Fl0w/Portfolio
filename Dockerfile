FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY . /app
WORKDIR /app

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
