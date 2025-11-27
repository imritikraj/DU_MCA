import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)



df_1983 = pd.read_excel("Table9.xlsx", skiprows=1)
# print(df_1983)
df_1983.columns = ['State', 'Illiterate', 'Primary', 'Middle']
print("1983 Data loaded successfully")
# print(df_1983)
print(f"Dataset shape: {df_1983.shape}") # for the row and col

print("\nFirst 5 rows:")
df_1983.head()

df_1993 = pd.read_excel("Prac2_Table9_1993.xlsx", skiprows=1)
# print(df_1993)
df_1993.columns = ['State', 'Illiterate', 'Primary', 'Middle']
print("1993 Data loaded successfully")
# print(df_1983)
print(f"Dataset shape: {df_1993.shape}") # for the row and col

print("\nFirst 5 rows:")
df_1993.head()



print("DATA OVERVIEW")
print("============================================")

print("\n1983 DATASET INFO:")
print(f"Number of states: {len(df_1983)}")
print(f"Columns: {list(df_1983.columns)}")
# print(f"Data types:\n{df_1983.dtypes}")

print("\n1993-94 DATASET INFO:")
print(f"Number of states: {len(df_1993)}")
print(f"Columns: {list(df_1993.columns)}")
# print(f"Data types:\n{df_1993.dtypes}")

print("DESCRIPTIVE STATISTICS - MIDDLE EDUCATION LEVEL")
print("=" * 10)

print("\n1983 - Middle Education Statistics:")
print(df_1983['Middle'].describe())

print("\n1993-94 - Middle Education Statistics:")
print(df_1993['Middle'].describe())


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 1983 Box Plot
sns.boxplot(data=df_1983, y='Middle', ax=ax1, color='lightblue')
ax1.set_title('1983 - Primary Sector\n(Middle Education Level)', fontsize=14, fontweight='bold', color="blue")
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.grid(True, alpha=0.3)

# Add mean line for 1983
mean_1983 = df_1983['Middle'].mean()
ax1.axhline(y=mean_1983, color='red', linestyle='--', alpha=0.7, label=f'Mean: {mean_1983:.2f}%')
ax1.legend()

# 1993-94 Box Plot
sns.boxplot(data=df_1993, y='Middle', ax=ax2, color='lightgreen')
ax2.set_title('1993-94 - Primary Sector\n(Middle Education Level)', fontsize=14, color="blue", fontweight='bold')
ax2.set_ylabel('Percentage (%)', fontsize=12)
ax2.grid(True, alpha=0.3)

# Add mean line for 1993-94
mean_1993 = df_1993['Middle'].mean()
ax2.axhline(y=mean_1993, color='red', linestyle='--', alpha=0.7, label=f'Mean: {mean_1993:.2f}%')
ax2.legend()

plt.tight_layout()
plt.suptitle('Comparative Box Plots: Middle Education in Primary Sector', fontsize=16, color="red", fontweight='bold', y=1.02)
plt.show()



# Preparing data for combined box plot
df_combined = pd.DataFrame({
    'Year': ['1983'] * len(df_1983) + ['1993-94'] * len(df_1993),
    'Middle_Education': pd.concat([df_1983['Middle'], df_1993['Middle']], ignore_index=True)
})

# Create combined box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_combined, x='Year', y='Middle_Education', 
            palette=['lightblue', 'lightgreen'])
plt.title('Direct Comparison: Middle Education Levels (1983 vs 1993-94)', 
          fontsize=14, fontweight='bold')
plt.ylabel('Percentage (%)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(True, alpha=0.3)

# Add data points
sns.stripplot(data=df_combined, x='Year', y='Middle_Education', 
              color='black', alpha=0.6, size=5, jitter=True)

plt.show()


print("DETAILED STATISTICAL ANALYSIS \n")


def calculate_detailed_stats(data, year):
    """Calculate detailed statistics for box plot analysis"""
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_whisker = Q1 - 1.5 * IQR
    upper_whisker = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_whisker) | (data > upper_whisker)]
    
    stats = {
        'Year': year,
        'Mean': data.mean(),
        'Median': data.median(),
        'Std Dev': data.std(),
        'Min': data.min(),
        'Max': data.max(),
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'Lower Whisker': lower_whisker,
        'Upper Whisker': upper_whisker,
        'Outliers': outliers.tolist(),
        'Outlier Count': len(outliers),
        'Skewness': data.skew()
    }
    return stats

