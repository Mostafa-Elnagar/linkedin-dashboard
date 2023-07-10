FROM python:3.9.16-slim-buster

LABEL maintainer "Mostafa Elnagar"

# set working directory in container
WORKDIR /usr/src/app

# Copy and install packages
COPY requirements.txt /
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN pip install gunicorn
# Copy app folder to app folder in container
# Set the working directory inside the container

# Copy the project files into the container
COPY app.py index.py requirements.txt ./

# Copy the directories into the container
COPY assets/ ./assets
COPY data/ ./data
COPY graphics/ ./graphics
COPY pages/ ./pages
COPY utils/ ./utils
# Changing to non-root user
RUN useradd -m appUser
USER appUser

# Run locally on port 8050
CMD gunicorn --bind 0.0.0.0:8050 index:server
