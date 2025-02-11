
# Riskome CLI & Telegram Bot for Credit Risk Assessment

**Riskome** is a credit risk assessment tool that helps users predict the likelihood of loan defaults using machine learning. It is available as both a **Command-Line Interface (CLI)** and a **Telegram Bot** for easy interaction.

## Features  
- **Command-Line Interface (CLI)** for local use  
- **Telegram Bot Integration** for real-time interaction and predictions  
- **Custom Model Training** using uploaded CSV files  
- Predict whether a user is a **High Risk** or **Low Risk**  
- Supports machine learning model training and predictions from user data  

---

## Telegram Bot Instructions  
### Step 1: Start the Bot  
1. Open Telegram and search for the bot using the handle provided.  
2. Click **Start** to begin. The bot will respond with a welcome message.  

### Step 2: Upload a CSV File  
1. The CSV file should contain:  
   - **Feature columns** in the first columns  
   - **Target variable** (label) in the last column  

   Example dataset format:  
   | Age | Income | Loan Amount | Default |  
   |-----|--------|-------------|---------|  
   | 35  | 45000  | 15000       | 0       |  
   | 45  | 60000  | 25000       | 1       |  

2. The bot will automatically train the model on the uploaded data.  

### Step 3: Make Predictions  
- Type any text message to predict the risk based on the previously trained model.  
- The bot will respond with **High Risk** or **Low Risk**.  

---

## CLI Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Riskome/RisKome.git
   ```
2. Run the CLI using Python:  
   ```bash
   python riskome_cli.py
   ```
3. Follow the on-screen instructions to upload data, train the model, and make predictions.

---

## Technology Stack  
- **Python**  
- **scikit-learn** for Machine Learning  
- **Telegram Bot API**  
- **pandas** for data manipulation


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

