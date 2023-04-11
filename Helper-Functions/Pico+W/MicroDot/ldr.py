import machine
 
class LDR:
    def __init__(self, pin):
        self.ldr_pin = machine.ADC(machine.Pin(pin))
        
    def raw(self):
        return self.ldr_pin.read_u16()
    
    def percent(self):
        return round(self.raw()/65535*100,2)
    


 