import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load CSV
df = pd.read_csv("food (2).csv")

# Nutritional numeric columns
features = [
    "Data.Carbohydrate",
    "Data.Fiber",
    "Data.Kilocalories",
    "Data.Protein",
    "Data.Sugar Total",
    "Data.Water",
    "Data.Fat.Saturated Fat",
    "Data.Fat.Total Lipid"
]

X = df[features]

# Handle missing values
X = X.fillna(X.mean())

# Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method: k = 2 to 10
wcss = []

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot elbow curve
plt.plot(range(2, 11), wcss, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method for k-Means")
plt.grid(True)
plt.show()