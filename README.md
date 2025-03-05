# Taxi Data Pipeline

![image](https://github.com/user-attachments/assets/3988670b-23d8-445f-b9a6-6279d9011cd2)

## 📌 Overview
This project is a **data pipeline** for processing taxi trip data, involving **extraction, transformation, and loading (ETL)**. The pipeline is built using **Python and Pandas** and supports **JSON and CSV** data sources. It includes **logs** for managing the traceability.

## 📁 Project Structure
```
📂 taxi-pipeline
 ┣ 📂 data         # Contains source data files (CSV & JSON)
 ┃ ┣ 📂 csv        # Raw CSV files
 ┃ ┗ 📂 json       # Raw JSON files
 ┣ 📂 staging      # Intermediate storage before transformation and staging logs
 ┣ 📂 processed    # Final processed data and processing logs
 ┣ 📂 src          # Source code for staging & processing
 ┣ 📜 README.md    # Project documentation
```
## ⚙️ Features

<img width="541" alt="image" src="https://github.com/user-attachments/assets/b957066f-d7d8-4335-9108-3c4734bae32e" />

- **Extracting Process:**
  - Extracts and merges CSV and JSON files.
  - Fill empty data with N/A.
  - Drop the duplicates.
- **Transforming Process:**
  - Converts column names to **snake_case**.
  - Maps `payment_type` to readable labels.
  - Converts `trip_distance` from miles to kilometers.
  - Adds `trip_duration` using `lpep_pickup_datetime` & `lpep_dropoff_datetime`.
  - Saves processed data as **CSV**.
- **Loading Process:** Saves final processed data to a CSV file and makes Data Menu for table info.
- **Logging:** Every step is logged for full traceability.
## 📊 Data Schema
| Column                  | Description |
|-------------------------|-------------|
| `vendor_id`             | Taxi company ID |
| `lpep_pickup_datetime`  | Pickup time |
| `lpep_dropoff_datetime` | Dropoff time |
| `store_and_fwd_flag`    | Whether the trip was stored before sending (Y/N) |
| `ratecode_id`           | Rate category |
| `pu_location_id`        | Pickup location ID |
| `do_location_id`        | Dropoff location ID |
| `passenger_count`       | Number of passengers |
| `trip_distance_km`      | Distance in kilometers (converted from miles) |
| `fare_amount`           | Base fare |
| `extra`                 | Additional charges such as night fees or peak-hour fees |
| `mta_tax`               | Additional taxes imposed by the MTA |
| `tip_amount`            | Tip amount given by the passenger |
| `tolls_amount`          | Toll fees paid during the trip |
| `ehail_fee`             | Booking fee for electronic taxi reservations |
| `improvement_surcharge` | Regulatory surcharge imposed by the city of New York |
| `total_amount`          | Total fare after taxes, surcharges, and tips |
| `payment_type`          | Readable payment method |
| `trip_type`             | Trip type, regular trip or prearranged (pre-booked) trip |
| `congestien_surcharge`  | Congestion surcharge applied to certain trips |
| `trip_duration`         | Trip duration in minutes & seconds |

## Menu

**Taxi Data Analysis Menu:**
1. Show top rows of data
2. Show dataset summary
3. Find maximum trip duration
4. Find maximum trip distance
5. Count rows and columns
6. Find average trip duration
7. Find average trip distance
8. Find most used vendor
9. Find most used payment type
10. Show time period of data
11. Find most expensive trip
12. Exit
Enter your choice (1-12):
