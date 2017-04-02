import csv
import numpy as np 
import pandas as pd 

df=pd.read_csv('Feature4.csv')
f=open('OutputBenignGraphsFinal.txt','rU')
#cw=csv.writer(open("Feature.csv",'w'))
CsvHeaders= ["add","aget","and","aput","array-length","check-cast","const","div","double-to","fill-array-data-payload","float-to","goto","if","iget","instance-of" ,"int-to","invoke","iput","long-to","monitor","move","mul","neg","new","or","packed","rem","return", "sget","shl","shr","sput","sub","throw","xor"]
LineCount=1
OneAppDictionary={}
for line in f:# For a particular app
	if (LineCount%2!=0): #Graph Number stored on odd lines 
		AppName=line 
	else:
		OneAppDictionary=eval(line) # Storing the entire even line in one dictionary
		for key in OneAppDictionary: # Traversing the dictionary for one app
			print key, 'corresponds to', OneAppDictionary[key]
			df.loc[LineCount/2,key]=OneAppDictionary[key] # [index][key]=Value 
	LineCount=LineCount+1

df.fillna(0, inplace=True)				
	

df.to_csv('out9.csv')
