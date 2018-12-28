#!/bin/sh

sudo pip install -r requirements.txt

export FLASK_APP=app.py
export FLASK_DEBUG=1

