# Use an official Python runtime as a parent image
FROM python:3.9.13

# Set the working directory in the container
WORKDIR /

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for Flask to run on port 80
ENV PORT 80

# Run the Flask app
CMD ["python", "app.py"]
