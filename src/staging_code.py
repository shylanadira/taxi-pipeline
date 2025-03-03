import pandas as pd
import glob
import os

os.makedirs("staging", exist_ok=True)
csv_files = glob.glob("data/csv/*.csv")
json_files = glob.glob("data/json/*.json")

print("Found CSV files:", csv_files)
print("Found JSON files:", json_files)