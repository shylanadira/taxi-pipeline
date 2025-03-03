import pandas as pd
import glob
import os
import logging
# Setup logging
log_filename = "staging/staging.log"
os.makedirs("staging", exist_ok=True)
logging.basicConfig(
    filename=log_filename, level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# Data Extraction
os.makedirs("staging", exist_ok=True)
logging.info("Starting data extraction and staging process...")
csv_files = glob.glob("data/csv/*.csv")
json_files = glob.glob("data/json/*.json")
logging.info(f"Found {len(csv_files)} CSV files and {len(json_files)} JSON files.")

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

# Save to staging folder
staging_df.to_csv("staging/staging_table.csv", index=False)
logging.info("Staging table created successfully in 'staging/' folder.")
print("Successfully created in 'staging/' folder.")

initial_row_count = len(staging_df)
print(f"Initial row count before deduplication: {initial_row_count}")
staging_df = staging_df.drop_duplicates()
final_row_count = len(staging_df)
duplicates_removed = initial_row_count - final_row_count

print(f"Removed {duplicates_removed} duplicate rows.")
print(f"Final row count after deduplication: {final_row_count}")

