#!/usr/bin/env bash
sudo pip install awscli -i https://pypi.douban.com/simple

if [ ! -d ~/.aws ]; then
  mkdir ~/.aws
fi

if [ ! -f ~/.aws/config ]; then
  cp config ~/.aws/config
fi

if [ ! -f ~/.aws/credentials ]; then
  cp credentials ~/.aws/credentials
fi

sudo cp s3-upload /usr/local/bin/
