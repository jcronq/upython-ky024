import machine
import time

class Controller:
    reading_count = 10

    def __init__(self, ADC_PIN):
        self.adc = machine.ADC(machine.Pin(ADC_PIN))

    def get_value(self):
        readings = []
        for idx in range(self.reading_count):
            readings.append(self.adc.read_u16())
            time.sleep(0.1)
        return sum(readings) / self.reading_count
