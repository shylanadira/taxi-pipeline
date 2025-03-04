import pandas as pd
import os
import logging
# Setup logging
log_filename = "result/loading.log"
os.makedirs("result", exist_ok=True)
logging.basicConfig(
    filename=log_filename, level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
def load_data():
    try:
        df = pd.read_csv("result/processed_table.csv")
        logging.info("Processed data loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error loading processed data: {e}")
        print("Error loading data. Please check if the file exists.")
        return None

def display_menu():
    print("\nTaxi Data Analysis Menu:")
    print("1. Show top rows of data")
    print("2. Show dataset summary")
    print("3. Find maximum trip duration")
    print("4. Find minimum trip distance")
    print("5. Count rows and columns")
    print("6. Exit")
