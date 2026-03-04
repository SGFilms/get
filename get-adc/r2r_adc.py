import RPi.GPIO as GPIO, time as t

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False) -> None:
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.last_n = 0

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self) -> None:
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number) -> None:
        binary = [int(el) for el in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, binary)

    def sequential_counting_adc(self):
        n = -1
        while GPIO.input(self.comp_gpio) == 0:
            if n < 255:
                n += 1
                print(n)
                binary = [int(el) for el in bin(n)[2:].zfill(8)]
                GPIO.output(self.bits_gpio, binary)
                t.sleep(self.compare_time + 0.5)
            elif n >= 255:
                print("out of range")
                return

        return n

        
            
    def get_sc_voltage(self):
        self.sequential_counting_adc()
        return float( self.last_n / 255 * self.dynamic_range )

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.296)

        while True:
            print(adc.get_sc_voltage())

    finally:
        adc.deinit()