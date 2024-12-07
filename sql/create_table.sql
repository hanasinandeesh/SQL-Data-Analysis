-- SQL script to create the car_sales table
DROP TABLE IF EXISTS car_sales;

CREATE TABLE car_sales (
    Make TEXT,
    Model TEXT,
    Year INTEGER,
    Engine_Fuel_Type TEXT,
    Engine_HP REAL,
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
