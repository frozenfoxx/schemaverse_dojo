# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
WORKDIR /app
ENV APPDIR="/app"

# Add requirements
COPY requirements.txt ./
RUN \
  python3 -m pip install -r requirements.txt --no-cache-dir

# Copy app source
COPY . .

# Launch
ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]
