import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def predict_series(file_path, steps):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip().str.lower()  
    print("Columns in file:", df.columns.tolist())
   
    if "value" not in df.columns:
        raise ValueError("CSV must contain a 'value' column")
    X = [[i] for i in range(len(df))]
    y = df["value"].values
    model = LinearRegression()
    model.fit(X, y)
    future_X = [[i] for i in range(len(df), len(df)+steps)]
    predictions = model.predict(future_X)
    plt.plot(range(len(df)), y, label="Original")
    plt.plot(range(len(df), len(df)+steps), predictions, 'ro--', label="Predicted")
    plt.legend()
    plt.show()
   
    return predictions
preds = predict_series("series.csv", steps=3)
print("Predictions:", preds)
