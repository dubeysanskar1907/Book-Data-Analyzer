import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/books.csv")

df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

rating_map = {"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
df["Rating"]=df["Rating"].map(rating_map)

sns.countplot(x="Rating",data=df)
plt.title("Book Rating Distribution")
plt.savefig("results/rating_distribution.png")
plt.show()
sns.histplot(df["Price"],bins=20)
plt.title("Book Price Distribution")
plt.savefig("results/price_distribution.png")
plt.show()

sns.boxplot(x="Rating",y="Price",data=df)
plt.title("Price vs Rating")
plt.savefig("results/price_vs_rating.png")
plt.show()