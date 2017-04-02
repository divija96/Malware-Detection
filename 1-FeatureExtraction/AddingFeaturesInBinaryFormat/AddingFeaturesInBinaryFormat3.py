import csv
import numpy as np 
import pandas as pd 
#For Non Standard
df=pd.read_csv('Feature3.csv')
f=open('TemporaryDict','rU')
#cw=csv.writer(open("Feature.csv",'w'))
CsvHeaders= ["ACCESS","ACCESS_PROVIDER","BILLING","BIND","C2D_MESSAGE","INSTALL_SHORTCUT","MAPS_RECEIVE","MIPUSH_RECEIVE","READ_ATTACHMENT","READ","READ_SETTINGS","RECEIVE_ADM_MESSAGE","RECEIVE","SERVICE","UA_DATA","UNINSTALL_SHORTCUT","WRITE_HISTORY_BOOKMARKS","WRITE_PERMISSION","WRITE_SETTINGS"]
#print CsvHeaders
Permissions=set()
DistinctPermissions=set()
AppsDictionary={}
for line in f:
	AppApk,AppPermissions=line.split(":")
	AppsDictionary[AppApk]=AppPermissions
	#print AppsDictionary
	#print

#df.iloc[0]=dict(A='ACCES_MOCK_LOCATION')
#df.loc[1,'ACCES_MOCK_LOCATION']=0
#df.to_csv('out.csv')
#print df
i=-1
for AppApk in AppsDictionary: #For a particular app
	i=i+1
	PermString=AppsDictionary[AppApk]
	PermString=PermString[1:-2]
	PermsList=PermString.split(', ')
	#print PermsList
	for Perm in PermsList:# Permissions of the ith app		
		
		for header in CsvHeaders:
			
			if( not Perm.startswith("\'android.permission.")):
				if(header in Perm[1:-1]):
					print "Yay!!"
					df.loc[i,header]=1
	

df.fillna(0, inplace=True)				
	

df.to_csv('out8.csv')

#for row in cw:
#	App=AppsDictionary[row[0]]
#
#   row[3] = 4
#   writer.writerow(row)

