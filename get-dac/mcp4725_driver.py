import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("Invalid input.")

        if not (0 <= number <= 4095):
            print("Input out of 12-bit range.")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Value: {number}. Data sent via I2C: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self, voltage):
        if not isinstance(voltage, (int, float)):
            print("Invalid input.")
        if voltage < 0 or voltage > self.dynamic_range:
            print(f"Input out of range [0, 3.153].")
        number = int(round(voltage / self.dynamic_range * 4095))
        self.set_number(number)

if __name__ == "__main__":
    dac = MCP4725(dynamic_range = 5.04, verbose = True)

    try:
        while True:
            try:
                voltage = float(input('Enter voltage: '))
                dac.set_voltage(voltage)
            except ValueError:
                print('Invalid.\n')
    finally:
        dac.deinit()

