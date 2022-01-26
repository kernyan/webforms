#! /bin/bash

export FLASK_APP=webpy
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=8080
