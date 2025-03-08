from sklearn.cluster import KMeans

def apply_kmeans(data, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = kmeans.fit_predict(data)

    print(f"K-Means clustering completed with {n_clusters} clusters.")
    return clusters
