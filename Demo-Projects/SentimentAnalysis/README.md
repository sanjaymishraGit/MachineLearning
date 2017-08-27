# sentiment-analyzer
Analyses the twitter sentiment on given topic and stores the result in csv file.
It uses Python 'TextBlob' library for processing natural language. It uses PatternAnalyzer and NaiveBayesAnalyzer for decting 
Polarity,Subjectivity,Classification,P_Pos and P_Neg in a topic

##Requirements

* Python 3

##Usage 

1. Fetch the twitter API keys and fill the information in `credentials.yml`

2. `virtualenv -p python3 twitter`
3. `source twitter/bin/activate`
3. `pip3 install tweepy yaml textblob`
4. `python sentiment.py`

##Results
Check baba_ram_sentiment_dataset.csv for the actual csv output
