import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Handles missing values and corrects data types."""
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)
    return df

def scale_features(df, numeric_columns):
    """Standardizes numerical features."""
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df

if __name__ == "__main__":
    df = load_data("../data/customer_churn.csv")
    df = clean_data(df)
    df = scale_features(df, ["Tenure", "MonthlyCharges", "TotalCharges"])
    print("Data preprocessing completed.")

