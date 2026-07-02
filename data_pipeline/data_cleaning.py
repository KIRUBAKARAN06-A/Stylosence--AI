import pandas as pd

# Load customer data
df = pd.read_csv("../dataset/customer_data.csv")

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Display cleaned data
print("Cleaned Customer Data:")
print(df)

# Save cleaned data
df.to_csv("../dataset/cleaned_customer_data.csv", index=False)

print("Data cleaning completed successfully!")
