# SQL Data Analysis on Car Sales Data

## Project Overview

This project demonstrates how to perform basic data analysis on a local SQLite database using SQL. The dataset contains information about car sales, and SQL queries are used to analyze and process the data. The analysis includes counting records, calculating averages, summing values, and filtering based on specific conditions. The project highlights the application of SQL in data analysis by transforming raw data into valuable insights.

### Objective
The goal of this project is to show how SQL can be used to:
- Gain insights from raw data
- Count records to understand dataset size
- Calculate aggregates like totals and averages
- Filter and sort data based on certain criteria (e.g., high horsepower)
- Make informed decisions based on data analysis results

### Dataset Used:
- **Car Sales Dataset** from [GitHub](https://github.com/chandanverma07/DataSets/blob/master/Car_sales.csv)

### Dataset Information

The dataset contains information on car sales across various manufacturers and includes fields such as:
- **Make**: The manufacturer of the car (e.g., Toyota, Ford, BMW).
- **Model**: The specific model of the car (e.g., Camry, Mustang, X5).
- **Year**: The year of manufacture.
- **MSRP**: Manufacturer's Suggested Retail Price.
- **Engine HP**: Horsepower of the engine.
- **Mileage**: The mileage or fuel efficiency of the car.
- **Price**: The final sale price of the car, after negotiations and discounts.

This dataset can be used to perform various types of analyses, including pricing trends, engine performance, and market preferences.


## Analysis Performed

### 1. Count the Total Number of Records in the Dataset

This query calculates the total number of records in the dataset to get an idea of its size. It is useful when starting any data analysis project to know how much data you are working with.

SELECT COUNT(*) AS Total_Records FROM car_sales;

Result: The query returns the total number of records in the dataset.

<img width="734" alt="Screenshot 2024-12-07 233400" src="https://github.com/user-attachments/assets/19936c7c-8989-4f9e-aa0a-f3438c073f54">


### 2. Calculate the Total and Average MSRP (Price) from the car_sales Dataset

This query calculates both the sum and the average of the MSRP column (Manufacturer's Suggested Retail Price) from the car_sales dataset.

SELECT 
    COUNT(*) AS Total_Records, 
    SUM(`Price in thousands`) AS Total_Price,
    AVG(`Price in thousands`) AS Average_Price 
FROM car_sales;

Result: This query returns:
-The total number of records in the dataset.
-The total price of all cars combined.
-The average price per car.

<img width="626" alt="Screenshot 2024-12-07 234344" src="https://github.com/user-attachments/assets/3dc33110-ef62-4ecb-993a-a0723ab5aecd">


### 3. Filter Records Where Engine_HP is Greater Than 300

This query filters the records where the Engine_HP (engine horsepower) is greater than 300.

SELECT * FROM car_sales WHERE Horsepower > 300;

Result: This query returns the full records of cars with horsepower greater than 300, which could indicate sports cars or high-performance models.

<img width="628" alt="Screenshot 2024-12-07 234501" src="https://github.com/user-attachments/assets/6a74fdd0-3650-455d-b520-5c84e1d8a997">



### Prerequisites

- **Python**: To run the Python script and manage dependencies.
- **SQLite3**: To manage the SQLite database.
- **VS Code** : To edit the scripts and view the results.

