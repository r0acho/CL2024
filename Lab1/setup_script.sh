#!/bin/bash

apt update
apt upgrade -y
apt install wget python3 python3-pip python3-venv vim -y
apt install -y libsndfile1 ffmpeg
source ~/.bashrc
cd /home/user/lab1_files
python3 -m venv env
source env/bin/activate
pip3 install Cython nemo_toolkit['all'] fastapi uvicorn python-multipart requests
mkdir data && cd data
wget https://github.com/sberdevices/golos/raw/master/examples/data/001ce26c07c20eaa0d666b824c6c6924.wav
cd ../models && mkdir models && cd models
wget https://us.openslr.org/resources/114/QuartzNet15x5_golos.nemo.gz
gzip -dv QuartzNet15x5_golos.nemo.gz
cd ../src/examples && mkdir -p src/examples && cd src/examples
wget https://raw.githubusercontent.com/sberdevices/golos/master/examples/infer.py
cd ../../
