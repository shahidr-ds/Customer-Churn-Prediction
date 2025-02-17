from src.data_preprocessing import load_data, clean_data, scale_features
from src.feature_engineering import encode_categorical
from src.model_training import train_model

if __name__ == "__main__":
    print("Starting churn prediction pipeline...")
    
    df = load_data("data/customer_churn.csv")
    df = clean_data(df)
    df = scale_features(df, ["Tenure", "MonthlyCharges", "TotalCharges"])
    
    df = encode_categorical(df, ["Contract", "PaymentMethod"])
    
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    
    model = train_model(X, y)
    
    print("Pipeline execution completed.")

