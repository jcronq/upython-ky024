#!/bin/bash
#--data-binary $file_reference \
host="$1"
name="status"
curl \
    --request GET \
    http://$host:8008/$name
echo ""
