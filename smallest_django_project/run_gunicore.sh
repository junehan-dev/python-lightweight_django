#!/bin/sh
echo ""> ./log.txt
source ../venv/bin/activate
gunicorn wsgi_app:application --log-file=./log.txt
