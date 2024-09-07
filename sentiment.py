from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())

analyzer = SentimentIntensityAnalyzer()

negative = []
neutral = []
positive = []

for n in range(df.shape[0]):
    title = df.iloc[n,0]
    title_analyzer = analyzer.polarity_scores(title)
    print(title_analyzer)

    negative.append(title_analyzer['neg'])
    neutral.append(title_analyzer['neu'])
    positive.append(title_analyzer['pos'])
    
df["Negative"] = negative
df["Neutral"] = neutral
df["Positive"] = positive
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


document = open("results.csv", "a")
negative_mean = df["Negative"].mean()
neutral_mean = df["Neutral"].mean()
positive_mean = df["Positive"].mean()
document.write(f"The mean of negative article scores is {negative_mean}")
document.write(f"\nThe mean of neutral article scores is {neutral_mean}")
document.write(f"\nThe mean of positive article scores is {positive_mean}")

#being sorted in positive and negative
largest_pos = df.nlargest(5, ["Positive"])
largest_neg = df.nlargest(5, ["Negative"])
document.write(f"\nThe 5 most positive articles are: {largest_pos}")
document.write(f"\nThe 5 most negative articles are: {largest_neg}")
document.close()
