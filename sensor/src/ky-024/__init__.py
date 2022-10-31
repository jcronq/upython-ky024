from machine import ADC

class Controller:
    def __init__(self, ADC_PIN):
        adc = ADC(ADC_PIN)

    def get_value():
        return adc.read_uv()
