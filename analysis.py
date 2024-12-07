import sqlite3
import pandas as pd
import os

# Path to the SQLite database
DB_PATH = 'car_sales.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def load_data():
    try:
        # Loading the data into the database
        print("Loading data into the database...")

        # Check the current directory and confirm the file path
        print("Current directory:", os.getcwd())

        # Correct path to CSV file
        df = pd.read_csv('data/Car_sales.csv')  # Ensure this path is correct
        
        # Print column names for debugging
        print("Columns in CSV:", df.columns)

        # Create table if not exists
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS car_sales (
                Manufacturer TEXT,
                Model TEXT,
                Sales_in_thousands INTEGER,
                Resale_value INTEGER,
                Vehicle_type TEXT,
                Price_in_thousands INTEGER,
                Engine_size INTEGER,
                Horsepower INTEGER,
                Wheelbase INTEGER,
                Width INTEGER,
                Length INTEGER,
                Curb_weight INTEGER,
                Fuel_capacity INTEGER,
                Fuel_efficiency INTEGER,
                Latest_Launch TEXT
            );
        ''')

        # Load the DataFrame into SQL
        df.to_sql('car_sales', conn, if_exists='replace', index=False)
        print("Data loaded successfully into the database.")
        
    except Exception as e:
        print(f"Error loading data: {e}")

def execute_query(query_name, query):
    try:
        print(f"Executing Query '{query_name}'...")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(f"Query '{query_name}' executed successfully.")
            return result
        else:
            print(f"No results returned for Query '{query_name}'")
            return None
    except Exception as e:
        print(f"Error executing query '{query_name}': {e}")
        return None

def export_results_to_csv(results, file_name):
    try:
        if results:
            df = pd.DataFrame(results)
            df.to_csv(file_name, index=False)
            print(f"Query results exported successfully to '{file_name}'.")
        else:
            print("No results to export.")
    except Exception as e:
        print(f"Error exporting results: {e}")

# SQL Queries
queries = {
    "total_records": "SELECT COUNT(*) FROM car_sales;",
    "total_and_avg_price": "SELECT COUNT(*) AS Total_Records, SUM(`Price in thousands`) AS Total_Price,AVG(`Price in thousands`) AS Average_Price FROM car_sales;",  # Column name with space, enclosed in backticks
    "high_horsepower": "SELECT * FROM car_sales WHERE Horsepower > 300;"  # Column name Horsepower
}

# Load the data into the database
load_data()

# Execute each query and export the results
all_results = []
for query_name, query in queries.items():
    result = execute_query(query_name, query)
    if result:
        all_results.append(result)

# Export all results to CSV
export_results_to_csv(all_results, 'results/query_results.csv')

# Close the database connection
conn.close()
