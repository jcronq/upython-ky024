#!/home/cronqj/.bin/miniconda3/envs/rgb_sensor/bin/python

import requests
import time

sample_count = 10

while True:
    readings = []
    for idx in range(sample_count):
        response = requests.get("http://10.20.30.139:8008/hall_voltage")
        time.sleep(0.1)
        readings.append(int(response.text))
    print(sum(readings)/sample_count)

        
