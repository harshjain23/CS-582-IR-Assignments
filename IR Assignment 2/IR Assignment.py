import os
import string
import re
import math
import collections
from nltk import PorterStemmer

### File Paths
file_path_docs = "C:/Users/harsh/PycharmProjects/IR Assignment 1/cranfieldDocs/"
file_path_queries = "C:/Users/harsh/PycharmProjects/IR Assignment 1/"
file_path_stopwords = "C:/Users/harsh/PycharmProjects/IR Assignment 1/"
file_path_relevance = "C:/Users/harsh/PycharmProjects/IR Assignment 1/"

stopwords = set()
index = dict()
q_index = dict()
weight = dict()
q_weight = dict()
document_text = dict()
doc_len = dict()
q_len = dict()
queries = dict()
cos_sim = dict()
relevance = dict()


def remove_punctuation(content):
    # pre-processes the sentences of the data by removing the punctuations, case sensitivity and digits
    content = content.strip()
    content = content.lower()
    content = re.sub('\d', '%d', content)
    for x in string.punctuation:
        if x in content:
            content = content.replace(x, " ")
    return content


def main():
    # opens the input data files and calls relevant methods
    get_stopwords()
    for file in os.listdir(file_path_docs):
        f = open(file_path_docs+file, 'r')
        content = f.read()
        content = content.replace("\n", " ")
        get_tag_values(content)
    get_queries()
    build_index()
    calculate_weight()
    cosine_sim()
    get_relevance()
    eval_metrics()


def get_queries():
    # retrieves the input queries
    global queries
    q_count = 0
    with open(file_path_queries + 'queries.txt', 'r') as x:
        for line in x:
            q_count += 1
            line = line.replace("\n", "")
            line = remove_punctuation(line)
            line = remove_stopwords(line)
            line = stemming(line)
            line = remove_stopwords(line)
            queries[q_count.__str__()] = line


def get_tag_values(content):
    # retrieves the values of the required tags from the document
    global document_text
    for item in content.split("</DOCNO>"):
        if "<DOCNO>" in item:
            doc_no = (item[item.find("<DOCNO>") + len("<DOCNO>"):]).strip()
    for item in content.split("</TITLE>"):
        if "<TITLE>" in item:
            title = item[item.find("<TITLE>") + len("<TITLE>"):]
    for item in content.split("</TEXT>"):
        if "<TEXT>" in item:
            text = item[item.find("<TEXT>") + len("<TEXT>"):]
    doc_text = title + " " + text
    doc_text = remove_punctuation(doc_text)
    doc_text = remove_stopwords(doc_text)
    doc_text = stemming(doc_text)
    doc_text = remove_stopwords(doc_text)
    document_text[doc_no] = doc_text


def get_stopwords():
    # retrieves the stopwords from the file provided
    f = open(file_path_stopwords + "stopwords.txt", "r")
    global stopwords
    for line in f:
        stopwords.add(line.replace("\n", ""))


def stemming(content):
    # performs stemming on a word using Porter Stemmer
    if stem:
        ps = PorterStemmer()
        words = content.split(" ")
        for word in words:
            content = content.replace(word, ps.stem(word))
    return content


def remove_stopwords(content):
    # removes the stopwords in a given string
    if stopword_removal:
        words = content.split(" ")
        for word in list(words):
            if word in stopwords or len(word) <= 2:
                words.remove(word)
        content = " ".join(words)
    return content


def build_index():
    # builds the inverted index for all the words of the input documents and queries
    global index
    global document_text
    for doc_id, text in document_text.items():
        words = text.split(" ")
        for word in words:
            if word not in index.keys():
                index[word] = {}
                index[word][doc_id] = 1
            elif word in index and doc_id not in index[word].keys():
                index[word][doc_id] = 1
            else:
                index[word][doc_id] += 1
    global q_index
    global queries
    for doc_id, text in queries.items():
        words = text.split(" ")
        for word in words:
            if word not in q_index.keys():
                q_index[word] = {}
                q_index[word][doc_id] = 1
            elif word in q_index and doc_id not in q_index[word].keys():
                q_index[word][doc_id] = 1
            else:
                q_index[word][doc_id] += 1


