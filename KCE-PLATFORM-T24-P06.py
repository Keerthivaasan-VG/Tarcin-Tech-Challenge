import pandas as pd

def report(input_csv="input.csv", output_csv="report.csv"):
    # Read CSV
    df = pd.read_csv(input_csv)

    # Compute KPIs
    kpis = pd.DataFrame({
        "mean": df.mean(),
        "median": df.median(),
        "std": df.std()
    })

    # Normalize (min-max scaling)
    normalized = (kpis - kpis.min()) / (kpis.max() - kpis.min())

    # Save normalized report
    normalized.to_csv(output_csv)

    return normalized

# Example usage
print(report())
