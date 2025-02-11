import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import argparse
import sys

# Generate a synthetic dataset for credit risk assessment
def generate_dataset():
    np.random.seed(42)
    data = {
        "income": np.random.normal(50000, 15000, 1000),
        "loan_amount": np.random.normal(10000, 5000, 1000),
        "loan_duration": np.random.normal(36, 12, 1000),
        "credit_score": np.random.normal(650, 50, 1000),
        "default": np.random.choice([0, 1], size=1000, p=[0.8, 0.2])
    }
    return pd.DataFrame(data)

# Train a logistic regression model
def train_model(df):
    X = df[["income", "loan_amount", "loan_duration", "credit_score"]]
    y = df["default"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Model training complete.")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    return model

# CLI interface
def main():
    parser = argparse.ArgumentParser(description="Riskome CLI - Credit Risk Assessment Tool")
    parser.add_argument("--train", action="store_true", help="Train the credit risk model")
    parser.add_argument("--predict", nargs=4, metavar=("income", "loan_amount", "loan_duration", "credit_score"),
                        help="Predict credit risk with given features")

    args = parser.parse_args()

    if args.train:
        print("Generating synthetic dataset...")
        df = generate_dataset()
        print("Dataset generated. Training the model...")
        train_model(df)

    elif args.predict:
        try:
            income, loan_amount, loan_duration, credit_score = map(float, args.predict)
            print(f"\nPredicting credit risk for: Income: {income}, Loan Amount: {loan_amount}, "
                  f"Loan Duration: {loan_duration} months, Credit Score: {credit_score}\n")

            # Dummy prediction (since we're not loading the trained model)
            risk_score = (income - loan_amount) / loan_duration + credit_score / 100
            prediction = "High Risk" if risk_score < 200 else "Low Risk"
            print(f"Predicted Credit Risk: {prediction}")
        except ValueError:
            print("Invalid input. Please provide numerical values for all features.")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
