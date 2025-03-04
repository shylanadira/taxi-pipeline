import pandas as pd
import os
import re
import logging
# Set up logging
log_filename = "result/processing.log"
os.makedirs("result", exist_ok=True)
logging.basicConfig(
    filename=log_filename, level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
def log_and_print(message, level="info"):
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    print(message)

log_and_print("Data processing started..")

def snake_case(col_name):
    col_name = re.sub(r'[\W]+', '_', col_name)
    col_name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', col_name) 
    col_name = col_name.lower().strip('_')
    return col_name

payment_mapping_df = pd.read_csv("data/payment_type.csv", header=None, names=["code", "label"], dtype=str)
payment_mapping = dict(zip(payment_mapping_df["code"], payment_mapping_df["label"]))

staging_df = pd.read_csv("staging/staging_table.csv", dtype=str)

# Normalize column names
staging_df.columns = [snake_case(col) for col in staging_df.columns]
log_and_print("Normalized column names to snake_case.")

# Convert payment_type 
if "payment_type" in staging_df.columns:
    staging_df["payment_type"] = staging_df["payment_type"].astype(str).map(payment_mapping).fillna("Unknown")
    log_and_print("Converted payment_type to lables.")

# Convert trip_distance from miles to kilometers
if "trip_distance" in staging_df.columns:
    staging_df["trip_distance"] = pd.to_numeric(staging_df["trip_distance"], errors="coerce")
    staging_df["trip_distance"] = (staging_df["trip_distance"] * 1.60934).round(2)
    staging_df.rename(columns={"trip_distance": "trip_distance_km"}, inplace=True)
    log_and_print("Converted trip_distance to kilometers.")

# Calculate trip duration (lpep_pickup_datetime - lpep_dropoff_datetime)
if "lpep_pickup_datetime" in staging_df.columns and "lpep_dropoff_datetime" in staging_df.columns:
    staging_df["lpep_pickup_datetime"] = pd.to_datetime(staging_df["lpep_pickup_datetime"], errors="coerce")
    staging_df["lpep_dropoff_datetime"] = pd.to_datetime(staging_df["lpep_dropoff_datetime"], errors="coerce")
    staging_df["trip_duration"] = (staging_df["lpep_dropoff_datetime"] - staging_df["lpep_pickup_datetime"]).dt.total_seconds()
    staging_df["trip_duration"] = staging_df["trip_duration"].fillna(0).astype(int)  
    staging_df["trip_duration"] = staging_df["trip_duration"].apply(lambda x: f"{x // 60} min {x % 60} sec") 
    log_and_print("Calculated trip duration.")
    
staging_df.fillna("N/A", inplace=True)
# Save processed data
staging_df.to_csv("result/processed_table.csv", index=False)

log_and_print("Processed table saved successfully in 'result/' folder.")

log_and_print("Data processing completed successfully.")