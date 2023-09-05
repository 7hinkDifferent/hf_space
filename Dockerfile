# Dockerfile
FROM python
LABEL author="7hinkDifferent"

# Necessary setup and installation
RUN apt-get update && \
    apt-get install -y nginx vim

# Workspace
WORKDIR /home
COPY api ./api
COPY templates ./templates
RUN python3 templates/main.py --type server && \
    pip3 install -r templates/requirements.txt && \
    pip3 install -r api/requirements.txt 

# CMD