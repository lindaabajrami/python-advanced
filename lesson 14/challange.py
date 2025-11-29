import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv("weather_tokyo_data.csv")

print("\nCOLUMNS FOUND IN CSV:")
print(df.columns)

# -----------------------------
# FIX DATE COLUMN
# -----------------------------
# Combine year + day ("MM/DD" format)
df["date"] = df["year"].astype(str) + "/" + df["day"]
df["date"] = pd.to_datetime(df["date"], format="%Y/%m/%d")

# Convert temperature to float (fix parentheses like "(0.3)")
df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
    .astype(float)
)

# -----------------------------
# 1. AVERAGE TEMPERATURE
# -----------------------------
avg_temp = df["temperature"].mean()
print(f"\nAverage Temperature: {avg_temp:.2f} °C")

# -----------------------------
# 2. MONTHLY TEMPERATURE
# -----------------------------
df["month"] = df["date"].dt.month
df["month_name"] = df["date"].dt.strftime("%B")

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_avg = df.groupby("month_name")["temperature"].mean().reindex(month_order)

print("\nMonthly Average Temperatures:")
print(monthly_avg)

# Bar plot for monthly average temperature
plt.figure(figsize=(10,5))
monthly_avg.plot(kind="bar")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. HIGHEST & LOWEST TEMPERATURE DAYS
# -----------------------------
hottest = df.loc[df["temperature"].idxmax()]
coldest = df.loc[df["temperature"].idxmin()]

print("\nHottest Day:")
print(hottest)

print("\nColdest Day:")
print(coldest)

# -----------------------------
# 4. TEMPERATURE TREND OVER TIME
# -----------------------------
plt.figure(figsize=(12,5))
plt.plot(df["date"], df["temperature"])
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()

# -----------------------------
# 5. SEASONAL AVERAGE TEMPERATURE
# -----------------------------
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

df["season"] = df["month"].apply(get_season)

season_order = ["Winter", "Spring", "Summer", "Fall"]

seasonal_avg = df.groupby("season")["temperature"].mean().reindex(season_order)

print("\nSeasonal Average Temperature:")
print(seasonal_avg)

# Plot seasonal averages
plt.figure(figsize=(8,5))
seasonal_avg.plot(marker="o")
plt.title("Seasonal Average Temperature")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()\






