from sklearn.preprocessing import StandardScaler


def preprocess_data(df):
    numeric_df = df.select_dtypes(include=['number'])
    numeric_df = numeric_df.dropna()

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    # print("Data preprocessing complete.")
    return scaled_data


