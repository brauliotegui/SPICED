# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
ADD requirements.txt /app

COPY requirements.txt /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD get_tweets.py /app
ADD credentials.py /app

# Run get_tweets.py when the container launches
CMD ["python", "get_tweets.py"]
