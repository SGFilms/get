import mcp4725_driver
import signal_generator as sg

amplitude = 3
signal_frequency = 10
sampling_frequency = 2000

dt = 1.0 / sampling_frequency
t = 0.0

if __name__ == '__main__':
    dac = mcp4725_driver.MCP4725(dynamic_range = 5.04, verbose = True)
    try:

        while True:
            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
            dac.set_voltage(norm_amp * amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
            t += dt


    finally:
        dac.deinit()
