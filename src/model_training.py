import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_model(X, y):
    """Trains a RandomForest model and prints metrics."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    return model

if __name__ == "__main__":
    df = pd.read_csv("../data/customer_churn.csv")
    X = df.drop(columns=["Churn"])
    y = df["Churn"]
    
    trained_model = train_model(X, y)
    print("Model training completed.")

