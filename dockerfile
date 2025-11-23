# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Change directory to /app/examples/v201 where server.py is located
WORKDIR /app/examples/v201

# Expose port 9000
EXPOSE 9000
# EXPOSE 8080

# Run server.py when the container launches
CMD ["python", "central_system.py"]