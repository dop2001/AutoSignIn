#!/bin/bash

# git clone repository from GitHub
git clone git@github.com:dop2001/Action.git
cd Action

# get current path
CurrentPath=$(pwd)

# Download file path
EdgeURL=https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_120.0.2210.133-1_amd64.deb?brand=M102
DriverURL=https://msedgedriver.azureedge.net/120.0.2210.133/edgedriver_linux64.zip

# download and install Edge web browser
wget -c $EdgeURL -O Edge.deb
sudo dpkg -i Edge.deb

if [ $? -ne 0 ]; then
    echo "Edge install fail!"
    exit 1
fi

# download and install Edge driver



echo $CurrentPath