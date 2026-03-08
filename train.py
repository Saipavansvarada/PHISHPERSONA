import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")

# Keep required columns
df = df[['v1', 'v2']]
df.columns = ['label', 'text']

# Convert labels
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split dataset (STRATIFIED SPLIT ⭐ IMPORTANT)
X_train, X_test, y_train, y_test = train_test_split(
    df['text'],
    df['label'],
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

# Build pipeline (BEST PRACTICE ⭐)
model_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        stop_words='english',
        ngram_range=(1,2),
        max_df=0.9,
        min_df=2
    )),
    ('classifier', LogisticRegression(
        max_iter=2000,
        class_weight='balanced'
    ))
])

# Train model
model_pipeline.fit(X_train, y_train)

# Predict
predictions = model_pipeline.predict(X_test)

# Evaluate
print("Model Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# Save model (single file ⭐ VERY IMPORTANT)
joblib.dump(model_pipeline, "spam_model.pkl")

print("\n✅ Stronger Spam Model Trained and Saved!")