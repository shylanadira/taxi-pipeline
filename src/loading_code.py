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
    print("4. Find maximum trip distance")
    print("5. Count rows and columns")
    print("6. Exit")
def main():
    df = load_data()
    if df is None:
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print(df.head())
        elif choice == "2":
            print(df.describe())
        elif choice == "3":
            max_duration = df["trip_duration"].max()
            print(f"Maximum trip duration: {max_duration}")
        elif choice == "4":
            max_distance = df["trip_distance_km"].max()
            print(f"Maximum trip distance: {max_distance} km")
        elif choice == "5":
            print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a number between 1-6.")

if __name__ == "__main__":
    main()