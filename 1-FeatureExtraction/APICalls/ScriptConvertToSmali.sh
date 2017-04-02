myarray=(`cat /home/mukta/AllAppsForAPICalls.txt`)
noofelements=${#myarray[*]}
#now traverse the array
counter=253
while [ $counter -lt 778 ]
do
    apktool d "$(echo /media/mukta/myD/AndroidDataset/benign/"${myarray[$counter]}".apk)"  -o "$(echo /media/mukta/myE/BenignSmalis/"${myarray[$counter]}")"   
    counter=$(( $counter + 1 ))

done
