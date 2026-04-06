import pandas as pd
import random

records = []
categories = ['Income', 'Food & Dining', 'Healthcare & Medical', 'Shopping & Retail']
countries = ['USA', 'UK', 'AU']
currencies = ['USD', 'GBP', 'AUD']

for i in range(100):
    records.append({
        "transaction_description": f"Transaction {i}",
        "category": random.choice(categories),
        "country": random.choice(countries),
        "currency": random.choice(currencies)
    })

df = pd.DataFrame(records)
df.to_parquet('/home/cc/synthetic_transactions.parquet', index=False)
print("Synthetic data generated at /home/cc/synthetic_transactions.parquet")
