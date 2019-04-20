#!/bin/bash

yum install -y git pip nginx
pip install virtualenv supervisor
if [ ! -d "venv" ]; then
    virtualenv venv --system-site-packages
fi
venv/bin/pip install -r requirements.txt

if [ ! -f "/etc/nginx/nginx.conf.bak" ]; then
    cp -f /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
fi

if [ ! -d "/etc/supervisor" ]; then
    mkdir -m 755 -p /etc/supervisor
fi

if [ ! -f "../mongodb-linux-x86_64-rhel70-3.6.0.tgz" ]; then
    echo "ERROR"
fi

if [ ! -d "../mongodb" ]; then
    tar -zxvf ../mongodb-linux-x86_64-rhel70-3.6.0.tgz -C ..
    mv ../mongodb-linux-x86_64-rhel70-3.6.0 ../mongodb
    mkdir -m 755 -p ../mongodb/data
fi

cp -f conf/nginx.conf /etc/nginx/nginx.conf
cp -f conf/supervisord.conf /etc/supervisor/supervisord.conf
cp -f conf/mongo.conf ../mongodb/bin/mongo.conf

../mongodb/bin/mongod --config ../mongodb/bin/mongo.conf &
nginx
supervisord -c /etc/supervisor/supervisord.conf

#ver="5.7"
#tag="5.7.19-1.el7"

#wget https://cdn.mysql.com//Downloads/MySQL-$ver/mysql-$tag.x86_64.rpm-bundle.tar
#wget ftp://195.220.108.108/linux/centos/7.4.1708/os/x86_64/Packages/libaio-0.3.109-13.el7.x86_64.rpm

#tar -xvf mysql-$tag.x86_64.rpm-bundle.tar
#rpm -ivh libaio-0.3.109-13.el7.x86_64.rpm
#rpm -ivh mysql-community-common-$tag.x86_64.rpm
#rpm -ivh mysql-community-libs-$tag.x86_64.rpm
#rpm -ivh mysql-community-client-$tag.x86_64.rpm
#rpm -ivh mysql-community-server-$tag.x86_64.rpm
#rpm -ivh mysql-community-devel-$tag.x86_64.rpm
#rpm -ivh mysql-community-libs-compat-$tag.x86_64.rpm

#cp -f my.cnf /etc/my.cnf
