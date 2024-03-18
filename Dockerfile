# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for unstructured
RUN apt-get update \
    && apt-get install -y python3-opencv \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install -U --no-cache-dir -r requirements.txt
# Copy the content of the local repo
COPY . .