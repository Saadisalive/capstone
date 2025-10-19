import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/Programmer/Downloads/IMDB Dataset.csv")

print("First 3 rows:")
print(df.head(3))
print("\nLast 3 rows:")
print(df.tail(3))

print("\nDataset Info:")
print(df.info())

print("\nNull values in dataset:")
print(df.isnull().sum())

subset = df.iloc[40:75]
print("\nSubset (Rows 41–75):")
print(subset)

if "No_of_Votes" in df.columns:
    highest_votes = df.loc[df["No_of_Votes"].idxmax()]
    print("\nMovie with Highest Votes:")
    print(highest_votes)
else:
    print("\nColumn 'No_of_Votes' not found in dataset.")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df["IMDB_Rating"], color="orange")
plt.title("Boxplot of IMDB Rating")

plt.subplot(1, 2, 2)
sns.boxplot(y=df["Runtime"], color="lightblue")
plt.title("Boxplot of Runtime")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["Runtime"], df["IMDB_Rating"], color="purple", alpha=0.6)
plt.title("IMDB Rating vs Runtime")
plt.xlabel("Runtime (minutes)")
plt.ylabel("IMDB Rating")
plt.show()

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(df["IMDB_Rating"], kde=True, color="salmon")
plt.title("Distribution of IMDB Rating")

plt.subplot(1, 2, 2)
sns.histplot(df["Runtime"], kde=True, color="green")
plt.title("Distribution of Runtime")
plt.tight_layout()
plt.show()

if "Rating" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(x="Rating", data=df, palette="coolwarm")
    plt.title("Count of Movies by Rating")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("\nColumn 'Rating' not found in dataset.")
