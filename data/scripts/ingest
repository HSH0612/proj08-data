import pandas as pd
from pathlib import Path
import shutil

input_file = "/home/cc/transactions_v1.parquet"
output_file = "/home/cc/transactions_clean_v1.parquet"

df = pd.read_parquet(input_file)
df = df.dropna(subset=['transaction_description', 'category'])
df['transaction_description_clean'] = df['transaction_description'].str.lower().str.strip()
df.to_parquet(output_file, index=False)

print(f"Ingested and cleaned data saved to {output_file}")
