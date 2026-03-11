import mcp3021_driver, adc_plot, time

adc = mcp3021_driver.MCP3021(5.2)

voltage_values = []
time_values = []
duration = 10

try:
    t_start = time.time()

    while (time.time() - t_start) < duration:
        voltage_values.append(adc.get_voltage())
        time_values.append(time.time() - t_start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
    del adc