import pwm_dac, signal_generator as sg

amplitude = 3
signal_frequency = 10
sampling_frequency = 1000

dt = 1.0 / sampling_frequency
t = 0.0

if __name__ == '__main__':
    dac = pwm_dac.PWM_DAC(12, 20000, 3.153, True)
    try:

        while True:
            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, t)
            dac.set_voltage(norm_amp * amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
            t += dt


    finally:
        dac.deinit()