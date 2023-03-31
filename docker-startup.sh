#!/bin/bash

nginx -g deamon off;
python -m flask --app ./app/backend/server.py run
