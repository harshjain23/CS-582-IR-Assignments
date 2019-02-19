#IR Assignment 4

#Name: Harsh Jain
#UIN: 670665164
#ID: hjain20@uic.edu


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


#To run the code: 
- Run the 'IR Assignment.py' script with the arguments: (in the order mentioned 
here):
	Path for abstracts.
	Path for gold standards.
Example:
python "IR Assignment.py" www/abstacts www/gold

#Results:
PAGE RANK Output: 
1- 0.05709992486851991
2- 0.07738542449286251
3- 0.09641873278236905
4- 0.11106937139994985
5- 0.12444277485599782
6- 0.13370899073378384
7- 0.13929018639762406
8- 0.1439859039032589
9- 0.14815987501937886
10- 0.1514656601433457
TF-IDF Output: 
1- 0.0781367392937641
2- 0.10293012772351616
3- 0.12471825694966197
4- 0.13955672426746824
5- 0.15127723516153269
6- 0.16004257450538417
7- 0.16487245536832282
8- 0.16919251547350686
9- 0.17236473352175807
10- 0.1745435464443726

