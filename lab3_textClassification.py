# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:40:16 2018

@author: Sen
"""
import re, string
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

#Read the datasets
path = 'C:/Users/Sen/Downloads/CUS 635 (Web data mining)/Labs/Lab3/'
filePrefix = 'training_'
categories=['ARTS','SPORTS']
minWordLength = 3
maxWordLength = 20
totArticles = 0

dataset={}
allFeatures=set()
for category in categories:
    fileName=path+filePrefix+category.lower()
    f= open(fileName,'r')
    dataset[category]=f.readlines()
    f.close
    totArticles+=len(dataset[category])
    
'''
print (dataset['ARTS'])
print ('===========================')
print (dataset['SPORTS'])
'''

feature_count = {}
category_count = {}
probCat = {}

# Calculate the probabilities for each category
for category in categories:
    probCat[category]=len(dataset[category])*1.0/totArticles
    print ("%s - p(%s)=%s" % (category,category,probCat[category]))
    
freqWord = {}
wordCounts = {}

def buildFrequencies(dataset):
    for category in categories:
        freqWordCat = {}
        count = 0
        for article in dataset[category]:
            #You can do a lot of optimization here
            words = [w for w in word_tokenize(article)]
            count+=len(words)
            for word in words:
                allFeatures.add(word)
                if word in freqWordCat:
                    freqWordCat[word] = freqWordCat[word]+1
                else:
                    freqWordCat[word] = 1
        freqWord[category] = freqWordCat
        wordCounts[category] = count


#Generate frequencies
buildFrequencies(dataset)

x = 'the'
print ("Checking Frequencies for word 'play':")
print ("F('%s'|'ARTS')=%s" % (x, freqWord['ARTS'][x]))
print ("F('%s'|'SPORTS')=%s" % (x,freqWord['SPORTS'][x]))


def getTermProbability(word):
    count = 0
    total = 0
    for category in categories:
        total += wordCounts[category]
        if word in freqWord[category]:
            count+=freqWord[category][word]
    return count*1.0/total

def getTermCondProbability(word,category):
    count = 0
    total = wordCounts[category]

    if word in freqWord[category]:
        count=freqWord[category][word]
    else:
        #Apply Laplace Smoothing
        count=1.0/(len(freqWord[category])+len(allFeatures))
    
    return count*1.0/total

term = 'the'
  
print ("probability for word %s - p('%s')= %s" % (term, term, getTermProbability('team')))
print ("probability for word %s in ARTS - p('%s'|'ARTS')=%s" % (term, term, getTermCondProbability('team','ARTS')))
print ("probability for word %s in SPORTS - p('%s'|'SPORTS')=%s" % (term, term, getTermCondProbability('team','SPORTS')))

def NaiveBayesClassifier(article):
    words = [w for w in word_tokenize(article)]
    results={}
    for category in categories:
        pCat = probCat[category]
        pNumerator = 1.0
        for word in words:
            pN = getTermCondProbability(word,category)
            pNumerator*= pN
        pClassification = pNumerator*pCat
        results[category] = pClassification
    
    pMax = 0.0
    predictedClass = ''
    for category in categories:
        if results[category]>pMax:
            pMax = results[category]
            predictedClass = category

    #print ('The article has been assigned to class "%s" with a probability of %s' % (predictedClass,pMax))
    return predictedClass

article = "Without Any Title at Stake, Cavaliers Relive Rally Past Warriors"
NaiveBayesClassifier(article)

f=open('C:\\tmp\\testing.txt','r')
lines=f.readlines()
f.close

correct = 0
total = len(lines)
index = 1

TP=0.0
TN=0.0
FP=0.0
FN=0.0

F=0.0
precision = 0.0
recall = 0.0

for line in lines:
    elems = line.split('\t')
    article=elems[0]
    category=elems[1][:-1]
    predictedCategory = NaiveBayesClassifier(article)
    
    print '%s. Prediction[%s] Class[%s]' % (index,predictedCategory,category)
    index+=1
    
    #Calculating quality measures
    if (predictedCategory == category):
        correct+=1
        if (category == categories[1]):
            TP+=1
        else:
            TN+=1
    else:
        if (predictedCategory == categories[1]):
            FN+=1
        else:
            FP+=1

precision = TP/(TP+FP)
recall = TP/(TP+FN)
F=2*(precision*recall)/(precision+recall)

print ('\nThe classifer was correct %s out of %s or %s' % (correct,total,correct*1.0/total))
print 'precision=%s' % precision
print 'recall=%s' % recall
print 'F=%s' % F