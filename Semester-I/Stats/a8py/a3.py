import pandas as pd 
import matplotlib.pyplot as plt

population_data = pd.DataFrame(
    {"YEAR": [1994, 2000, 2005, 2010],
    "TOTAL POPULATION (In Millions)": [894.2, 1005.3, 1094.0, 1187.1]
     }
)

print(population_data)


Count = population_data['TOTAL POPULATION (In Millions)'].value_counts();
population_data = population_data.sort_values("YEAR")
# print(Count)

plt.figure(figsize=(8,8))
plt.pie(population_data['TOTAL POPULATION (In Millions)'],
        labels=population_data['YEAR'],
        autopct='%.2f%%'
        )
plt.title('Population Distribution by Year')
plt.show()


# computing cumulative populations 
population_data["Cumulative"] = population_data['TOTAL POPULATION (In Millions)'].cumsum()

plt.figure(figsize=(8,5))
plt.plot(population_data['YEAR'], 
         population_data['Cumulative'], 
         marker='o', linestyle='-')
plt.title('Ogive: Cumulative Population Over Time (1994-2010)')
plt.xlabel('Year')
plt.ylabel('Cumulative Population (in Millions)')
plt.grid(True)
plt.show()