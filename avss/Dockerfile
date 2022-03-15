# Base target:
# All used targets should be based off of this target, and as such, changes to this 
# should be kept to an absolute minimum, as it causes the longest builds.
# This should contain all setup required by all other targets, such as environment
# variables, and essential apt dependencies.
##


FROM python:3.7-slim AS base

# Install apt dependencies
# Put apt dependencies here that are needed by all build paths
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    git \
    bison \
    flex \ 
    python3-dev \
    python3-pip \
    libgmp-dev \
    libmpc-dev \
    libssl-dev \
    sudo \
    wget

WORKDIR /
RUN wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
RUN tar -xvf pbc-0.5.14.tar.gz
WORKDIR /pbc-0.5.14
RUN sudo ./configure
RUN sudo make
RUN sudo make install

WORKDIR /

RUN sudo ldconfig /usr/local/lib


ENV PYTHONUNBUFFERED 1 

# Path variables needed for Charm
ENV LIBRARY_PATH /usr/local/lib
ENV LD_LIBRARY_PATH /usr/local/lib

WORKDIR /
RUN git clone https://github.com/JHUISI/charm.git 
WORKDIR /charm
RUN ./configure.sh
RUN make
RUN make install 

WORKDIR /

RUN python3 -m pip install --upgrade pip
RUN pip install \
    gevent \
    setuptools \
    numpy \
    ecdsa \
    pysocks \
    gmpy2 \
    zfec \
    gipc \
    pycrypto \
    pytest \
    coincurve
  
RUN apt-get install -y --no-install-recommends \
    tmux \
    vim

WORKDIR /usr/src/avss/

# RUN pip install debugpy
# ENTRYPOINT [ "python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m"]


