import pandas as pd 

df = pd.read_csv("data/books.csv")

df["price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

rating_map = {
    "One":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5
}

df["Rating"] = df["Rating"].map(rating_map)

print("Average price :",df["price"].mean())

print("\nTop 5 expensive books")
print(df.sort_values("price",ascending=False).head())

print("\nBooks per rating")
print(df["Rating"].value_counts())