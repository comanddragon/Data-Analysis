from sklearn.decomposition import PCA

def apply_pca(data, n_components):
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(data)

    # print(f"Explained variance by components: {pca.explained_variance_ratio_}")
    # print(f"Total explained variance: {sum(pca.explained_variance_ratio_) * 100:.2f}%")

    explained_variance = pca.explained_variance_ratio_
    print(f'Explained variance by PC1: {explained_variance[0]}')
    print(f'Explained variance by PC2: {explained_variance[1]}')


    return pca_result

