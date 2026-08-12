import pandas as pd






customer = pd.read_csv(
    "C:/Users/Admin/Downloads/Ecommerce_Sales_Profit_Analytics/Ecommerce_Sales_Profit_Analytics/data/customers.csv"
)

orders = pd.read_csv(
    "C:/Users/Admin/Downloads/Ecommerce_Sales_Profit_Analytics/Ecommerce_Sales_Profit_Analytics/data/orders.csv"
)

products = pd.read_csv(
    "C:/Users/Admin/Downloads/Ecommerce_Sales_Profit_Analytics/Ecommerce_Sales_Profit_Analytics/data/products.csv"
)

print("Files loaded successfully!")




customer.head()
orders.head()




customer.info()
orders.info()
products.info()



print(customer.isnull().sum())
print(orders.isnull().sum())
print(products.isnull().sum())



print(customer.duplicated().sum())
print(orders.duplicated().sum())
print(products.duplicated().sum())



orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])



df = orders.merge(
customer,
on="CustomerID",
how="left"
)
df = df.merge(
products,
on="ProductID",
how="left"
)



df.head



df.shape



print(customer.isnull().sum())
print(orders.isnull().sum())
print(products.isnull().sum())



Total_Revenue= df["Revenue"].sum()
print(Total_Revenue)



Total_Profit = df["Profit"].sum()
print(Total_Profit)



Total_Orders = df["OrderID"].nunique()
print(Total_Orders)



Total_Customers =  df["CustomerID"].nunique()
print(Total_Customers)



Total_Quantity =  df["Quantity"].sum()
print(Total_Quantity)



Profit_Margin = (df["Profit"].sum()/df["Revenue"].sum())*100
print(Profit_Margin)



df["Monthly"]=df["OrderDate"].dt.to_period('M')




Monthly_Sales = df.groupby("Monthly")["Revenue"].sum()
print(Monthly_Sales)



Monthly_Profit = df.groupby("Monthly")["Profit"].sum()
print(Monthly_Profit)



Monthly_Sales.idxmax()



Category_Sales = (
 df.groupby("Category")["Revenue"]
    .sum()
    .sort_values (ascending = False)
)
print(Category_Sales)
    



Category_Profit=  (
 df.groupby("Category")["Profit"]
    .sum()
    .sort_values (ascending = False)
)
print(Category_Profit)



Region_Analysis = df.groupby("Region").agg(
    Revenue = ("Revenue", "sum"),
    Profit = ("Profit", "sum"),
    Orders = ("OrderID", "nunique")
)
print(Region_Analysis)



Segment_Analysis = df.groupby("Segment").agg(
    Revenue = ("Revenue", "sum"),
    Profit = ("Profit", "sum"),
    Orders = ("OrderID", "nunique"),
    Customer = ("CustomerID", "nunique")
)
print(Segment_Analysis)



Top_Products = (
    df.groupby(["ProductID","Category","SubCategory"])
.agg (
    Revenue = ("Revenue", "sum"),  
    Profit = ("Profit", "sum"),
    Quantity = ("Quantity","sum")
)
.sort_values("Revenue", ascending = False)
.head(10)
)
print(Top_Products)



Top_Customers = (
    df.groupby("CustomerID")
    .agg (
        Revenue = ("Revenue","sum"),
        Profit = ("Profit","sum"),
        Orders = ("OrderID","nunique")
    )
    .sort_values("Revenue", ascending = False)
    .head(10)
)
print(Top_Customers)



df["Status"].value_counts()



Returned = df[df["Status"] == "Returned"]
Returned_revenue = Returned["Revenue"].sum()
print(Returned_revenue)



Return_rate = (
    (df["Status"]== "Returned").sum()
    / len(df)
)*100
print(Return_rate)



Discount_Analysis = df.groupby("Discount").agg(
    Revenue = ("Revenue", "sum"),
    Profit = ("Profit", "sum"),
    Orders = ("OrderID", "nunique")
)
print(Discount_Analysis)



Payment_Analysis = df.groupby("PaymentMethod").agg(
    Revenue = ("Revenue", "sum"),
    Profit = ("Profit", "sum"),
    Orders = ("OrderID", "nunique")
)
print(Payment_Analysis)




import matplotlib.pyplot as plt
import seaborn as sns




df["Month"] = df["OrderDate"].dt.to_period("M")

monthly_revenue = df.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_revenue.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)
plt.figure(figsize=(10, 6))

region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



segment_sales = df.groupby("Segment")["Revenue"].sum()

plt.figure(figsize=(8, 8))

plt.pie(
    segment_sales.values,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Revenue by Customer Segment")

plt.show()



top_products = (
    df.groupby("ProductID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

top_products.plot(kind="barh")

plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product ID")

plt.tight_layout()
plt.show()



monthly = df.groupby("Month").agg(
    Revenue=("Revenue", "sum"),
    Profit=("Profit", "sum")
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly.index.astype(str),
    monthly["Revenue"],
    marker="o",
    label="Revenue"
)

plt.plot(
    monthly.index.astype(str),
    monthly["Profit"],
    marker="o",
    label="Profit"
)

plt.title("Monthly Revenue vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()



payment_orders = df.groupby("PaymentMethod")["OrderID"].nunique()

plt.figure(figsize=(10, 6))

payment_orders.plot(kind="bar")

plt.title("Orders by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()



plt.savefig(
    "charts/01_Monthly_Revenue.png",
    dpi=300,
    bbox_inches="tight"
)



df.head()



df.to_csv("cleaned_data.csv", index=False)



import os

os.listdir()



cleaned_df = pd.read_csv("cleaned_data.csv")

cleaned_df.head()



print(cleaned_df.shape)






































