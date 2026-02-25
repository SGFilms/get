import numpy as np, time as t

def get_sin_wave_amplitude(freq, time) -> float:
    return (np.sin(2 * np.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    t.sleep(1.0 / sampling_frequency)
    