#IR Assignment 2

#Approach used:
- Read the input files: Cranfeild documents, Stopwords file, Queries file, Relevance file.
- Pre-processing:
  remove tags.
  remove punctuations.
  remove stopwords (performed once again after stemming).
  stemming.
  convert to lower case.
  remove digits.
  remove newline characters and unwanted space characters.
  
- build the inverted index for the documents and queries.
- calculate the weight of the document and query words from the indexes built in previous step.
  ### TF is unnormalized.
  ### IDF for the query words was calculated using frequencies of the document inverted index
		(N= 1400 and number of documents the word appears in those 1400 documents).
- calculate the cosine similarity based on the weights calculated in the previous step.
- evaluate the results as required.
