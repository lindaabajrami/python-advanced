import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_tokyo_data.csv")

print("\nCOLUMNS FOUND IN CSV:")
print(df.columns)

df["date"] = df["year"].astype(str) + "/" + df["day"]
df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")


df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
    .astype(float)
)
avg_temp = df["temperature"].mean()
print(f"\nAverage Temperature: {avg_temp:.2f} °C")

df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.strftime("%B")

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_avg = df.groupby("month_name")["temperature"].mean().reindex(month_order)

print("\nMonthly Average Temperatures:")
print(monthly_avg)

