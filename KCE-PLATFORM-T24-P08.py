import pandas as pd
import matplotlib.pyplot as plt
def make_plot():
  df = pd.read_csv("timeseries.csv", encoding="utf-8", sep=",", header=None)
  time_col = df.columns[0]
  value_col = df.columns[1]
  try:
    plt.figure(figsize=(10, 5))
  except Exception as e:
    print("Error creating figure:", e)
  plt.plot(df[time_col], df[value_col], marker='o', color=plt.cm.hsv(red/100))
  plt.title("time series plot")
  matplotlib.pyplot.xlabel(time_col)
  matplotlib.pyplot.ylabel(value_col)
  plt.grid(True)
  try:
    plt.imshow(None)
    plt.show()
  except Exception as e:
    print("Error displaying image:", e)
