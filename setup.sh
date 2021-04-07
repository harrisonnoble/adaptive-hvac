#!/bin/bash

# update/upgrade installed packages and distribution
sudo apt update -y
sudo apt upgrade
sudo apt dist-upgrade

# install the general purpose I/O and camera v2 python library
sudo apt install python3-gpiozero -y
sudo apt install python-picamera -y
sudo pip3 install numpy
sudo apt install python3-opencv
sudo apt-get install -y libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev  libqtgui4  libqt4-test
sudo apt-get install python3-pil.imagetk
sudo pip3 install adafruit-circuitpython-amg88xx
