# PRODIGY_ML_02
# 🛍️ Customer Segmentation using K-Means Clustering

This project uses **K-Means Clustering** to segment customers of a retail store based on their purchasing behavior.

---

## 🎯 Objective

To help a retail store better understand its customer base by:
- Grouping customers into meaningful clusters
- Identifying distinct spending behaviors
- Enabling targeted marketing and personalized service

---

## 📊 Features Used

- **Annual Income (k$)**
- **Spending Score (1–100)**  
_(You can add more features like Age, Gender, Purchase Frequency, etc.)_

---

## 🚀 How It Works

1. **Preprocessing**: Input features are scaled using `StandardScaler`.
2. **KMeans Clustering**: Customers are grouped based on feature similarity.
3. **Elbow Method**: Determines the optimal number of clusters `k`.
4. **Visualization**: Scatter plot to show clusters and centroids.

---

## 📁 Dataset

The dataset should be a CSV file with columns like:

| CustomerID | Annual Income (k$) | Spending Score (1-100) |
|------------|--------------------|-------------------------|
| 1          | 15                 | 39                      |
| 2          | 16                 | 81                      |
| ...        | ...                | ...                     |

You can download a popular version of this dataset from:
[Kaggle - Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

---

## 🧪 Sample Output

- The script will show an **Elbow Plot** to help you choose the best number of clusters.
- Then it visualizes the **customer segments** with centroids.

![Elbow Method](images/elbow_plot.png)
![Customer Clusters](images/customer_clusters.png)

---

## 📦 Requirements

```bash
pip install pandas matplotlib scikit-learn
