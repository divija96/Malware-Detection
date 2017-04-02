import csv
f=open('TemporaryDict','rU')
cw=csv.writer(open("AllPermissions.csv",'w'))
Permissions=set()
DistinctPermissions=set()
AppsDictionary={}
for line in f:
	AppApk,AppPermissions=line.split(":")
	AppsDictionary[AppApk]=AppPermissions
	print AppsDictionary
	print
	
	
for AppApk in AppsDictionary: 
	PermString=AppsDictionary[AppApk]
	PermString=PermString[1:-2]
	PermsList=PermString.split(', ')
	for Perm in PermsList:
		#print "Perm"+Perm
		if(Perm.startswith("\'android.permission.")):
			if(Perm[20:-1] not in Permissions):
				Permissions.add(Perm[20:-1])
	DistinctPermissions=set(Permissions)
	cw.writerow(list(DistinctPermissions))
	print DistinctPermissions

	

f.close()