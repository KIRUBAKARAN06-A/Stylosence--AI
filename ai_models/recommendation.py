import pandas as pd

# Load customer data
df = pd.read_csv("../dataset/customer_data.csv")

def recommend_style(height, weight, body_type, occasion):
    if occasion.lower() == "formal":
        return "Black Blazer, White Shirt, Formal Pant"

    elif occasion.lower() == "party":
        return "Premium Suit with Leather Shoes"

    elif occasion.lower() == "casual":
        return "T-Shirt, Jeans and Sneakers"

    elif occasion.lower() == "sports":
        return "Sports T-Shirt and Track Pant"

    else:
        return "No recommendation available"

# Example
customer = df.iloc[0]

dress = recommend_style(
    customer["height"],
    customer["weight"],
    customer["body_type"],
    customer["style"]
)

print("Recommended Dress:")
print(dress)
