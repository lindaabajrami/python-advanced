import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../lesson 12/kaggle_data/avgIQpercountry.csv')

nobel_prize_by_continent = df.groupby('Continent')['Nobel prices'].sum()

no_of_continents = nobel_prize_by_continent.count()

print(no_of_continents)

colors = ['gold', 'lightcoral', 'yellow', 'thistle', 'orange', 'lightskyblue', 'aquamarine', 'burlywood']

plt.figure(figsize=(10,10))

nobel_prize_by_continent.plot(kind='pie', color=colors, autopc='%1.1f%%')

plt.title("Distribution of nobel prizes by continent")

plt.axist('equal')

plt.ylabel('')

plt.tight_layout()

plt.show()