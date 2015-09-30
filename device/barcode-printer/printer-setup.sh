#!/bin/bash -e
echo ' * Getting drivers for QL-570...'
wget -c 'http://download.brother.com/welcome/dlfp002174/ql570lpr-1.0.1-0.i386.deb'
wget -c 'http://download.brother.com/welcome/dlfp002176/ql570cupswrapper-1.0.1-0.i386.deb'

echo ' * Preparing system...'
sudo dpkg --add-architecture i386
sudo apt-get update
#sudo apt-get dist-upgrade
sudo apt-get install cups
sudo apt-get install gcc-4.7-multilib psutils

echo ' * Installing drivers for QL-570...'
sudo mkdir -p /var/spool/lpd
sudo dpkg -i ql570lpr-1.0.1-0.i386.deb
sudo dpkg -i ql570cupswrapper-1.0.1-0.i386.deb

echo ' * Configuring remote CUSP admin...'
sudo cupsctl --remote-admin
echo "Enter password of user $USER"
sudo lppasswd -a $USER

echo 'Done'
exit 0
