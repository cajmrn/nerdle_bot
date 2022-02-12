########################################################################
# Dockerfile for Oracle JDK 8 on Ubuntu 16.04
########################################################################

# pull base image
FROM python:3.8.12

# Define the working directory
WORKDIR /nerdle_bot

# add a post-invoke hook to dpkg which deletes cached deb files
# update the sources.list
# update/dist-upgrade
# clear the caches
RUN  apt-get update && apt-get install -y --no-install-recommends wget unzip openjdk-11-jdk software-properties-common && apt-get clean

COPY requirements.txt .

RUN pip install -r requirements.txt

#ENTRYPOINT ["java", "-Xmx4g", "-jar", "/opt/h2o.jar"]
# Define default command

COPY src/ src/

COPY setup.py .

RUN pip install -e .