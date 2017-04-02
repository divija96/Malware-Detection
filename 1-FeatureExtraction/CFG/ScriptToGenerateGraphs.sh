Apps_List=(`cat AllApps.csv`)
NoOfApps=${#Apps_List[*]}
counter=1
while [ $counter -lt 800 ];
 do  
	python androxgmml.py -i /media/mukta/myD/AndroidDataset/benign/${Apps_List[$counter]} -o /media/mukta/myE/BenignGraphs1/"Ben"$counter.xgmml;
	 counter=$(($counter+1)); 
	
	echo "$counter"; 
done

MalApps_List=(`cat MaliciousApps.csv`)
NoOfApps=${#MalApps_List[*]}
counter=1
while [ $counter -lt 610 ];
 do  
 echo "${MalApps_List[$counter]}";
	python androxgmml.py -i /media/mukta/myD/AndroidDataset/Drebin/drebin-0/${MalApps_List[$counter]} -o /media/mukta/myE/MaliciousGraphs/"Mal"$counter.xgmml;
	 counter=$(($counter+1)); 
	 
	echo "$counter"; 
done

