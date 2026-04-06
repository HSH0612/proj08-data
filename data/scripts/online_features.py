import pandas as pd

# Sample input data
input_data = [
    {"transaction_description": "Transaction 1", "amount": 100, "category": "Food & Dining"},
    {"transaction_description": "Transaction 2", "amount": 200, "category": "Income"},
]

# Create DataFrame
df = pd.DataFrame(input_data)

# Compute online features
df["amount_squared"] = df["amount"] ** 2
df["is_food"] = df["category"] == "Food & Dining"

# Save the output to CSV
output_file = "/home/cc/online_features_output.csv"
df.to_csv(output_file, index=False)

# Print completion message
print("Online feature computation finished. Output saved to:", output_file)
