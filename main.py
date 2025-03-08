from scripts.data_loader import load_data
from scripts.data_preprocessing import preprocess_data
from scripts.pca_analysis import apply_pca
from scripts.clustering import apply_kmeans
from scripts.visualization import plot_clusters


file_path = "data/project.xlsx"
df = load_data(file_path)
print(df.head())


if df is not None:
    scaled_data = preprocess_data(df)

    pca_data = apply_pca(scaled_data, n_components=2)

    clusters = apply_kmeans(pca_data, n_clusters=2)

    plot_clusters(pca_data, clusters)

