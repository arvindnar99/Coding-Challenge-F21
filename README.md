# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Solution Explanation

These are the following sources used:

[VaderSentiment](https://github.com/cjhutto/vaderSentiment#introduction)
[Positive and Negative movie review datasets](https://pythonprogramming.net/static/downloads/short_reviews/)
[Learning to classify text](https://www.nltk.org/book/ch06.html)
[Sentence and word Tokenization](https://stackoverflow.com/questions/37605710/tokenize-a-paragraph-into-sentence-and-then-into-words-in-nltk)
[Sentiment Analysis Playlist](https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&t=0s)

With these resources, I was able to implement two different types of sentiment analysis.

## Vader Sentiment Analysis

Vader Sentiment analysis relies on sentiment lexions which are a list of lexical features or words. These words are labeled based off their semantic orientation. In this case the orientations are either positive, negative, and neutral. Vader analysis not only tells use which orientation it thinks the text is but also gives us a compound ratio that tells us how positive, negative, or neutral a piece of text is. In my implementation, I was able to pass on our input file and tokenize it's contents into seperate sentences. After that was done, I called the SentimentIntensityAnalyzer() built in function provided by the NLTK library and took the sentiment score of each sentence of the input file. I also did sentiment analysis on the whole text to compare the results I got from the analysis of individual sentences. The outputs were then written to the "output.txt" file

The score was then processed and we are given a compound ratio. 
  - A positive sentiment means that the compound score is >= .05. 
  - A neutral sentiment means that the compound score is > -.05 and the score < .05
  - A negative sentiment means that the compound score is <= -.05

## Naive Bayes Classifier

 For the next implementation, I used the Naive Bayes Classififier. Using a dataset found online, I am able to train the classifier in order to estimate wheter a given text is positive or negative. I used parts of speech tagging and word tokenization on the datasets which is and appended the proper label to each review in the specified files. Once that has been done, the data is then appended to the all_words[] list and is now able to decide the features that are relevant in our input. The featuresets variable is used to extract and process the data in our dataset and put them inot a training set and testing set which will be used to train the classifier. I was able to use the input file in the feature extractor function and get a estimation of each sentence in our input on whether it is positive or negative sentiment. The outputs were then written to the "outputNAIVEBATES.txt" file
 
 ## Output
 

   - The Vader Sentiment Analyzer showed that the input file has a majority positive sentiment. Below is a pie chart showing the percentage of each sentiment:
     
      ![nb](https://user-images.githubusercontent.com/62112884/132259296-0de1bfbb-ea85-479e-8d91-64a0283a4d7a.PNG)
      
   - The Naive Bayes Classifier showed that the input file has a majority negative sentiment. Below is a pie chart showing the percentage of each sentiment:
      
      ![nbs](https://user-images.githubusercontent.com/62112884/132259956-5e2131fb-1e16-4d88-9698-141753d9f0a5.PNG)



     
## Analysis and Conclusion

After reading the given input file, my observation was that it had mostly positive sentiment. According to the vader sentiment on the full excerpt and the individual sentences, we can see that it shows mostly positive sentiment. The same cannot be said with our Naive Bayes classifer as it marked almost most of the sentences as negative. This could be because there was not an easily accesible neutral dataset with netural lexicons. Neutral words would be labeled as negative and if it was netural there is a low chance that the classifier would define it as a positive sentiment. Another reason why is that our dataset is very limited even though each of them has about 1000 different movie reviews. Training the classifier with a larger dataset may solve the problems we got with the ouputs.

