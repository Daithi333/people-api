#!/bin/bash
echo "Creating Virtual Env"
pip install virtualenv
virtualenv env
source env/Scripts/activate
pip install -r requirements.txt
pip install -r tests/requirements.txt