def calculate_weight():
    # calculates the weight of the words in the vocab for each document and query using TF-IDF
    global document_text
    global index
    global weight
    global doc_len
    global q_len
    for word in index.keys():
        for doc_id in index[word].keys():
            if word not in weight.keys():
                weight[word] = {}
            tf = (index[word][doc_id])
            idf = math.log((len(document_text) / len(index[word])), 2)
            weight[word][doc_id] = tf * idf
            if doc_id not in doc_len.keys():
                doc_len[doc_id] = (tf**2) * (idf**2)
            else:
                doc_len[doc_id] += (tf**2) * (idf**2)
    global queries
    global q_index
    global q_weight
    for word in q_index.keys():
        for doc_id in q_index[word].keys():
            if word not in q_weight.keys():
                q_weight[word] = {}
            tf = (q_index[word][doc_id])
            if word in index.keys():
                idf = math.log((len(document_text) / len(index[word])), 2)
            else:
                idf = 0
            q_weight[word][doc_id] = tf * idf
            if doc_id not in q_len.keys():
                q_len[doc_id] = (tf**2) * (idf**2)
            else:
                q_len[doc_id] += (tf**2) * (idf**2)


def cosine_sim():
    # calculates the cosine similarities of the queries against the relevant documents
    global weight
    global q_weight
    global index
    global q_index
    global cos_sim
    global q_len
    global doc_len
    for word in q_index.keys():
        for q_id in q_index[word].keys():
            if word in index.keys():
                for doc_id in index[word].keys():
                    if q_id not in cos_sim.keys():
                        cos_sim[q_id] = {}
                    if doc_id not in cos_sim[q_id].keys():
                        cos_sim[q_id][doc_id] = weight[word][doc_id] * q_weight[word][q_id] / \
                                                (math.sqrt(doc_len[doc_id]) * math.sqrt(q_len[q_id]))
                    else:
                        cos_sim[q_id][doc_id] += weight[word][doc_id] * q_weight[word][q_id] / \
                                                 (math.sqrt(doc_len[doc_id]) * math.sqrt(q_len[q_id]))


def get_relevance():
    # retrieves the relevance expected output
    global relevance
    with open(file_path_relevance + 'relevance.txt', 'r') as x:
        for line in x:
            words = line.split()
            if words[0] not in relevance:
                relevance[words[0]] = [words[1]]
            else:
                relevance[words[0]].append(words[1])


def eval_metrics():
    # evaluates the performance of this program's result
    global queries
    global cos_sim
    global relevance
    relevant_given = 0
    query_counter = 0
    relevant_found_t10 = 0
    relevant_found_t50 = 0
    relevant_found_t100 = 0
    relevant_found_t500 = 0
    for q_id in queries.keys():
        query_counter += 1
        relevant_given += len(relevance[q_id])
        doc_counter = 0
        for doc_id, sim_val in collections.Counter(cos_sim[q_id]).most_common(500):
            doc_counter += 1
            if doc_id in relevance[q_id]:
                if doc_counter in range(1, 11):
                    relevant_found_t10 += 1
                    relevant_found_t50 += 1
                    relevant_found_t100 += 1
                    relevant_found_t500 += 1
                elif doc_counter in range(11, 51):
                    relevant_found_t50 += 1
                    relevant_found_t100 += 1
                    relevant_found_t500 += 1
                elif doc_counter in range(51, 101):
                    relevant_found_t100 += 1
                    relevant_found_t500 += 1
                else:
                    relevant_found_t500 += 1
    print("Top 10:")
    print("Precision: " + (relevant_found_t10/100).__str__())
    print("Recall: " + (relevant_found_t10 / relevant_given).__str__())
    print("\nTop 50:")
    print("Precision: " + (relevant_found_t50 / 500).__str__())
    print("Recall: " + (relevant_found_t50 / relevant_given).__str__())
    print("\nTop 100:")
    print("Precision: " + (relevant_found_t100 / 1000).__str__())
    print("Recall: " + (relevant_found_t100 / relevant_given).__str__())
    print("\nTop 500:")
    print("Precision: " + (relevant_found_t500 / 5000).__str__())
    print("Recall: " + (relevant_found_t500 / relevant_given).__str__())


stem = True
stopword_removal = True
main()
