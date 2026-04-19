# ============================================================
# EXPERIMENT 7: Spam Filter & Sentiment Analysis in Python
# ============================================================
# Install if needed: pip install scikit-learn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, classification_report,
                              confusion_matrix, ConfusionMatrixDisplay)

print("=" * 50)
print("EXPERIMENT 7: Spam Filter & Sentiment Analysis")
print("=" * 50)

# ===========================================================
# PART A — SPAM FILTER
# ===========================================================
print("\n" + "=" * 30)
print("PART A: SPAM FILTER")
print("=" * 30)

emails = [
    "Win free money now click here",
    "Congratulations you won a lottery",
    "Buy cheap pills online now",
    "Free offer claim your prize",
    "Click here to get rich fast",
    "Hello can we schedule a meeting",
    "Please find the attached report",
    "Meeting agenda for tomorrow",
    "Project update from the team",
    "Happy birthday see you soon",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1=Spam, 0=Ham

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=42
)

clf = MultinomialNB()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("\nSpam Filter Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred,
      target_names=["Ham", "Spam"]))

# Test on new email
new_emails = ["Win big money now!", "Can you join the call at 3pm?"]
new_X = vectorizer.transform(new_emails)
preds = clf.predict(new_X)
for email, label in zip(new_emails, preds):
    print(f"  '{email}' → {'SPAM' if label == 1 else 'HAM'}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Ham", "Spam"])
disp.plot(cmap='Blues')
plt.title("Spam Filter - Confusion Matrix")
plt.tight_layout()
plt.savefig('exp7_spam_cm.png')
plt.show()

# ===========================================================
# PART B — SENTIMENT ANALYSIS
# ===========================================================
print("\n" + "=" * 30)
print("PART B: SENTIMENT ANALYSIS")
print("=" * 30)

reviews = [
    "This product is amazing I love it",
    "Absolutely fantastic quality highly recommend",
    "Great value for money very happy",
    "Wonderful experience will buy again",
    "Best purchase I have ever made",
    "Terrible product do not buy",
    "Very disappointed with the quality",
    "Waste of money horrible experience",
    "Awful service never ordering again",
    "Bad product stopped working quickly",
]
sentiments = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 1=Positive, 0=Negative

tfidf = TfidfVectorizer()
X2 = tfidf.fit_transform(reviews)

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, sentiments, test_size=0.3, random_state=42
)

clf2 = MultinomialNB()
clf2.fit(X2_train, y2_train)
y2_pred = clf2.predict(X2_test)

print("\nSentiment Analysis Accuracy:", accuracy_score(y2_test, y2_pred))
print("\nClassification Report:\n", classification_report(y2_test, y2_pred,
      target_names=["Negative", "Positive"]))

new_reviews = ["I love this!", "This is the worst thing ever."]
new_X2 = tfidf.transform(new_reviews)
preds2 = clf2.predict(new_X2)
for review, label in zip(new_reviews, preds2):
    print(f"  '{review}' → {'POSITIVE' if label == 1 else 'NEGATIVE'}")

# Confusion Matrix
cm2 = confusion_matrix(y2_test, y2_pred)
disp2 = ConfusionMatrixDisplay(confusion_matrix=cm2, display_labels=["Negative", "Positive"])
disp2.plot(cmap='Greens')
plt.title("Sentiment Analysis - Confusion Matrix")
plt.tight_layout()
plt.savefig('exp7_sentiment_cm.png')
plt.show()
print("\nExperiment 7 Complete!")
