#!/home/cronqj/.bin/miniconda3/envs/rgb_sensor/bin/python

import requests
import time

sample_count = 10

while True:
    response = requests.get("http://10.20.30.139:8008/hall_voltage")
    print(response.text)
    time.sleep(0.1)

        
