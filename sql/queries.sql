-- Count the total number of records in the dataset
SELECT COUNT(*) AS Total_Records FROM car_sales;

-- Calculate the total and average MSRP (price) from the car_sales dataset
SELECT 
    SUM(MSRP) AS Total_MSRP, 
    AVG(MSRP) AS Average_MSRP 
FROM car_sales;

-- Filter records where Engine_HP is greater than 300
SELECT * 
FROM car_sales 
WHERE Engine_HP > 300;
