#!/bin/sh

# Build the Docker image
docker build -t TG-Livegram-Bot .

# Run the Docker container with an interactive shell
docker run -it TG-Livegram-Bot /bin/sh
