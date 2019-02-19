import os
import string
import collections
from nltk import PorterStemmer


counts = dict()
total_words = 0
stopwords = set()
most_common = []
stopword_count = 0
terms = int
stem = False
stopword_removal = False


def remove_punctuation(sentence):
    # pre-processes the sentences of the data by removing the punctuations, case sensitivity and digits
    sentence = sentence.lower()
    sentence = sentence.replace("\n","")
    sentence = sentence.replace("\d", "")
    for x in string.punctuation:
        if x in sentence:
            sentence = sentence.replace(x, "")
    return sentence


def word_count(sentence):
    # retrieves the words of a sentence to add to the vocabulary and their count to the total word count
    global counts
    global total_words
    words = sentence.split(" ")
    for word in words:
        if (not stopword_removal) or word not in stopwords:
            if stem:
                word = stem_word(word)
            if word in counts and word != "" and " " not in word :
                counts[word] += 1
                total_words += 1
            elif word != "" and " " not in word:
                counts[word] = 1
                total_words += 1
    return words


def main():
    # reads the input files and sends each line to be processed
    file_path = "C:/Users/harsh/PycharmProjects/IR Assignment 1/citeseer/"
    for file in os.listdir(file_path):
        with open(file_path+file,'r') as x:
            for line in x:
                line = remove_punctuation(line)
                word_count(line.strip())


def get_stopwords():
    # retrieves the stopwords from the file provided
    f = open("stopwords.txt", "r")
    global stopwords
    for line in f:
        stopwords.add(line.replace("\n", ""))


def check_stopwords():
    # get the count of stopwords in the 20 most common words
    global most_common
    global stopword_count
    most_common = collections.Counter(counts).most_common(20)
    stopword_count = 0
    for word, value in most_common:
        if word in stopwords:
            stopword_count += 1


def get_term_count():
    # gets the number of terms required to make up 15% of the total words
    global terms
    terms = 0
    count = 0
    for word, value in collections.Counter(counts).most_common():
        if count < total_words * 0.15:
            count += value
            terms += 1
        else:
            break


print("### Before Porter Stemming and Removal of Stopwords ###")


main()
get_stopwords()
check_stopwords()
get_term_count()
print("Total Word Count: " + total_words.__str__())
print("Vocabulary Word Count: " + counts.__len__().__str__())
print("20 Most common words with their counts: \n" + most_common.__str__())
print("Count of most common words that are stopwords: " + stopword_count.__str__())
print("Terms required to make up 15% of total number of terms: " + terms.__str__())


#def remove_stopwords():
#    global total_words
#    global counts
#    for word in stopwords:
#        if word in counts:
#            total_words -= counts[word]
#            del counts[word]


def stem_word(word):
    # performs stemming on a word using Porter Stemmer
    ps = PorterStemmer()
    word = ps.stem(word)
    return word


stem = True
stopword_removal = True
total_words = 0
counts.clear()
most_common.clear()
stopword_count = 0
terms = 0


main()
# remove_stopwords()
check_stopwords()
get_term_count()
print("\n\n\n### After Porter Stemming and Removal of Stopwords ###")
print("Total Word Count: " + total_words.__str__())
print("Vocabulary Word Count: " + counts.__len__().__str__())
print("20 Most common words with their counts: \n" + most_common.__str__())
print("Count of most common words that are stopwords: " + stopword_count.__str__())
print("Terms required to make up 15% of total number of terms: " + terms.__str__())
