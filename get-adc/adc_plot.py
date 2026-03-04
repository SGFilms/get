import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)

    plt.ylim(0, 3.3)
    plt.xlim(0, 10)
    plt.ylabel('Voltage, V')

    plt.xlabel('Time, s')

    plt.grid()

    plt.show()