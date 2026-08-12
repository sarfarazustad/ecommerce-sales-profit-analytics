-- E-Commerce Sales & Profit Analytics
-- SQL analysis queries

-- 1. Total Revenue
SELECT SUM(Quantity * UnitPrice) AS Total_Revenue
FROM orders;

-- 2. Total Units Sold
SELECT SUM(Quantity) AS Total_Units_Sold
FROM orders;

-- 3. Revenue by Product
SELECT ProductID,
       SUM(Quantity * UnitPrice) AS Revenue
FROM orders
GROUP BY ProductID
ORDER BY Revenue DESC;

-- 4. Top 10 Products by Revenue
SELECT ProductID,
       SUM(Quantity * UnitPrice) AS Revenue
FROM orders
GROUP BY ProductID
ORDER BY Revenue DESC
LIMIT 10;

-- Add further project-specific SQL analysis queries here.
