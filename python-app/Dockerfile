# Use the official Python image
FROM python:3.8-slim

# Install wget
RUN apt-get update && apt-get install -y wget

# Create and change to the app directory
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run the application
CMD [ "python", "client.py" ]
