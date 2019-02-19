#IR Assignment 4

#Approach used:
- Read the input files: documents and gold standard files
- Pre-processing:
  remove tags.
  remove stopwords(used stopwords from nltk).
  stemming.
  convert to lower case.
  
- build the inverted index for the documents.
- calculate the weight of the document from the indexes built in previous step.
- calculate TF-IDF for each token and sum them for TF-IDF of n-grams in documents. TF is unnormalized.
- page rank implemented for all n-grams of each document using undirected word graph.
- evaluate the results as per MRR for both TF-IDF and Page Rank using top 10 n-grams.
