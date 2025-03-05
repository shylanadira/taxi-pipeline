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
    print("6. Find average trip duration")
    print("7. Find average trip distance")
    print("8. Find most used vendor")
    print("9. Find most used payment type")
    print("10. Show time period of data")
    print("11. Find most expensive trip")
    print("12. Exit")
def main():
    df = load_data()
    if df is None:
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-12): ")
        
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
            avg_duration = df["trip_duration"].mean()
            print(f"Average trip duration: {avg_duration:.2f} seconds")
        elif choice == "7":
            avg_distance = df["trip_distance_km"].mean()
            print(f"Average trip distance: {avg_distance:.2f} km")
        elif choice == "8":
            most_vendor = df["vendor_id"].mode()[0]
            print(f"Most used vendor: {most_vendor}")
        elif choice == "9":
            most_payment_type = df["payment_type"].mode()[0]
            print(f"Most used payment type: {most_payment_type}")
        elif choice == "10":
            start_date = df["lpep_pickup_datetime"].min()
            end_date = df["lpep_dropoff_datetime"].max()
            print(f"Data covers the period from {start_date} to {end_date}")
        elif choice == "11":
            most_expensive_trip = df["fare_amount"].max()
            print(f"Most expensive trip cost: ${most_expensive_trip:.2f}")
        elif choice == "12":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please enter a number between 1-12.")


if __name__ == "__main__":
    main()