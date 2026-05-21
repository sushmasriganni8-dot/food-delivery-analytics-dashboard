import pandas as pd

df = pd.read_csv("Dataset/foodorders.csv")

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

df["transaction_type"] = df["transaction_type"].fillna("Unknown")

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nTOP SELLING FOOD ITEMS")
print(df["item_name"].value_counts())

total_revenue = df["transaction_amount"].sum()

print("\nTOTAL REVENUE")
print("₹", total_revenue)

average_order = df["transaction_amount"].mean()

print("\nAVERAGE ORDER VALUE")
print("₹", round(average_order, 2))

print("\nPEAK SALES TIME")
print(df["time_of_sale"].value_counts())

print("\nPAYMENT METHOD ANALYSIS")
print(df["transaction_type"].value_counts())

print("\nFOOD CATEGORY ANALYSIS")
print(df["item_type"].value_counts())
print("\nREVENUE BY FOOD ITEM")

print(df.groupby("item_name")["transaction_amount"].sum().sort_values(ascending=False))
print("\nREVENUE BY CATEGORY")

print(df.groupby("item_type")["transaction_amount"].sum())



import matplotlib.pyplot as plt

top_items = df["item_name"].value_counts()

top_items.plot(kind="bar")

plt.title("Top Selling Food Items")

plt.xlabel("Food Items")

plt.ylabel("Number of Orders")

plt.show()
payment_counts = df["transaction_type"].value_counts()

payment_counts.plot(kind="pie", autopct="%1.1f%%")

plt.title("Payment Method Distribution")

plt.ylabel("")

plt.show()
revenue_by_item = df.groupby("item_name")["transaction_amount"].sum()

revenue_by_item.plot(kind="bar")

plt.title("Revenue by Food Item")

plt.xlabel("Food Item")

plt.ylabel("Revenue")

plt.show()
sales_time = df["time_of_sale"].value_counts()

sales_time.plot(kind="bar")

plt.title("Orders by Time of Sale")

plt.xlabel("Time of Sale")

plt.ylabel("Number of Orders")

plt.show()
df.to_csv("Dataset/cleaned_foodorders.csv", index=False)

print("\nCleaned dataset saved successfully!")
