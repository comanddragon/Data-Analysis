import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    numeric_df = df.select_dtypes(include=['number'])

    numeric_df = numeric_df.fillna(numeric_df.mean())

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)

    scaled_df = pd.DataFrame(scaled_data, columns=numeric_df.columns)

    print("Data preprocessing complete. Shape:", scaled_df.shape)
    return scaled_df
