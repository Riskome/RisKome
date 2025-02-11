import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Initialize the model variable globally
model = None

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to Riskome! 🧮\n"
        "Upload a CSV file to train the credit risk model.\n"
        "Once trained, you can input new data for predictions in this format:\n"
        "`1.0, 23.5, 5000, 0`\n"
        "Features should be separated by commas.", parse_mode="Markdown"
    )

# CSV file handler
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global model
    file = await context.bot.get_file(update.message.document.file_id)
    file_path = "data.csv"
    await file.download_to_drive(file_path)
    await update.message.reply_text("📂 CSV file uploaded. Training the model...")

    try:
        # Load CSV file
        data = pd.read_csv(file_path)
        X = data.iloc[:, :-1].values  # Features
        y = data.iloc[:, -1].values  # Target variable

        # Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the Random Forest model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        await update.message.reply_text("✅ Model training completed successfully! You can now send feature data for prediction.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error in training the model: {e}")

# Prediction command
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global model
    if model is None:
        await update.message.reply_text("⚠️ Please upload a CSV to train the model first.")
        return

    user_input = update.message.text
    try:
        # Convert user input into a list of floats
        input_data = [float(x) for x in user_input.split(",")]
        prediction = model.predict([input_data])[0]

        # Interpret the prediction
        if prediction == 1:  # Assuming '1' means high risk and '0' means low risk
            await update.message.reply_text("⚠️ High Risk: This user is considered high credit risk. Please proceed with caution.")
        else:
            await update.message.reply_text("✅ Low Risk: This user is considered low credit risk.")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error in prediction. Please provide input as comma-separated feature values.\nExample: 1.0, 23.5, 5000, 0")

# Main function to run the bot
if __name__ == "__main__":
    application = ApplicationBuilder().token(😘:AAGFOmureLINJe5P1D-SiaBW10e0Nm8qMhk").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_file))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, predict))

    print("Bot is running...")
    application.run_polling()
