import r2r_adc, time, adc_plot

adc = r2r_adc.R2R_ADC(3.175, compare_time = 0.0001)

voltage_values = []
time_values = []
duration = 10

try:
    t_start = time.time()

    while (time.time() - t_start) < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - t_start)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()
    del adc