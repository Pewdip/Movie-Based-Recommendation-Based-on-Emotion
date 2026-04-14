import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')   # Ensure charts open in VS Code
import matplotlib.pyplot as plt

# === LOAD DATA ===
try:
    df = pd.read_excel("movies_with_emotions_year.xlsx")
except FileNotFoundError:
    print("❌ File not found. Please ensure 'movies_with_emotions_year.xlsx' is in the same folder.")
    exit()

# === EMOTION-BASED RECOMMENDER FUNCTION ===
def recommend_movies(emotion):
    """Return top 5 movies based on the given emotion."""
    emotion = emotion.capitalize()
    if emotion not in df['Emotion'].unique():
        print(f"⚠️ Emotion '{emotion}' not found! Available emotions are:")
        print(", ".join(df['Emotion'].unique()))
        return []

    filtered = df[df['Emotion'] == emotion].sort_values(by="Rating", ascending=False).head(5)
    return filtered

# === SHOW PIE CHART ===
def show_pie_chart(filtered_df):
    """Display a pie chart of ratings for the top 5 movies."""
    plt.figure(figsize=(7, 7))
    plt.pie(
        filtered_df['Rating'],
        labels=filtered_df['Title'],
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title("Top 5 Recommended Movies (by Rating)")
    plt.tight_layout()
    plt.show(block=True)

# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("🎬 Emotion-Based Movie Recommender 🎭")
    print("Available emotions:", ", ".join(df['Emotion'].unique()))
    print("----------------------------------------------------------")

    user_emotion = input("Enter your current emotion: ").strip()
    recommendations = recommend_movies(user_emotion)

    if len(recommendations) > 0:
        print(f"\n🎥 Top 5 Movie Recommendations for '{user_emotion.capitalize()}':\n")
        for i, row in enumerate(recommendations.itertuples(), 1):
            print(f"{i}. {row.Title} ({row.Year}) - ⭐ {row.Rating} ({row.Votes} votes) [{row.Genre}]")

        # Show chart
        show_pie_chart(recommendations)
    else:
        print("No recommendations found.")

print("Program finished.")
