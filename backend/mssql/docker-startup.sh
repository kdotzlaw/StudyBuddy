#!/bin/bash

nginx -g deamon off;
python3 -m flask --app ./app/backend/server.py run