#!/bin/bash

# update/upgrade installed packages and distribution
sudo apt update -y
sudo apt upgrade
sudo apt dist-upgrade

# install the general purpose I/O and camera v2 python library
sudo apt install python3-gpiozero -y
sudo apt install python-picamera -y
sudo pip3 install numpy
sudo pip3 install opencv-contrib-python
