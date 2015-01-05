#!/bin/bash -e
wget -c 'http://download.brother.com/welcome/dlfp002174/ql570lpr-1.0.1-0.i386.deb'
wget -c 'http://download.brother.com/welcome/dlfp002176/ql570cupswrapper-1.0.1-0.i386.deb'

sudo apt-get update
#sudo apt-get dist-upgrade

sudo apt-get install cups
sudo apt-get install gcc-4.7-multilib psutils

sudo mkdir -p /var/spool/lpd
sudo dpkg -i ql570lpr-1.0.1-0.i386.deb
sudo dpkg -i ql570cupswrapper-1.0.1-0.i386.deb

# Remote admin
sudo cupsctl --remote-admin
sudo lppasswd -a $USER

exit 0
