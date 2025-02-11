# **Riskome CLI**  
Riskome CLI is a command-line interface tool designed for credit risk assessment. It utilizes a regression model to train on synthetic datasets and predict credit risk based on key financial indicators. The CLI offers an easy way to interact with the model, train it, and make predictions.

## **Features**  
- **Train a Regression Model**: Automatically generate synthetic datasets and train a credit risk model.  
- **Predict Credit Risk**: Input financial details to predict the likelihood of loan default.  
- **Command-Line Simplicity**: All interactions are done via an intuitive command-line interface.

## **Installation**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Riskome/RisKome.git  
   ```  

2. Navigate to the project directory:  
   ```bash
   cd RisKome  
   ```  

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt  
   ```

## **Usage**  
1. **Train the Model**  
   Train the regression model on a synthetic dataset:  
   ```bash
   python riskome_cli.py --train  
   ```

2. **Make a Prediction**  
   Use the CLI to predict credit risk. Input financial indicators such as income, loan amount, and credit score:  
   ```bash
   python riskome_cli.py --predict '{"income": 5000, "loan_amount": 20000, "credit_score": 700}'  
   ```

   Example output:  
   ```  
   Predicted default risk: Low  
   ```  

3. **View Help**  
   Display all available commands:  
   ```bash
   python riskome_cli.py --help  
   ```

## **Sample Data**  
The model trains on a synthetic dataset generated internally. No external data is required to get started.  


---
### RiskOme AI Agent
🚀 **RiskOme AI Agent** analyzes credit risk and provides tweet-ready insights for Automatic updates on [X (Twitter)](https://twitter.com/Riskome).

**Follow our journey and updates on X:** [@Riskome](https://twitter.com/Riskoome)


### **Contributing**
Feel free to fork this repository and contribute. Suggestions and improvements are always welcome!

---

### **License**
This project is licensed under the **MIT License**. You’re free to modify and distribute it.

---

