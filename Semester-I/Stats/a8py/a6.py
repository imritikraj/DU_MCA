import numpy as np
import pandas as pd
from scipy.stats import kruskal
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

rural_male = [52.9, 49.8, 44.4, 40.0, 34.2, 26.0]
rural_female = [87.0, 84.8, 79.9, 75.3, 67.8, 49.8]
urban_male = [22.6, 20.5, 18.5, 16.1, 13.2, 10.4]
urban_female = [60.3, 54.5, 43.7, 43.7, 30.7, 23.6]

years = ['1983', '1987-88', '1993-94', '1999-2000', '2004-05', '2009-10']

print("Data Overview:")
print(f"Rural Male:    {rural_male}")
print(f"Rural Female:  {rural_female}")
print(f"Urban Male:    {urban_male}")
print(f"Urban Female:  {urban_female}")
print(f"Time Periods:  {years}\n")


data_dict = {
    'Year': years * 4,
    'Non_Literacy': rural_male + rural_female + urban_male + urban_female,
    'Group': ['Rural Male']*6 + ['Rural Female']*6 + ['Urban Male']*6 + ['Urban Female']*6
}

df = pd.DataFrame(data_dict)
print("📈 Data Summary:")
print(df.groupby('Year')['Non_Literacy'].describe())


plt.figure(figsize=(12, 8))



plt.subplot(2, 1, 1)
for group in df['Group'].unique():
    group_data = df[df['Group'] == group]
    plt.plot(group_data['Year'], group_data['Non_Literacy'], marker='o', label=group, linewidth=2)

plt.title('Non-Literacy Trends Across Demographic Groups (1983-2009)', fontsize=14, fontweight='bold')
plt.ylabel('Non-Literacy Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)



plt.subplot(2, 1, 2)
sns.boxplot(data=df, x='Year', y='Non_Literacy', palette='viridis')
plt.title('Distribution of Non-Literacy Rates by Year', fontsize=14, fontweight='bold')
plt.ylabel('Non-Literacy Rate (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()



# Prepare data for Kruskal-Wallis test
# Group non-literacy rates by year
year_groups = []
for year in years:
    year_data = df[df['Year'] == year]['Non_Literacy'].values
    year_groups.append(year_data)
    print(f"{year}: {year_data}")

# Perform Kruskal-Wallis test
statistic, p_value = kruskal(*year_groups)




print(f"Kruskal-Wallis H Statistic: {statistic:.4f}")
print(f"P-value: {p_value:.6f}")



alpha = 0.05
if p_value < alpha:
    print(f"RESULT: Reject H0 - Time has significant impact on non-literacy rates")
    print("There are statistically significant differences in non-literacy rates across the years.")
else:
    print(f"RESULT: Fail to reject H0 - No significant impact of time on non-literacy rates")
    print("There are no statistically significant differences in non-literacy rates across the years.")



if p_value < 0.001:
    print("   Very strong evidence against H0")
elif p_value < 0.01:
    print("   Strong evidence against H0")
elif p_value < 0.05:
    print("   Moderate evidence against H0")
elif p_value < 0.1:
    print("   Weak evidence against H0")
else:
    print("   No evidence against H0")


for i, year in enumerate(years):
    median_val = np.median(year_groups[i])
    mean_val = np.mean(year_groups[i])
    std_val = np.std(year_groups[i])
    print(f"{year}: Mean = {mean_val:.1f}%, Median = {median_val:.1f}%, Std = {std_val:.1f}")

# Calculate overall trends
overall_means = [np.mean(group) for group in year_groups]
trend_slope = (overall_means[-1] - overall_means[0]) / (len(years) - 1)


print(f"Average non-literacy rate decreased from {overall_means[0]:.1f}% to {overall_means[-1]:.1f}%")
print(f"Average annual decrease: {abs(trend_slope):.2f} percentage points")

print(f"\n💡 Conclusion:")
if p_value < alpha:
    print("The Kruskal-Wallis test confirms that time period significantly affects non-literacy rates.")
    print("This suggests that educational policies and interventions over the years have had measurable impact.")
else:
    print("The Kruskal-Wallis test does not show significant differences in non-literacy rates across years.")
    print("This might indicate consistent patterns or that other factors beyond time are more influential.")