# Calculate statistics for both years
stats_1983 = calculate_detailed_stats(df_1983['Middle'], '1983')
stats_1993 = calculate_detailed_stats(df_1993['Middle'], '1993-94')

# Create comparison table
comparison_df = pd.DataFrame([stats_1983, stats_1993])
comparison_df = comparison_df.set_index('Year')
comparison_df = comparison_df.round(3)

print("\nStatistical Comparison:")
comparison_df



# Identify outlier states
print("OUTLIER ANALYSIS \n")


print("\n1983 Outliers:")
outliers_1983 = df_1983[df_1983['Middle'] > stats_1983['Upper Whisker']]
if not outliers_1983.empty:
    for _, row in outliers_1983.iterrows():
        print(f"  - {row['State']}: {row['Middle']}%")
else:
    print("  No significant outliers")

print("\n1993-94 Outliers:")
outliers_1993 = df_1993[df_1993['Middle'] > stats_1993['Upper Whisker']]
if not outliers_1993.empty:
    for _, row in outliers_1993.iterrows():
        print(f"  - {row['State']}: {row['Middle']}%")
else:
    print("  No significant outliers")




    # Create distribution plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# 1983 Distribution
sns.histplot(data=df_1983, x='Middle', kde=True, ax=ax1, color='lightblue', bins=8)
ax1.set_title('1983 - Distribution of Middle Education', fontsize=12, fontweight='bold')
ax1.set_xlabel('Percentage (%)')
ax1.axvline(df_1983['Middle'].mean(), color='red', linestyle='--', label=f'Mean: {df_1983["Middle"].mean():.2f}%')
ax1.axvline(df_1983['Middle'].median(), color='green', linestyle='--', label=f'Median: {df_1983["Middle"].median():.2f}%')
ax1.legend()

# 1993-94 Distribution
sns.histplot(data=df_1993, x='Middle', kde=True, ax=ax2, color='lightgreen', bins=8)
ax2.set_title('1993-94 - Distribution of Middle Education', fontsize=12, fontweight='bold')
ax2.set_xlabel('Percentage (%)')
ax2.axvline(df_1993['Middle'].mean(), color='red', linestyle='--', label=f'Mean: {df_1993["Middle"].mean():.2f}%')
ax2.axvline(df_1993['Middle'].median(), color='green', linestyle='--', label=f'Median: {df_1993["Middle"].median():.2f}%')
ax2.legend()

plt.tight_layout()
plt.show()


# Calculate percentage change
mean_change = ((stats_1993['Mean'] - stats_1983['Mean']) / stats_1983['Mean']) * 100
median_change = ((stats_1993['Median'] - stats_1983['Median']) / stats_1983['Median']) * 100

print("\nTREND ANALYSIS (1983 → 1993-94) \n")

print(f"Mean increase: {stats_1993['Mean'] - stats_1983['Mean']:.2f} percentage points")
print(f"Mean percentage change: {mean_change:.1f}%")
print(f"Median increase: {stats_1993['Median'] - stats_1983['Median']:.2f} percentage points")
print(f"Median percentage change: {median_change:.1f}%")
print(f"Standard deviation change: {stats_1993['Std Dev'] - stats_1983['Std Dev']:.2f}")
print(f"Range increase: {stats_1993['Max'] - stats_1983['Max']:.2f} percentage points")

print("\nIMPLICATIONS:")
print("• Significant overall improvement in educational attainment")
print("• Growing inequality in educational development across states")
print("• Need for targeted interventions in lagging states")
print("• Kerala's success suggests replicable educational models")