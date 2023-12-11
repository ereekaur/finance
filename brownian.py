import math
import os
import matplotlib.pyplot as plt
from scipy.stats import shapiro, kstest, anderson
from datetime import datetime, timedelta

"""""

This calculator takes .txt stock data and calculates how much it deviate from so called
Brownian motion.

You can exclude certain timeline  and you can insert how long timeline you are interested in examining.


"""""
def calculate_log_differences(data):
    log_differences = []

    for i in range(1, len(data)):
        yesterday_close = data[i - 1][-2]
        today_close = data[i][-2]
        log_difference = math.log(today_close) - math.log(yesterday_close)
        log_differences.append(log_difference)

    return log_differences



# read data from file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'shiba.txt')  
with open(file_path, 'r') as file:
    lines = file.readlines()
data = [list(map(float, line.strip().split(',')[1:-1])) for line in lines[1:]]
dates = [datetime.strptime(line.strip().split(',')[0], '%Y-%m-%d') for line in lines[1:]]
window_size = timedelta(days=70)  



# exclude
exclude_periods = [
    (datetime(2022, 1, 1), datetime(2022, 2, 1)),  
   
]

max_statistic_sw = float('-inf')
min_statistic_sw = float('inf')
max_statistic_ks = float('-inf')
min_statistic_ks = float('inf')
max_statistic_ad = float('-inf')
min_statistic_ad = float('inf')
most_normal_period_sw = None
least_normal_period_sw = None
most_normal_period_ks = None
least_normal_period_ks = None
most_normal_period_ad = None
least_normal_period_ad = None

for i in range(len(data) - window_size.days + 1):
    window_data = data[i:i + window_size.days]
    window_dates = dates[i:i + window_size.days]
    excluded = any(
        (start <= window_dates[0] <= end or start <= window_dates[-1] <= end) for start, end in exclude_periods
    )

    if excluded:
        continue  
   
    log_differences = calculate_log_differences(window_data)
    
    # Shapiro-Wilk 
    stat_sw, p_value_sw = shapiro(log_differences)

    # Kolmogorov-Smirnov 
    stat_ks, p_value_ks = kstest(log_differences, 'norm')

    # Anderson-Darling test
    stat_ad, p_value_ad, _ = anderson(log_differences, dist='norm')

    if stat_sw > max_statistic_sw:
        max_statistic_sw = stat_sw
        most_normal_period_sw = (window_dates[0], window_dates[-1])
        p_value_most_sw = p_value_sw
    if stat_sw < min_statistic_sw:
        min_statistic_sw = stat_sw
        least_normal_period_sw = (window_dates[0], window_dates[-1])
        p_value_least_sw = p_value_sw

    if stat_ks > max_statistic_ks:
        max_statistic_ks = stat_ks
        most_normal_period_ks = (window_dates[0], window_dates[-1])
        p_value_most_ks = p_value_ks
    if stat_ks < min_statistic_ks:
        min_statistic_ks = stat_ks
        least_normal_period_ks = (window_dates[0], window_dates[-1])
        p_value_least_ks = p_value_ks

    if stat_ad > max_statistic_ad:
        max_statistic_ad = stat_ad
        most_normal_period_ad = (window_dates[0], window_dates[-1])
        p_value_most_ad = p_value_ad
    if stat_ad < min_statistic_ad:
        min_statistic_ad = stat_ad
        least_normal_period_ad = (window_dates[0], window_dates[-1])
        p_value_least_ad = p_value_ad


# plot histograms

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(calculate_log_differences(data[dates.index(least_normal_period_sw[0]):dates.index(least_normal_period_sw[1]) + 1]),
         bins=20, color='blue', alpha=0.5, edgecolor='black', label='Least Normal Period (Shapiro-Wilk)')
plt.title(f'Shapiro-Wilk Test\nLogarithm Differences Histogram\n{least_normal_period_sw[0].strftime("%Y-%m-%d")} to {least_normal_period_sw[1].strftime("%Y-%m-%d")}\np-value: {p_value_least_sw:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(calculate_log_differences(data[dates.index(most_normal_period_sw[0]):dates.index(most_normal_period_sw[1]) + 1]),
         bins=20, color='green', alpha=0.5, edgecolor='black', label='Most Normal Period (Shapiro-Wilk)')
plt.title(f'Shapiro-Wilk Test\nLogarithm Differences Histogram\n{most_normal_period_sw[0].strftime("%Y-%m-%d")} to {most_normal_period_sw[1].strftime("%Y-%m-%d")}\np-value: {p_value_most_sw:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(calculate_log_differences(data[dates.index(least_normal_period_ks[0]):dates.index(least_normal_period_ks[1]) + 1]),
         bins=20, color='blue', alpha=0.5, edgecolor='black', label='Least Normal Period (Kolmogorov-Smirnov)')
plt.title(f'Kolmogorov-Smirnov Test\nLogarithm Differences Histogram\n{least_normal_period_ks[0].strftime("%Y-%m-%d")} to {least_normal_period_ks[1].strftime("%Y-%m-%d")}\np-value: {p_value_least_ks:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(calculate_log_differences(data[dates.index(most_normal_period_ks[0]):dates.index(most_normal_period_ks[1]) + 1]),
         bins=20, color='green', alpha=0.5, edgecolor='black', label='Most Normal Period (Kolmogorov-Smirnov)')
plt.title(f'Kolmogorov-Smirnov Test\nLogarithm Differences Histogram\n{most_normal_period_ks[0].strftime("%Y-%m-%d")} to {most_normal_period_ks[1].strftime("%Y-%m-%d")}\np-value: {p_value_most_ks:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()




plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(calculate_log_differences(data[dates.index(least_normal_period_ad[0]):dates.index(least_normal_period_ad[1]) + 1]),
         bins=20, color='blue', alpha=0.5, edgecolor='black', label='Least Normal Period (Anderson-Darling)')
plt.title(f'Anderson-Darling Test\nLogarithm Differences Histogram\n{least_normal_period_ad[0].strftime("%Y-%m-%d")} to {least_normal_period_ad[1].strftime("%Y-%m-%d")}\np-value: {p_value_least_ad:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(calculate_log_differences(data[dates.index(most_normal_period_ad[0]):dates.index(most_normal_period_ad[1]) + 1]),
         bins=20, color='green', alpha=0.5, edgecolor='black', label='Most Normal Period (Anderson-Darling)')
plt.title(f'Anderson-Darling Test\nLogarithm Differences Histogram\n{most_normal_period_ad[0].strftime("%Y-%m-%d")} to {most_normal_period_ad[1].strftime("%Y-%m-%d")}\np-value: {p_value_most_ad:.4f}')
plt.xlabel('Logarithm Differences')
plt.ylabel('Frequency')
plt.legend()

plt.tight_layout()
plt.show()
