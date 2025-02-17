import pandas as pd
import joblib

def load_model(model_path):
    """Loads a trained model."""
    return joblib.load(model_path)

def make_prediction(model, new_data):
    """Makes predictions on new customer data."""
    return model.predict(new_data)

if __name__ == "__main__":
    model = load_model("../models/churn_model.pkl")
    
    new_data = pd.DataFrame({
        "Tenure": [10], "MonthlyCharges": [70], "TotalCharges": [700]
    })
    
    prediction = make_prediction(model, new_data)
    print("Prediction:", prediction)

