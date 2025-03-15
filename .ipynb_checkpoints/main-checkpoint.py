from scripts.data_loader import load_data
from scripts.data_preprocessing import preprocess_data
from scripts.pca_analysis import apply_pca
from scripts.clustering import apply_kmeans
from scripts.visualization import *
from scripts.one_hot_encoder import one_hot_encoder


file_path = "data/project.xlsx"
df = load_data(file_path)
print(df.head())


if df is not None:
    dp = one_hot_encoder(file_path)

    scaled_data = preprocess_data(dp)

    pca_data = apply_pca(scaled_data, n_components=3)

    plot_pca(pca_data)

    clusters = apply_kmeans(pca_data, n_clusters=4)

    plot_clusters(pca_data, clusters)

