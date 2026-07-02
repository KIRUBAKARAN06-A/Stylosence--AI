import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stylosense"
)

cursor = conn.cursor()

# Read cleaned data
df = pd.read_csv("../dataset/cleaned_customer_data.csv")

# Insert data into database
for _, row in df.iterrows():
    query = """
    INSERT INTO customers
    (customer_id, height, weight, body_type, style)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        row["customer_id"],
        row["height"],
        row["weight"],
        row["body_type"],
        row["style"]
    )

    cursor.execute(query, values)

conn.commit()

print("Data loaded successfully!")

cursor.close()
conn.close()
