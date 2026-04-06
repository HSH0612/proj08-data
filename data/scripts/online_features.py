# online_features.py
import json
import re
import sys

def compute_features(transaction: dict) -> dict:
    description = transaction.get("transaction_description", "")
    
    # Clean text: lowercase, remove special characters
    description_clean = re.sub(r'[^a-z0-9\s]', '', description.lower()).strip()
    
    # Feature: description word count
    description_length = len(description_clean.split())
    
    return {
        "transaction_description": description,
        "transaction_description_clean": description_clean,
        "country": transaction.get("country", ""),
        "currency": transaction.get("currency", ""),
        "description_length": description_length
    }

if __name__ == "__main__":
    # Accept JSON input from command line
    input_data = json.loads(sys.argv[1])
    features = compute_features(input_data)
    print(json.dumps(features, indent=2))
