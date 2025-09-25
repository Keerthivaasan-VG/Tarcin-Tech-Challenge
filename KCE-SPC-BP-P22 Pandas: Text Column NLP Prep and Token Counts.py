import pandas as pd
from collections import Counter
import re

# Example DataFrame
df = pd.DataFrame({'text': ["Hello world!", "Pandas NLP prep.", "Tokenize this text."]})

# Clean, lowercase, tokenize, count
df['tokens'] = df['text'].str.lower().str.replace(r'[^a-z\s]', '', regex=True).str.split()
token_counts = Counter([tok for tokens in df['tokens'] for tok in tokens])

print(df)
print(token_counts)
