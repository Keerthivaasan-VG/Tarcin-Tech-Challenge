import pandas as pd
from scipy.spatial.distance import jensenshannon

def cat_drift(prev_df, curr_df, col):
    prev = prev_df[col].value_counts(normalize=True)
    curr = curr_df[col].value_counts(normalize=True)
    all_cat = prev.index.union(curr.index)
    p = prev.reindex(all_cat, fill_value=0).values
    q = curr.reindex(all_cat, fill_value=0).values
    js = jensenshannon(p, q, base=2)
    return {"js_divergence": js, "drift": "High" if js > 0.1 else "Low"}

# Example
prev = pd.DataFrame({"color": ["red","red","blue","green","red"]})
curr = pd.DataFrame({"color": ["red","green","green","blue","blue"]})
print(cat_drift(prev, curr, "color"))
