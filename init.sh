#!/bin/sh

git config --global user.email "qingcaihome@yeah.net"
git config --global user.name "qingcaihome"

git remote add upstream https://github.com/louplus/jobplus9-2
git pull --rebase upstream master 

sudo pip install -r requirements.txt

export FLASK_APP=manage.py
export FLASK_DEBUG=1

sudo service mysql start

flask db init
flask db migrate -m 'init database'
flask db upgrade