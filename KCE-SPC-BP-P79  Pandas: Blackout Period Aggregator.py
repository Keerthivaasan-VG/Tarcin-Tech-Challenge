import pandas as pd

df = pd.DataFrame({
    "start": pd.to_datetime(["2025-01-01", "2025-01-05", "2025-01-10"]),
    "end":   pd.to_datetime(["2025-01-03", "2025-01-08", "2025-01-12"])
})

# Merge overlapping blackout periods
df = df.sort_values("start")
agg = []
s, e = df.iloc[0]
for i in df.itertuples(index=False):
    if i.start <= e: e = max(e, i.end)
    else: agg.append((s, e)); s, e = i
agg.append((s, e))

result = pd.DataFrame(agg, columns=["start", "end"])
print(result)
