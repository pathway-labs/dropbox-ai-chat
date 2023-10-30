# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt
# Install any dependencies
RUN pip install --upgrade -r requirements.txt
# Copy the content of the local repo
COPY . .