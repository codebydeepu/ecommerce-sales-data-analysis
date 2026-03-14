import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

#Loading the dataset using pandas and display: first 5 rows , last 5 rows and dataset shape
df = pd.read_csv("C:/Users/dipan/Downloads/Sample - Superstore.csv" , encoding="latin-1")
print("First 5 Rows")
print(df.head(5))
print("\nLast 5 Rows")
print(df.tail(5))
print("\nShape of Dataset")
print(df.shape)

#Checking the dataset information: column names , data types and missing values
print("\nColumn Names")
print(df.columns)
print("\n Data Types")
print(df.dtypes)
print("\nTotal number of Missing Values")
print(df.isnull().sum())

#Converting Order Date column to datetime format.
df["Order Date"] = pd.to_datetime(df["Order Date"])

#Finding and remove duplicate rows.
print(df.duplicated().sum())
df = df.drop_duplicates()

#Finding total sales, total profit, and total quantity sold.
Total_sales = df["Sales"].sum().round(2)
print(f"\nThe Total number of sales is {Total_sales}")
Total_profit = df["Profit"].sum().round(2)
print(f"The total number of Profit is {Total_profit}")
Total_quantity_sold = df["Quantity"].sum()
print(f"The total number of quantity sold is {Total_quantity_sold}")

#Finding top 10 best selling products based on sales.
Top_sell_product = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10).round(2)
print(f"\nThe Top 10 best selling products based on sales \n{Top_sell_product}")

#Finding sales by region.
Sales_Region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False).round(2)
print(f"\nThe sales by region \n{Sales_Region}")

#Finding monthly sales trend.
df["Monthly Sales"] = pd.to_datetime(df["Order Date"]).dt.month_name()
Monthly_Sales = df.groupby("Monthly Sales")["Sales"].sum().round(2)
print(f"\nThe monthly sales trend \n{Monthly_Sales}")

#Finding which category generates the most profit.
Top_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False).round(2)
print(f"\nThe category generates the most profit \n{Top_profit}")

#Using NumPy, calculate: mean sales , median sales and standard deviation
mean_sales = np.mean(df["Sales"]).round(2)
median_sales = np.median(df["Sales"]).round(2)
STD_sales = np.std(df["Sales"]).round(2)
print(f"\nThe sales mean is {mean_sales} ")
print(f"The sales medianis {median_sales} ")
print(f"The sales Standard deviation is {STD_sales} ")

#Creating a new column Profit Margin
df["Profit Margin"] = df["Profit"]/df["Sales"]

#Creating a bar chart showing sales by region.
plt.bar(Sales_Region.index, Sales_Region.values , color= "skyblue" , width=0.5 , label="Sales Data by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.legend()
plt.tight_layout()
plt.savefig("sales&region_bar_chart.png", dpi=300)
plt.show()

#Creating a line chart for monthly sales trend
plt.plot(Monthly_Sales.values, Monthly_Sales.index, marker="o" , color="green")
for x, y in zip(Monthly_Sales.values, Monthly_Sales.index):
    plt.text(x+500, y, str(round(x)), ha='center')
plt.xlabel("Sales")
plt.ylabel("Months")
plt.title("Monthly Sales trend")
plt.grid()
plt.tight_layout()
plt.savefig("Monthly_Sales_plot_chart.png", dpi=300)
plt.show()

#Creating a pie chart showing sales distribution by category.
category_sales = df.groupby("Category")["Sales"].sum()
plt.pie(category_sales.values ,autopct="%1.1f%%",labels=category_sales.index,startangle=90)
plt.axis("equal")
plt.title("Sales Distributiom")
plt.tight_layout()
plt.savefig("category&sales_distribution_pie.png",dpi = 300)
plt.show()

#Final Insight
print("\nFinal Insight")
print("1) After analyzing sales across regions, we observed that West Region generates the highest revenue.")
print("2) The analysis shows that Technology contributes the most profit.")
print("3) The product Canon imageCLASS 2200 Advanced Copier has the highest total sales")
print("4) The monthly sales trend shows fluctuations across the year " \
"Some months experience significantly higher sales , November and December Months have higher sales")
print('''5) Higher sales do not always guarantee higher profit.
Some products generate high revenue but have low profit margins, possibly due to higher discounts or operational costs.''')
