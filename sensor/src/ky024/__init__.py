import machine

class Controller:
    def __init__(self, ADC_PIN):
        self.adc = machine.ADC(machine.Pin(ADC_PIN))

    def get_value(self):
        return self.adc.read_u16()
