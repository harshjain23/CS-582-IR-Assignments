#IR Assignment 2

#Name: Harsh Jain
#UIN: 670665164
#ID: hjain20@uic.edu


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


#To run the code: 
- Open the 'IR Assignment.py' file.
- Replace the 'file_path' variables at the start of the file with the path of the said files on your local computer
  All the files are as provided by the professor.
	file_path_docs is where the Cranfield Documents are stored
	file_path_queries is where the query file is stored
	file_path_stopwords is where the file containing the stopwords is stored 
	file_path_relevance is where the list of relevant document is stored
- Run the python script.

#Answers to the assignment questions:
Top 10:
Precision: 0.22
Recall: 0.16793893129770993

Top 50:
Precision: 0.1
Recall: 0.3816793893129771

Top 100:
Precision: 0.074
Recall: 0.5648854961832062

Top 500:
Precision: 0.0238
Recall: 0.9083969465648855
