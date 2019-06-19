import csv

with open("budget_data.csv") as file:
    reader = csv.reader(file)
 
import pandas as pd
df = pd.read_csv("budget_data.csv")

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {df['Date'].count()}")
print(f"Total: ${df['Profit/Losses'].sum()}")

df['shifted_column'] = df['Profit/Losses'].shift(1)
df['difference'] = df['Profit/Losses'] - df['shifted_column']
average = df['difference'].mean()
maximum = df['difference'].max()
minimum = df['difference'].min()
      
GI_Date = df.sort_values("Profit/Losses").tail(1).Date
GD_Date = df.sort_values("Profit/Losses").head(1).Date
print(f"Average Change: {average}")
print("Greatest Increase in Profits: %s %s" %(GI_Date.to_string(index=False), maximum))
print("Greatest Decrease in Profits: %s %s" %(GD_Date.to_string(index=False), minimum))
