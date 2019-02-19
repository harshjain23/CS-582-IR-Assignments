#IR Assignment 1

#Approach used:
- Read the input files line by line.
- Pre-processing each line by removing punctuations, digits and case sensitivity
  (all sentences are converted to lower case).
- Split the sentence by blanks/whitespaces to get words and perform stopwords removal 
  and stemming on the words if needed.
- Tokenize the words whilst maintaining the total word count and the frequency for each word.
- Read the list of stopwords provided in the file given by Prof.
- Check the top 20 most common words for stopwords and get the count.
- Parse the words in the descending order of their frequency in the documents (most common words first) 
  to calculate the number of terms required to make up 15% of the total word count.
- Print the outputs as required.
