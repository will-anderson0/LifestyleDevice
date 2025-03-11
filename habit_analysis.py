from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

# Analyzes speech to detect user habits and suggest improvements.
def analyze_habits(text):
    words = word_tokenize(text.lower())

    if "coffee" in words:
        return "You mentioned coffee. Consider limiting intake in the evening for better sleep."
    if "exercise" in words:
        return "Great job mentioning exercise! Keep up the habit."

    return "No significant habit detected."
