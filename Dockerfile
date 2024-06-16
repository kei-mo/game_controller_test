FROM python:3.10-slim

WORKDIR /tmp
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
		vim \
		cmake \
		build-essential \
		curl \
		wget \
		gnupg2 \
		lsb-release \
		ca-certificates \ 
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# install opencv dependecies
RUN apt-get update && apt-get install -y \
      libsm6 libxext6  libgl1 &&\
    rm -rf /var/lib/apt/lists/*

#
# install python packages 
#
COPY requirements.txt ${PWD}
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	python3-pip  \
    && python3 -m pip install --upgrade --no-cache-dir -U pip\
    && python3 -m pip install --no-cache-dir -r requirements.txt 

WORKDIR /workspace
COPY . /workspace
