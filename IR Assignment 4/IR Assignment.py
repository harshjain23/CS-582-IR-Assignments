# Harsh Jain
# 670665164
# hjain20@uic.edu


import re
import math
import os
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import operator
import numpy as np
import nltk
import datetime
import heapq
import sys

ps = PorterStemmer()
stopwords = set(stopwords.words('english'))


def tfidf_calculation(termFrequency, docFrequency):
    return (termFrequency*(math.log2(1330/docFrequency)))


def calculate_weight(key, value, word_graph):
    sum = 0
    numerator = word_graph[value][key]
    for c_node in word_graph[value]:
        sum = sum + word_graph[value][c_node]
    if sum == 0:
        return 0
    else:
        return numerator / sum


def getNGrams(input, n):
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i + n])
    return output


def getlist(file):
    line = []
    for ln in file:
        splitLine = ln.split('_')
        line.append(splitLine[0].lower())
    return line


def tokenize( fileContent ):
    punctuations = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~'
    no_punctContent = ""
    for char in fileContent:
        if char not in punctuations:
            no_punctContent = no_punctContent + (char.lower())
    return re.split("\s+", no_punctContent.strip())


def main():
    arg = sys.argv
    # absPath = input('Provide the path')
    fileNames = {}
    absPath = arg[1]
    nGrams = []
    if os.path.isdir(absPath):
        wordGraphs = []
        vocab = {}
        idfDocs = {}
        tokenList = {}
        index = 0
        for file in sorted(os.listdir(absPath)):
            idfDocs[file] = {}
            wordList = []
            max = 0
            words = {}
            fileNames[index] = file
            with open(absPath + '/' + file, 'r', encoding="cp850") as i:
                fileContents = i.read()
                fileContent = fileContents.split()
                firstIndex = None
                secondIndex = None
                uniGramList = []
                biGramList = []
                triGramList = []
                finalWord = None
                finalIndex = None
                for wordIndex in range(len(fileContent)):
                    tempWord = fileContent[wordIndex].split('_')
                    if tempWord[1] in ['NN', 'NNS', 'NNP', 'NNPS', 'JJ']:
                        word = tempWord[0].lower()
                        if word not in stopwords:
                            word = ps.stem(word)
                            wordList.append(word)

                            if word in idfDocs[file]:
                                idfDocs[file][word] += 1
                            else:
                                idfDocs[file][word] = 1

                            if word in vocab:
                                if file in vocab[word]:
                                    vocab[word][file] = vocab[word][file] + 1
                                else:
                                    vocab[word][file] = 1
                            else:
                                vocab[word] = {}
                                vocab[word][file] = 1
                            if vocab[word][file] > max:
                                max = vocab[word][file]
                            if secondIndex != None:
                                aks = fileContent[wordIndex].split('_')
                                la = biGramList[-1].copy()
                                la.append(aks[0].lower())
                                triGramList.append(la)
                                firstIndex = secondIndex
                                secondIndex = wordIndex
                            if firstIndex != None:
                                secondIndex = wordIndex
                                aks = fileContent[wordIndex].split('_')
                                la = uniGramList[-1].copy()
                                la.append(aks[0].lower())
                                biGramList.append(la)
                            aks = fileContent[wordIndex].split('_')
                            uniGramList.append([aks[0].lower()])
                            firstIndex = wordIndex
                            if len(words):
                                if word in words:
                                    if wordIndex - 1 == finalIndex:
                                        if finalWord in words[word]:
                                            words[word][finalWord] += 1
                                        else:
                                            words[word][finalWord] = 1
                                        if word in words[finalWord]:
                                            words[finalWord][word] += 1
                                        else:
                                            words[finalWord][word] = 1
                                    finalIndex = wordIndex
                                    finalWord = word
                                else:
                                    words[word] = {}
                                    if wordIndex - 1 == finalIndex:
                                        words[word] = {finalWord: 1}
                                        words[finalWord][word] = 1
                                    finalIndex = wordIndex
                                    finalWord = word
                            else:
                                words[word] = {}
                                finalWord = word
                                finalIndex = wordIndex
                        else:
                            firstIndex = None
                            secondIndex = None
                    else:
                        firstIndex = None
                        secondIndex = None
            nGrams.append({1: uniGramList, 2: biGramList, 3: triGramList})
            wordGraphs.append(words)
            index += 1
            tokenList[file] = wordList
    else:
        print("Could Not Find Directory.")


    tfidfScores = {}
    for file in fileNames:
        fileName = fileNames[file]
        tfidfScores[fileName] = {}
        for phrase in idfDocs[fileName]:
            tfidfScores[fileName][phrase] = tfidf_calculation(idfDocs[fileName][phrase],len(vocab[phrase]))

    gramScores = []
    fileInd = 0
    for ng in nGrams:
        grams_scores = {}
        for grams in ng:
            scores = []
            gram = ng[grams]
            for wg in gram:
                score = 0
                for phrase in wg:
                    temp = ps.stem(phrase)
                    fileNa = fileNames[fileInd]
                    if temp in tfidfScores[fileNa]:
                        score = score + tfidfScores[fileNa][temp]
                scores.append(score)
            grams_scores[grams] = scores
        fileInd = fileInd + 1
        gramScores.append(grams_scores)

    topElementsPRank = []
    l = 0
    for ng in gramScores:
        index1 = gramScores[l][1]
        index2 = gramScores[l][2]
        index3 = gramScores[l][3]
        indices = []
        indices.extend(index1)
        indices.extend(index2)
        indices.extend(index3)
        topTen = sorted(range(len(indices)), key=lambda index: indices[index], reverse=True)[:10]
        topTenElements = []
        for elements in topTen:
            ind = int(elements)
            if ind < len(index1):
                topTenElements.append(nGrams[l][1][ind])
            else:
                ind1 = ind - len(index1)
                if ind1 < len(index2):
                    topTenElements.append(nGrams[l][2][ind1])
                else:
                    ind2 = ind1 - len(index2)
                    topTenElements.append(nGrams[l][3][ind2])
        l += 1
        topElementsPRank.append(topTenElements)


    scoring = []
    for wg in wordGraphs:
        weight = {}
        for j in wg:
            weight[j] = 1 / len(wg)
        currScore = {}
        count = 0
        for i in range(10):
            for j in wg:
                currentValue = 0
                nodeCount = len(wg)
                alpha = 0.85
                if len(wg[j]) > 0:
                    for val in wg[j]:
                        currentValue = currentValue + (calculate_weight(j, val, wg) * weight[val])
                        tempScore = alpha * currentValue + ((1 / nodeCount) * (1 - alpha))
                else:
                    tempScore = (1 / nodeCount) * (1 - alpha)
                if j in currScore and currScore[j] == tempScore:
                    count += 1
                currScore[j] = tempScore
            weight.clear()
            weight.update(currScore)
            if count == len(wg):
                break
            else:
                count = 0
        scoring.append(weight)

    gramScores = []
    m = 0
    for ng in nGrams:
        grams_scores = {}
        for grams in ng:
            scores = []
            gram = ng[grams]
            for wg in gram:
                score = 0
                for phrase in wg:
                    temp = ps.stem(phrase)
                    if temp in scoring[m]:
                        score = score + scoring[m][temp]
                scores.append(score)
            grams_scores[grams] = scores
        m = m + 1
        gramScores.append(grams_scores)

    topElements = []
    l = 0
    for ng in gramScores:
        index1 = gramScores[l][1]
        index2 = gramScores[l][2]
        index3 = gramScores[l][3]
        indices = []
        indices.extend(index1)
        indices.extend(index2)
        indices.extend(index3)
        topTen = sorted(range(len(indices)), key=lambda index: indices[index], reverse=True)[:10]
        topTenElements = []
        for elements in topTen:
            ind = int(elements)
            if ind < len(index1):
                topTenElements.append(nGrams[l][1][ind])
            else:
                ind1 = ind - len(index1)
                if ind1 < len(index2):
                    topTenElements.append(nGrams[l][2][ind1])
                else:
                    ind2 = ind1 - len(index2)
                    topTenElements.append(nGrams[l][3][ind2])
        l += 1
        topElements.append(topTenElements)

    goldPath = arg[2]
    goldFiles = {}
    if os.path.isdir(goldPath):
        for file in sorted(os.listdir(goldPath)):
            with open(goldPath + '/' + file, 'r',encoding="cp850") as i:
                fcontents = []
                fileContents = i.readlines()
                for ng in fileContents:
                    a = ng.replace('\n', '')
                    fcontents.append(a)
            goldFiles[file] = fcontents

    print('PAGE RANK Output: ')
    for index in range(1, 11):
        fileNum = 0
        totalScore = 0
        for file in topElements:
            fileScore = 0
            if fileNames[fileNum] in goldFiles:
                goldDict = goldFiles[fileNames[fileNum]]
                stemGoldDict = []
                for phrase in goldDict:
                    words = phrase.split()
                    stemmedPhrase = []
                    for word in words:
                        stemmedPhrase.append(ps.stem(word))
                    newPhrase = ' '.join(stemmedPhrase)
                    stemGoldDict.append(newPhrase)
                count = 0
                for phrase in topElements[fileNum]:
                    stemmedPhrase = []
                    for word in phrase:
                        stemmedPhrase.append(ps.stem(word))
                    finalPhrases = ' '.join(stemmedPhrase)
                    for goldPhrase in stemGoldDict:
                        if finalPhrases == goldPhrase:
                            fileScore = 1 / (count + 1)
                            break
                    else:
                        count += 1
                        if count == index:
                            break
                        continue
                    break
            else:
                fileScore = 0
            totalScore += fileScore
            fileNum += 1
        mrr = totalScore / len(goldFiles)
        print(mrr)
    print('TF-IDF Output: ')
    for index in range(1, 11):
        fileNum = 0
        totalScore = 0
        for file in topElementsPRank:
            fileScore = 0
            if fileNames[fileNum] in goldFiles:
                goldDict = goldFiles[fileNames[fileNum]]
                stemGoldDict = []
                for phrase in goldDict:
                    words = phrase.split()
                    stemmedPhrase = []
                    for word in words:
                        stemmedPhrase.append(ps.stem(word))
                    newPhrase = ' '.join(stemmedPhrase)
                    stemGoldDict.append(newPhrase)
                count = 0
                for phrase in topElementsPRank[fileNum]:
                    stemmedPhrase = []
                    for word in phrase:
                        stemmedPhrase.append(ps.stem(word))
                    finalPhrases = ' '.join(stemmedPhrase)
                    for goldPhrase in stemGoldDict:
                        if finalPhrases == goldPhrase:
                            fileScore = 1 / (count + 1)
                            break
                    else:
                        count += 1
                        if count == index:
                            break
                        continue
                    break
            else:
                fileScore = 0
            totalScore += fileScore
            fileNum += 1
        mrr = totalScore / len(goldFiles)
        print(mrr)

main()
