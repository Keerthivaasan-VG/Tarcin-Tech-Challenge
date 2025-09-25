import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
data = pd.read_csv("series.csv", encoding="utf-8", sep=",")

# Assuming your CSV has columns 't' and 'value'
t = data['t'].values
value = data['value'].values

# Find local maxima (peaks)
peaks = []
for i in range(1, len(value)-1):
    if value[i] > value[i-1] and value[i] > value[i+1]:
        peaks.append(i)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, value, label="Series")
plt.plot(t[peaks], value[peaks], "ro", label="Local maxima")
plt.xlabel("t")
plt.ylabel("value")
plt.title("Series with Local Maxima")
plt.legend()
plt.grid(True)
plt.show()

# Print peaks
for i in peaks:
    print(f"t={t[i]}, value={value[i]}")
