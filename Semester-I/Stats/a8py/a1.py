import pandas as pd 
from scipy.stats import gmean

data = pd.read_csv('BMW sales data (2010-2024).csv')
print(data)

# check each col is fill or not
data.isna().sum() 


central_tendencies = {
    'Mean': data[['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']].mean(),
    'Median': data[['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']].median(),
    'Mode': data[['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']].mode().iloc[0],
    'STD': data[['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']].std(),
    'GMean': gmean(data[['Engine_Size_L', 'Mileage_KM', 'Price_USD', 'Sales_Volume']])
}
pd.DataFrame(central_tendencies)

print("Mean of data:");
data[['Engine_Size_L', 'Mileage_KM', 'Price_USD']].mean()


print("Mode of data:");
data[['Engine_Size_L', 'Mileage_KM', 'Price_USD']].mode().iloc[0]


print("Standard Deviation")
data[['Engine_Size_L', 'Mileage_KM', 'Price_USD']].std()

print("Geometric Mean")
gmean(data[['Engine_Size_L', 'Mileage_KM', 'Price_USD']])