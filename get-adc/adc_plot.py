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

def plot_sampling_period_hist(time):
    periods = []
    for i in range(len(time)-1):
        periods.append(time[i+1] - time[i])

    plt.figure(figsize=(10, 6))
    plt.hist(periods)
    plt.ylabel('Frequency')
    plt.xlabel('Period, s')
    plt.xlim(0, 0.06)
    plt.grid()
    plt.show()