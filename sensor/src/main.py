# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:00:35 2022

@author: Jason Cronquist
"""
import machine
from src.ky024 import Controller
from src.lite_server.web_server import WebServer
from micropython import const

ADC_PIN = const(4)

def start_webserver(sensor):
    server = WebServer(enable_web_dav=True)

    @server.GET("/hall_voltage")
    def get_voltage():
        return sensor.get_value()

    server.start_listening()

def connect(cb):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('blah', 'blahblah')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    cb()

def run():
    print("hello world")
    sensor = Controller(ADC_PIN)
    print("sensor initialized")
    cb = lambda: start_webserver(sensor)
    connect(cb)
