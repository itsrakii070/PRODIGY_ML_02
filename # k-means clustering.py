# k-means clustering
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv("Mall_Customers.csv")

# Preview the data
print(data.head())

# Optional: drop 'CustomerID' and 'Genre' for clustering
X = data.drop(['CustomerID', 'Gender'], axis=1)


sns.pairplot(X)
plt.show()

inertia = []
K = range(1, 11)
for k in K:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    inertia.append(model.inertia_)

# Plot elbow
plt.figure(figsize=(8,5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia (Within-cluster sum of squares)')
plt.title('Elbow Method For Optimal K')
plt.grid(True)
plt.show()


k_optimal = 5
model = KMeans(n_clusters=k_optimal, random_state=42)
clusters = model.fit_predict(X)

X['Cluster'] = clusters

plt.figure(figsize=(8,6))
sns.scatterplot(
    data=X, x='Annual Income (k$)', y='Spending Score (1-100)', 
    hue='Cluster', palette='Set1', s=100
)
plt.title('Customer Segments by Annual Income & Spending Score')
plt.grid(True)
plt.show()

# Optional: Save clustered data
X.to_csv("clustered_customers.csv", index=False)
