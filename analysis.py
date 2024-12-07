# import sqlite3
# import pandas as pd

# # Step 1: Load the data from CSV and create the SQLite database
# def load_data_to_db():
#     # Connect to SQLite database (creates a new one if it doesn't exist)
#     connection = sqlite3.connect('car_sales.db')
#     cursor = connection.cursor()

#     # Read the SQL script to create the table
#     with open('sql/create_table.sql', 'r') as file:
#         create_table_sql = file.read()

#     # Execute the SQL script to create the table
#     cursor.executescript(create_table_sql)
    
#     # Load the CSV data into a Pandas DataFrame
#     car_sales_df = pd.read_csv('data/Car_sales.csv')
    
#     # Insert the DataFrame into the 'car_sales' table
#     car_sales_df.to_sql('car_sales', connection, if_exists='replace', index=False)
    
#     print("✅ Data loaded successfully into the database.")
#     connection.close()

# # Step 2: Run the SQL queries and export the results to a CSV file
# def run_queries_and_export_results():
#     # Connect to SQLite database
#     connection = sqlite3.connect('car_sales.db')

#     # List of queries to be executed
#     queries = {
#         "total_records": "SELECT COUNT(*) AS Total_Records FROM car_sales;",
#         "total_and_avg_msrp": "SELECT SUM(MSRP) AS Total_MSRP, AVG(MSRP) AS Average_MSRP FROM car_sales;",
#         "high_engine_hp": "SELECT * FROM car_sales WHERE Engine_HP > 300;"
#     }
    
#     all_results = []

#     for query_name, query in queries.items():
#         df = pd.read_sql_query(query, connection)
#         print(f"✅ Query '{query_name}' executed successfully.")
#         all_results.append(df)

#     # Concatenate all the query results into a single CSV file
#     final_results = pd.concat(all_results, ignore_index=True)
#     final_results.to_csv('results/query_results.csv', index=False)
    
#     print("✅ Query results exported successfully to 'results/query_results.csv'.")
#     connection.close()

# if __name__ == "__main__":
#     load_data_to_db()
#     run_queries_and_export_results()



import sqlite3
import pandas as pd

# Path to the SQLite database
DB_PATH = 'car_sales.db'

# Create a connection to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def load_data():
    try:
        # Loading the data into the database
        print("Loading data into the database...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS car_sales (
                Make TEXT,
                Model TEXT,
                Year INTEGER,
                Engine_Fuel_Type TEXT,
                Engine_HP INTEGER,
                Engine_Cylinders INTEGER,
                Transmission_Type TEXT,
                Driven_Wheels TEXT,
                Number_of_Doors INTEGER,
                Market_Category TEXT,
                Vehicle_Size TEXT,
                Vehicle_Style TEXT,
                Highway_MPG INTEGER,
                City_MPG INTEGER,
                Popularity INTEGER,
                MSRP INTEGER
            );
        ''')
        
        # Assuming you have a pandas DataFrame ready with your data
        df = pd.read_csv('data/Car_sales.csv')
        df.to_sql('-car_sales', conn, if_exists='replace', index=False)
        print("-Data loaded successfully into the database.")
    except Exception as e:
        print(f"-Error loading data: {e}")

def execute_query(query_name, query):
    try:
        print(f"-Executing Query '{query_name}'...")
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(f"-Query '{query_name}' executed successfully.")
            return result
        else:
            print(f"-No results returned for Query '{query_name}'")
            return None
    except Exception as e:
        print(f"Error executing query '{query_name}': {e}")
        return None

def export_results_to_csv(results, file_name):
    try:
        if results:
            df = pd.DataFrame(results)
            df.to_csv(file_name, index=False)
            print(f"-Query results exported successfully to '{file_name}'.")
        else:
            print("No results to export.")
    except Exception as e:
        print(f"-Error exporting results: {e}")

# SQL Queries
queries = {
    "total_records": "SELECT COUNT(*) FROM car_sales;",
    "total_and_avg_msrp": "SELECT COUNT(*), AVG(MSRP) FROM car_sales;",
    "high_engine_hp": "SELECT * FROM car_sales WHERE Engine_HP > 200;"
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
