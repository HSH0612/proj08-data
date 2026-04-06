import pandas as pd

# Read cleaned transactions
df = pd.read_parquet("/app/output/transactions_clean_v1.parquet")

# Drop missing values
df = df.dropna(subset=['transaction_description', 'category'])

# Standardize text
df['transaction_description_clean'] = df['transaction_description'].str.lower().str.strip()

# Save cleaned file
df.to_parquet("/app/output/transactions_clean_v1.parquet", index=False)

# Split into train and eval CSV files
train_df = df.sample(frac=0.8, random_state=42)
eval_df = df.drop(train_df.index)

train_df.to_csv("/app/output/train_data.csv", index=False)
eval_df.to_csv("/app/output/eval_data.csv", index=False)

# Print first 5 rows to verify
print(df.head(5))
