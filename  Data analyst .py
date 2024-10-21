import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\kovid\OneDrive\Desktop\Amazon Sale Report (1).csv')

# 1. Sales Overview
# Convert 'Date' to datetime format with specified format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')  # Specify the format

df['Year'] = df['Date'].dt.year

# Calculate total sales per year
sales_overview = df.groupby('Year')['Amount'].sum()

# Plotting sales overview
plt.figure(figsize=(10, 6))
sales_overview.plot(kind='bar', color='skyblue')
plt.title('Total Sales per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales Amount (INR)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 2. Product Analysis
# Count the number of products sold by category
product_distribution = df['Category'].value_counts()

# Plotting product distribution
plt.figure(figsize=(10, 6))
product_distribution.plot(kind='bar', color='lightgreen')
plt.title('Product Distribution by Category')
plt.xlabel('Product Category')
plt.ylabel('Number of Products Sold')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# 3. Fulfillment Analysis
# Count fulfillment methods
fulfillment_analysis = df['Fulfilment'].value_counts()

# Plotting fulfillment analysis
plt.figure(figsize=(10, 6))
fulfillment_analysis.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Fulfillment Methods')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 4. Customer Segmentation
# Segment customers based on quantity purchased
customer_segmentation = df.groupby('Order ID')['Qty'].sum().describe()

print("Customer Segmentation Summary:")
print(customer_segmentation)

# 5. Geographical Analysis
# Count sales by state
geographical_distribution = df['ship-state'].value_counts()

# Modified plotting for clarity
plt.figure(figsize=(15, 8))  # Increased figure size for better clarity
geographical_distribution.plot(kind='bar', color='coral')

plt.title('Sales Distribution by State', fontsize=20)  # Increased title font size
plt.xlabel('State', fontsize=16)  # Increased x-axis label font size
plt.ylabel('Number of Sales', fontsize=16)  # Increased y-axis label font size

# Rotating x-axis labels for clarity
plt.xticks(rotation=45, ha='right', fontsize=12)  # Adjusted rotation, alignment, and font size for better readability
plt.grid(axis='y')

# Adding some space to avoid label clipping
plt.tight_layout()

# Display the plot
plt.show()

# 6. Business Insights
# Provide insights based on analysis
total_sales = df['Amount'].sum()
most_popular_product = product_distribution.idxmax()
most_profitable_category = df.groupby('Category')['Amount'].sum().idxmax()

print(f"\nTotal Sales Amount: {total_sales} INR")
print(f"Most Popular Product Category: {most_popular_product}")
print(f"Most Profitable Product Category: {most_profitable_category}")
