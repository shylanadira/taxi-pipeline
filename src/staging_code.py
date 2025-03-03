import pandas as pd
import glob
import os

os.makedirs("staging", exist_ok=True)
csv_files = glob.glob("data/csv/*.csv")
json_files = glob.glob("data/json/*.json")

print("Found CSV files:", csv_files)
print("Found JSON files:", json_files)

# Read CSV file
csv_dataframes = [pd.read_csv(file, dtype=str) for file in csv_files] if csv_files else []
combined_csv_df = pd.concat(csv_dataframes, ignore_index=True) if csv_dataframes else pd.DataFrame()

# Read JSON file
json_dataframes = [pd.read_json(file, dtype=str) for file in json_files] if json_files else []
combined_json_df = pd.concat(json_dataframes, ignore_index=True) if json_dataframes else pd.DataFrame()

# Merge
staging_df = pd.merge(combined_csv_df, combined_json_df, how="outer") if not combined_csv_df.empty else combined_json_df