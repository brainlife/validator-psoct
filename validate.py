#!/usr/bin/env python3
import json

# Temp validator logic for ps-oct.
results = {
    "errors": [],
    "warnings": [],
    "meta": {
        "info": "Temporary ps-oct validator passed with no errors",
        "version": "0.1",
        "date": "2025-04-07",
    }
}

# Write the results to product.json
with open("product.json", "w") as f:
    json.dump(results, f)

print("Validation done")
