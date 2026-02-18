import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pins = [22, 27, 17, 26, 25, 21, 20, 16][::-1]

GPIO.setup(pins, GPIO.OUT)

dynamic_range = 3.3

def voltage_to_number(voltage) -> int:
    if not (0.0 <= voltage <= dynamic_range):
        print(f'Voltage out of DAC range (0.00 - {dynamic_range:.2f} V)')
        print('Setting 0 Volts')
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number) -> None:
    binary = [int(el) for el in bin(number)[2:].zfill(8)]
    GPIO.output(pins, binary)

try:
    while True:
        try:
            voltage = float(input('Enter voltage: '))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print('Invalid input. Try again.\n')

finally:
    GPIO.output(pins, 0)
    GPIO.cleanup()