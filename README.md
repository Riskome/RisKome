Riskome – AI-Powered Credit Risk Assessment

**Riskome** is a lightweight yet powerful credit risk assessment tool built with Python and machine learning. It includes:

- ✅ Logistic Regression and Random Forest models  
- 🤖 Telegram bot for real-time risk prediction  
- 📊 Synthetic and user-uploaded CSV data support  
- ⚡ CLI-based interface for quick predictions  

---

## 📦 Features

- Upload a CSV and train a model on the go.  
- Predict if a user is **High Risk** or **Low Risk** using:
  - Income  
  - Loan Amount  
  - Loan Duration  
  - Credit Score  
- Real-time Telegram bot interface for risk checks.  
- Command-line interface (CLI) for offline predictions.  

---

## 💻 Technologies Used

| Language/Tool     | Purpose                          |
|------------------|----------------------------------|
| `Python`         | Core programming                 |
| `scikit-learn`   | Machine Learning Models          |
| `pandas`, `numpy`| Data preprocessing & generation  |
| `argparse`       | CLI interface                    |
| `Telegram Bot API` | Chat-based user interaction   |
| `logging`        | Debugging & monitoring           |
| `Colab / Jupyter`| Prototyping & visualization      |

---

## 🚀 Getting Started

### 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

### 🧪 Run in CLI Mode

Train the model with synthetic data:

```bash
python riskome.py --train
```

Make a prediction:

```bash
python riskome.py --predict 45000 10000 24 670
```

> Output: `Predicted Credit Risk: Low Risk` or `High Risk`

---

### 💬 Run Telegram Bot (Live Predictions)

In `riskome_bot.py`, replace the placeholder with your bot token:

```python
ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
```

Then start the bot:

```bash
python riskome_bot.py
```

- Use `/start` to begin  
- Upload a CSV file to train the model  
- Send a message like: `45000, 10000, 24, 670` to get predictions

---

## 📁 Sample CSV Format

```
income,loan_amount,loan_duration,credit_score,default
50000,10000,36,680,0
30000,15000,24,620,1
...
```

---

## 🛠 Future Improvements

- Add model explainability (SHAP/LIME)  
- Integrate a user database  
- Streamlit web dashboard  
- Docker container setup for cloud use  

---



 Riskome was built  to simulate real-world loan approval systems with fun integrations like Telegram bots, CLI tools, and predictive modeling — all using open-source tech.



---

## 📜 License

This project is licensed under the MIT License.

---

