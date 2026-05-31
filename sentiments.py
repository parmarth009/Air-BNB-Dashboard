import pandas as pd

# Load your listings file (with encoding fix)
df = pd.read_csv('listings.csv', encoding='latin1')

# Function to classify sentiment based on review score
def get_sentiment(score):
    if score >= 90:
        return 'Positive'
    elif score >= 70:
        return 'Neutral'
    else:
        return 'Negative'

# Apply sentiment to review scores rating column
df['sentiment'] = df['review_scores_rating'].apply(get_sentiment)

# Save the result as a new CSV file
df.to_csv('listings_with_sentiment.csv', index=False)

print("Done! File saved as listings_with_sentiment.csv")