# Deep Neural Network Example using custom data to for sentiment analysis 

To do this, we will use two files: pos and neg. The pos file has ~5,000 positive sentiment statements, and the neg file has ~5,000 negative sentiment statements.
we open the files, read the lines, tokenize the words, and add them to the lexicon. 
we  lemmatize and remove duplicates. We also don't really need super common words, nor very uncommon words. For example, words like "a", "and", or "or" aren't going to give us much value in this simple "bag of words" model, so we don't want them. Uncommon words aren't going to be very useful either, since they'd likely be so rare that their very presence would skew the results. 

This gives us about 62% accuracy. Feel free to test with many more layers, more nodes...etc. We will likely find that the impact is minimal. I said it was mostly dataset sizes that were important. In the next example, we're going to use a much larger dataset to see if that makes any significant difference.

