# PhishPersona ML Model

## 📌 Project Overview
**PhishPersona** is a machine learning-based phishing email detection system built using a transformer-based text classification approach. The model uses a **BERT-based architecture** for analyzing email content and predicting whether the email is **phishing or safe**.

The system is designed for cybersecurity applications to prevent social engineering attacks by providing probability-based phishing detection.

---

## 🚀 Problem Statement
The goal of this project is to classify email text into:

- **Phishing Email**
- **Safe Email**

This is a **supervised binary text classification problem** where the model outputs phishing probability between **0 and 1**.

---

## 🤖 Model Architecture

- Base Model: BERT Transformer Encoder
- Task: Sequence Classification
- Output Layer: Sigmoid activation for phishing probability scoring
- Loss Function: Binary Cross Entropy Loss
- Optimization: AdamW Optimizer

The model processes email text using tokenization followed by contextual embedding extraction.

---

## 📂 Project Structure
phishpersona/
│
├── app.py # Flask web application
├── model/
│ ├── tokenizer/ # BERT tokenizer files
│ ├── classifier_model/ # Trained ML model weights
│
├── dataset/
│ └── training_data.json # Training dataset
│
├── user_profile.json # User profile storage
├── requirements.txt # Dependencies
└── README.md

---

## 📊 Dataset Information

The model was trained on a curated phishing and legitimate email dataset containing:

- Email body text
- Label (0 = Safe, 1 = Phishing)

Dataset preprocessing steps include:
- Text cleaning
- Tokenization
- Padding and truncation
- Label encoding

---

## 🧠 Training Pipeline

1. Collect labeled email dataset
2. Preprocess email text
3. Tokenize using BERT tokenizer
4. Train sequence classification model
5. Validate using test dataset
6. Save trained model weights

---

## 🔧 Installation

### 1. Clone Repository
```bash
git clone https://github.com/Saipavansvarada/phishpersona.git
cd phishpersona
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate       # Windows
pip install -r requirements.txt #for installing dependencies
python app.py #ues this for running application

The applicatin will run on LOCALHOST - http://127.0.0.1:5000

📡 API Usage
Predict Email Phishing Probability
Endpoint: /predict
Method: POST
Input Format:
{
  "email_text": "Sample email content here"
}
Output format :
{
  "phishing_probability": 0.87,
  "prediction": "Phishing"
}

📈 Performance Metrics

The model performance is evaluated using:
-Accuracy
-Precision
-Recall
-F1 Score
-ROC-AUC Score

🔐 Security Features

-Session-based authentication
-Input validation
-Noise-resistant prediction pipeline
-Probability thresholding

🛠 Technologies Used

-Python
-PyTorch
-Transformers Library
-Flask
-NumPy
-JSON Storage

🌱Future Improvements

-Multi-language phishing detection
-URL feature extraction
-Hybrid ML + Rule-based detection
-Adversarial phishing pattern detection
-Real-time email scanning extension

👨‍💻 Author

 PhishPersona Development Team
  _Members_
  -Saipavan.S.Varada- 1rx24css215
  -Sahajal katiyar - 1rn24cs225
  -Saayi gagan AV- 1rn24cs220
  -SMD Aqueeluddin -1rn24cs218

⭐ Acknowledgement

This project utilizes transformer-based natural language processing techniques for cybersecurity threat detection.
