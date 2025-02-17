import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def encode_categorical(df, categorical_columns):
    """One-hot encodes categorical features."""
    encoder = OneHotEncoder(sparse_output=False, drop="first")
    encoded_cols = encoder.fit_transform(df[categorical_columns])
    df_encoded = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_columns))
    df = df.drop(columns=categorical_columns).reset_index(drop=True)
    return pd.concat([df, df_encoded], axis=1)

if __name__ == "__main__":
    df = pd.read_csv("../data/customer_churn.csv")
    df = encode_categorical(df, ["Contract", "PaymentMethod"])
    print("Feature engineering completed.")

