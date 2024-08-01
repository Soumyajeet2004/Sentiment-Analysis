from textblob import TextBlob

with open('data.txt','r') as dt:
    document = dt.read()
blob = TextBlob(document)
sentiment = blob.sentiment
polarity= sentiment.polarity
print("The Sentimental Polarity Is : ",polarity)

if polarity>0 :
    print("It is a Positive Feedback...")
elif polarity<0 :
    print("It is a Negative Feedback...")
else:
    print("It is a Neutral Feedback...")