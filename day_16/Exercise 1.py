import pandas as pd
import numpy as np

# -----------------------------
# Creating Sample Data
# -----------------------------

customers = pd.DataFrame({
    "Customer_ID":[1,2,3,4],
    "Name":["Ali","Sara","John","Anna"],
    "City":["Lahore","Karachi","Lahore","Islamabad"],
    "Age":[22,35,28,42]
})

orders = pd.DataFrame({
    "Customer_ID":[1,2,2,3,4,1],
    "Product":["Laptop","Phone","Tablet","Laptop","Camera","Mouse"],
    "Amount":[1200,800,300,1100,500,50]
})

# print("Customers Data")
# print(customers)

# print("\nOrders Data")
# print(orders)


# -----------------------------
# Concatenation
# -----------------------------
df1 = pd.DataFrame({"A":[1,2],"B":[3,4]})
df2 = pd.DataFrame({"A":[5,6],"B":[7,8]})

concat_df = pd.concat([df1,df2])
# print("\nConcatenated Data")
# print(concat_df)


# -----------------------------
# Merge / Joins
# -----------------------------

inner_join = pd.merge(customers,orders,on="Customer_ID",how="inner")
left_join = pd.merge(customers,orders,on="Customer_ID",how="left")
right_join = pd.merge(customers,orders,on="Customer_ID",how="right")
outer_join = pd.merge(customers,orders,on="Customer_ID",how="outer")

print("\nInner Join")
print(inner_join)
print("________________________________")
print("\nleft_join")
print(left_join)
print("________________________________")

print("\nright_join")
print(right_join)
print("________________________________")

print("\nouter Join")
print(outer_join)
# # -----------------------------
# # GroupBy
# # -----------------------------
# city_sales = inner_join.groupby("City")["Amount"].sum()
# print("\nTotal Sales per City")
# print(city_sales)


# # -----------------------------
# # Discretization / Binning
# # -----------------------------
# bins = [0,25,40,60]
# labels = ["Young","Adult","Senior"]

# customers["Age_Group"] = pd.cut(customers["Age"],bins=bins,labels=labels)

# print("\nCustomers with Age Groups")
# print(customers)


# # -----------------------------
# # DataFrame Operations
# # -----------------------------

# print("\nHead")
# print(inner_join.head())

# print("\nUnique Cities")
# print(customers["City"].unique())

# print("\nValue Counts")
# print(customers["City"].value_counts())


# # -----------------------------
# # Saving Data
# # -----------------------------

# inner_join.to_csv("sales_data.csv",index=False)
# customers.to_excel("customers.xlsx",index=False)

# print("\nFiles saved successfully")