#IR Assignment 1

#Name: Harsh Jain
#UIN: 670665164
#ID: hjain20@uic.edu


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


#To run the code: 
- Open the 'IR Assignment.py' file.
- Download and extract the 'citeseer' zip (provided by Prof.) on your local machine. 
- Replace the 'file_path' variable in the main function with the path of the extracted 'citeseer' folder 
  containing the document files.
- Download the document of 'stopwords' (given by the Prof.) on your local machine.
- Replace the path in the 'open' statement of the 'get_stopwords' function with the path of the 'stopwords' 
  file downloaded in the previous step.
- Run the python script.

#Answers to the assignment questions:
1. Pre-processing performed:
	> Convert the whole sentence to lower case.
	> Removal of newline(\n) character.
	> Removal of digits.
	> Removal of all punctuations.
	
2. The 'stem' and the 'stopword_removal' flags are set to false.
	a. 476173
	b. 19894
	c. [('the', 25662), ('of', 18638), ('and', 14131), ('a', 13345), ('to', 11536), ('in', 10067), ('for', 7379), 
		('is', 6577), ('we', 5138), ('that', 4820), ('this', 4446), ('are', 3737), ('on', 3656), ('an', 3281), 
		('with', 3200), ('as', 3057), ('by', 2765), ('data', 2691), ('be', 2500), ('information', 2322)]
	d. 18
	e. 4
	
3. The 'stem' and the 'stopword_removal' flags are set to true.
	a. 265756
	b. 13564
	c. [('system', 3741), ('data', 2691), ('agent', 2688), ('inform', 2398), ('model', 2315), ('paper', 2246), 
		('queri', 1905), ('user', 1756), ('learn', 1740), ('algorithm', 1584), ('1', 1551), ('approach', 1544), 
		('problem', 1543), ('applic', 1522), ('present', 1507), ('base', 1486), ('web', 1439), ('databas', 1424), 
		('comput', 1411), ('method', 1223)]
	d. 0
	e. 22
	