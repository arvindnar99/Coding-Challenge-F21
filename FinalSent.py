import os
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import nltk
import random
import pickle

# Open and read Datasets


posData = open('positive.txt', "r").read()
negData = open('negative.txt', "r").read()

# Open input text


with open('input.txt', 'r') as f:
    lines = f.read()

# Clean up and tokenize our input.txt file


lowerCase = lines.lower()
cleanText = lowerCase.translate(str.maketrans('', '', string.punctuation))
ts = sent_tokenize(lines.replace('\n', " "))


documents = []
all_words = []

# Loops to append sentiment values to our datasets and parts of speech tagging
awt = []
for r in posData.split('\n'):
    documents.append((r, "Positive sentiment"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in awt:
            all_words.append(w[0].lower())

for r in negData.split('\n'):
    documents.append((r, "Negative sentiment"))
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in awt:
            all_words.append(w[0].lower())


negWords = word_tokenize(negData)
posWords = word_tokenize(posData)

# loops to append tokenized words to our all words list


for i in posWords:
    all_words.append(i.lower())
for i in negWords:
    all_words.append(i.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:5000]

# function that uses nltk vader analysis to determine sentiment value of the excerpt and each sentence


def sentAnalysis(text):
    negSent, posSent, neuSent = 0, 0, 0

    if os.path.exists("output.txt"):
        os.remove("output.txt")

    fr = open("output.txt", "w")

    score = SentimentIntensityAnalyzer().polarity_scores(cleanText)

    if -.05 < score['compound'] < .05:
        fr.write("The text from the input file has NEGATIVE SENTIMENT\n")
    elif score['compound'] >= .05:
        fr.write("The text from the input file has POSITIVE SENTIMENT\n")
    else:
        fr.write("The text from the input file has NEUTRAL SENTIMENT\n")

    for sentences in text:
        vs = SentimentIntensityAnalyzer().polarity_scores(sentences)
        if -.05 < vs['compound'] < .05:
            test1 = "{:-<65} {}".format(sentences, "Negative Sentiment"), vs['neg']
            fr.write(str(test1))
            fr.write('\n')
            negSent += 1
        elif vs['compound'] >= .05:
            test2 = "{:-<65} {}".format(sentences, "Positive Sentiment"), vs['pos']
            fr.write(str(test2))
            fr.write('\n')
            posSent += 1
        else:
            test3 = "{:-<65} {}".format(sentences, "Neutral Sentiment"), vs['neu']
            fr.write(str(test3))
            fr.write('\n')
            neuSent += 1

    labels = 'Negative Sentiment', 'Positive Sentiment', 'Neutral Sentiment'
    sizes = [negSent, posSent, neuSent]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

# function that finds features of a given text document


def assignFeatures(document):
    wo = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = w in wo
    return features


# loads 5000 featuresets from pickle


setsfeature = open("featureSets.pickle",  "rb")
featuresets = pickle.load(setsfeature)
setsfeature.close()
random.shuffle(featuresets)
train_set = featuresets[:10000]
test_set = featuresets[10000:]

# loads NB classifier from pickle


NBC = open("NaiveBayesClassifer.pickle", "rb")
classifier = pickle.load(NBC)
NBC.close()

# function that uses our model to determine the sentiment of each sentence in the input file


def sentNB(text):
    negVal, posVal = 0, 0
    if os.path.exists("outputNAIVEBAYES.txt"):
        os.remove("outputNAIVEBAYES.txt")
    fr = open("outputNAIVEBATES.txt", "w")
    for sent in text:
        test = classifier.classify(assignFeatures(sent))

        if test == "Negative sentiment":
            negVal += 1
        if test == "Positive sentiment":
            posVal += 1
        out = "{:-<65} {}".format(sent, test)
        fr.write(str(out))
        fr.write('\n')

    labels = 'Negative Sentiment', 'Positive Sentiment'
    sizes = [negVal, posVal]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


sentAnalysis(ts)
sentNB(ts)
