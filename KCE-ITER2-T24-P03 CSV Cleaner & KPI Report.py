from sklearn.preprocessing import StandardScaler
import pandas as pd

def report(filename):
    df = pd.read_csv(filename, encoding="utf-8", sep=",", header='infer')

    # Keep only numeric columns for statistics
    numeric_cols = df.select_dtypes(include='number').columns
    report_df = pd.DataFrame()
    report_df['Mean'] = df[numeric_cols].mean()
    report_df['Median'] = df[numeric_cols].median()
    report_df['Std'] = df[numeric_cols].std()

    report_df.to_csv("output.csv", index=True, mode='w', header=True)
    print("CSV saved as output.csv")

    # Standardize the mean column
    scaler = StandardScaler()
    report_df['Standardized_Mean'] = scaler.fit_transform(report_df[['Mean']])

    report_df.to_csv('report.csv', index=True, mode='w', header=True)
    print("CSV saved as report.csv")


# report("data.csv")
