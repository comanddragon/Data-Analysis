import matplotlib.pyplot as plt

def plot_pca(pca_data):
    # Scatter plot of the first two principal components (PC1 vs. PC2)
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_data[:, 0], pca_data[:, 1], c='blue', alpha=0.7)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA: PC1 vs PC2')
    plt.show()

def plot_clusters(pca_data, clusters):
    plt.figure(figsize=(8,6))
    plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters, cmap='viridis', alpha=0.7)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA + K-Means Clustering')
    plt.colorbar(label='Cluster')
    plt.show()

