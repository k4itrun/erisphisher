# Dockerfile

# Author       : k4itrun
# Github       : https://github.com/k4itrun
# Github       : https://github.com/k4itrun
# Contact      : https://m.me/k4itrun
# Discord      : https://6889.fun/k4itrun
# Email        : k4itrun@6889.fun
# Date         : 11-10-2023
# Main Language: Python

# Download and import main images

# The `FROM debian:10` line in the Dockerfile is specifying the base image for the Docker container. It is pulling the official Debian 10 image from the Docker Hub registry. This base image provides a pre-configured environment with the Debian 10 operating system installed. It serves as the starting point for building the Docker image for the application.
FROM debian:10
# The `FROM python:3` line in the Dockerfile is specifying the base image for the Docker container. It is pulling the official Python 3 image from the Docker Hub registry. This base image provides a pre-configured environment with Python 3 installed, allowing you to run Python applications inside the Docker container.
FROM python:3

# The `LABEL MAINTAINER="https://github.com/k4itrun/erisphisher"` line in the Dockerfile is used to specify the maintainer of the Docker image. It provides contact information for the person responsible for maintaining the image. In this case, the maintainer is specified as the GitHub profile of the user "k4itrun" who is the author of the "erisphisher" project.
LABEL MAINTAINER="https://github.com/k4itrun/erisphisher"

# The `WORKDIR erisphisher/` command sets the working directory inside the Docker container to `/erisphisher/`. This means that any subsequent commands or actions will be performed relative to this directory. It is similar to using the `cd` command in a terminal to change the current directory.
WORKDIR erisphisher/
# The `ADD . /erisphisher` command is adding all the files and directories from the current directory (denoted by `.`) to the `/erisphisher` directory inside the Docker container.
ADD . /erisphisher

# The `RUN apt-get update` command updates the package lists for upgrades and new package installations.
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN apt-get install --no-install-recommends -y php
RUN apt-get install -y unzip
RUN apt-get clean

# The `CMD ["python3", "erisphisher.py"]` command is specifying the default command to be executed when the Docker container starts. In this case, it is running the `erisphisher.py` Python script using the `python3` interpreter.
CMD ["python3", "erisphisher.py"]
## "cd erisphisher", "docker build . -t erisphisher:1.0", "docker run --rm -it erisphisher:1.0"