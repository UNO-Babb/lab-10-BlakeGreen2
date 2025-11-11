#MapPlot.py
#Name: Blake Green
#Date:11/11/25
#Assignment: Lab 10

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cars


data = cars.get_car()


print("Number of entries:", len(data))
print("First entry looks like this:")
print(data[0])


horsepower = [car["Engine Information"]["Engine Statistics"]["Horsepower"] for car in data]
highway_mpg = [car["Fuel Information"]["Highway mpg"] for car in data]
make = [car["Identification"]["Make"] for car in data]


df = pd.DataFrame({
    "Make": make,
    "Horsepower": horsepower,
    "Highway MPG": highway_mpg
})


df = df.dropna()
df = df[df["Horsepower"] < 1000]
df = df[df["Highway MPG"] > 0]


plt.figure(figsize=(8, 5))
plt.scatter(df["Horsepower"], df["Highway MPG"], color="skyblue", edgecolor="black", alpha=0.7)
plt.title("Horsepower vs. Highway MPG")
plt.xlabel("Horsepower")
plt.ylabel("Highway MPG")
plt.grid(True)


z = np.polyfit(df["Horsepower"], df["Highway MPG"], 1)
p = np.poly1d(z)
plt.plot(df["Horsepower"], p(df["Horsepower"]), color="red", linewidth=2, label="Trend Line")
plt.legend()


plt.savefig("cars_visualization.png", dpi=300)
plt.show()
