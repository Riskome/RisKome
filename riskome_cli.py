
import random

def predict_risk(age, income, loan_amount):
    prediction = random.choice(["Low Risk", "High Risk"])
    return prediction

def run_cli():
    print("Welcome to RiskOme - Credit Risk Assessment AI Agent!")
    age = 30
    income = 40000
    loan_amount = 15000

    risk_level = predict_risk(age, income, loan_amount)
    print(f"Risk Assessment Result: {risk_level}")

run_cli()
