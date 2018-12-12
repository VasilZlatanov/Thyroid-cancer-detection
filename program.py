import json,os,sys,re
import csv

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier


#Train the program
diseaseTrainer = Trainer(tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

with open("new-thyroid.txt", "r") as file: #OPENS DATASET
   csvReader = csv.reader(file)
   header = csvReader.next()

   #Variables in header, given by the data from the data file
   classID = header.index("classID")
   T3resinUptakeTest = header.index("T3resinUptakeTest")
   totalSerumThyroxin = header.index("totalSerumThyroxin")
   totalSerumTriiodothyroine = header.index("totalSerumTriiodothyroine")
   tsh = header.index("tsh")
   maxAbsDifference = header.index("maxAbsDifference")
   
   for row in file: #FOR EACH LINE
       #lines = file.next().split(",") #PARSE CSV <DISEASE> <SYMPTOM>

      # take the value of the given element from the header and assign it to a variable
       #row = file.next().split(",", ' ')
       
       listedElements = row.split(",", 5)
       #print(listedElements[classID])
       
       firstElement = listedElements[classID]
       secondElement = listedElements[T3resinUptakeTest]
       thirdElement = listedElements[totalSerumThyroxin]
       fourthElement = listedElements[totalSerumTriiodothyroine]
       fifthElement = listedElements[tsh]
       sixthElement = listedElements[maxAbsDifference]
       print(sixthElement)

       
       #diseaseTrainer.train(lines[5], lines[4], lines[3], lines[2], lines[1],  lines[0]) #TRA
       #diseaseTrainer.train(lines[1], lines[0])
       diseaseTrainer.train(sixthElement, firstElement, secondElement, thirdElement, fourthElement, fifthElement)
       

#Classify the data       
diseaseClassifier = Classifier(diseaseTrainer.data, tokenizer.Tokenizer(stop_words = [], signs_to_remove = ["?!#%&"]))

#Ask for the user's input
print("Please insert the values from the test to see to which category it corresponds.")
print("Hint: The values must be separated with commas(,).")
userInput = raw_input()

#Classify the user's input
classification = diseaseClassifier.classify(userInput)

print()
print("The patient's results are from type: ")
print (classification)
print("Reference: 1 = normal, 2 = hypo, 3 = hyper")

#Things to do: change the Trainer class to except more arguments
