# SQL Data Analysis on Car Sales Data

## Project Overview

This project demonstrates how to perform basic data analysis on a local SQLite database using SQL. The dataset contains information about car sales, and we use SQL queries to analyze and process the data, including counting records, calculating averages, and filtering based on conditions. The analysis is done using an SQLite database that is populated with data from a CSV file.

The goal of this project is to show how SQL can be used to gain insights from raw data, including counting records, calculating averages, filtering based on specific criteria, and more. 

### Dataset used is : 
https://github.com/chandanverma07/DataSets/blob/master/Car_sales.csv


### Dataset Information

The dataset used in this project contains car sales data, including fields such as:
- **Make**: The manufacturer of the car (e.g., Toyota, Ford).
- **Model**: The specific model of the car (e.g., Camry, Mustang).
- **Year**: The year of manufacture.
- **MSRP**: Manufacturer's Suggested Retail Price.
- **Engine HP**: Horsepower of the engine.
- **Mileage**: The mileage of the car.
- **Price**: The final sale price of the car.


## Queries Run

### 1. Count the Total Number of Records in the Dataset
This query counts the total number of records in the `car_sales` dataset.

SELECT COUNT(*) AS Total_Records FROM car_sales;

<img width="624" alt="Screenshot 2024-12-07 225042" src="https://github.com/user-attachments/assets/262b71e2-c8ca-4f79-9578-26b06e0e8723">



### 2. Calculate the Total and Average MSRP (Price) from the car_sales Dataset

This query calculates both the sum and the average of the MSRP column (Manufacturer's Suggested Retail Price) from the car_sales dataset.

SELECT 
    SUM(MSRP) AS Total_MSRP, 
    AVG(MSRP) AS Average_MSRP 
FROM car_sales;


<img width="627" alt="Screenshot 2024-12-07 225124" src="https://github.com/user-attachments/assets/bd57bb20-50ca-4676-8060-ee884d3fcb23">


### 3. Filter Records Where Engine_HP is Greater Than 300

This query filters the records where the Engine_HP (engine horsepower) is greater than 300.

SELECT * 
FROM car_sales 
WHERE Engine_HP > 300;

<img width="736" alt="Screenshot 2024-12-07 225240" src="https://github.com/user-attachments/assets/81569d7a-3466-40ac-8cc4-a734335caedb">


## Prerequisites

Before you begin, ensure that you have the following tools installed:

- **Python**: To run the Python script and manage dependencies.
- **SQLite3**: To manage the SQLite database.
- **VS Code** : To edit the scripts and view the results.

