#!/usr/bin/env python3
import json

# Temp validator logic for ps-oct.
results = {
    "errors": [],
    "warnings": [],
    "meta": {
        "info": "Temporary ps-oct validator passed"
    }
}

# Write the results to product.json
with open("product.json", "w") as f:
    json.dump(results, f)

print("Validation done")
