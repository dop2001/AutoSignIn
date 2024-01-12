#!/bin/bash

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
mkdir driver && cd driver
wget -c $DriverURL -O Driver.zip
unzip Driver.zip
cd ../

if [ $? -ne 0 ]; then
    echo "Driver install fail!"
    exit 1
fi


echo $CurrentPath

ls -al ./driver
