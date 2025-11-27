import numpy as np
from scipy.stats import mannwhitneyu

rural_male = [52.9, 49.8, 44.4, 40.0, 34.2, 26.0]
rural_female = [87.0, 84.8, 79.9, 75.3, 67.8, 49.8]
urban_male = [22.6, 20.5, 18.5, 16.1, 13.2, 10.4]
urban_female = [60.3, 54.5, 48.3, 43.7, 37.6, 23.6]


early_period = [
    rural_male[0], rural_male[1], rural_male[2],
    rural_female[0], rural_female[1], rural_female[2],
    urban_male[0], urban_male[1], urban_male[2],
    urban_female[0], urban_female[1], urban_female[2]
]

later_period = [
    rural_male[3], rural_male[4], rural_male[5],
    rural_female[3], rural_female[4], rural_female[5],
    urban_male[3], urban_male[4], urban_male[5],
    urban_female[3], urban_female[4], urban_female[5]
]

stat, p = mannwhitneyu(early_period, later_period, alternative='two-sided')



print("Early period non-literacy values:", early_period)
print("Later period non-literacy values:", later_period)
print("Mann-Whitney U Statistic:", round(stat, 4))
print("p-value:", round(p, 4))



alpha = 0.05
if p < alpha:
    print("Result: Reject H0 → Time significantly impacts non-literacy at 5% level.")
else:
    print("Result: Fail to reject H0 → No significant impact of time on non-literacy.")