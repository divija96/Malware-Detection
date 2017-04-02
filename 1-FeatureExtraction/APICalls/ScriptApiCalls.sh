myarray=(`cat /home/mukta/AllAppsForAPICalls.txt`)
noofelements=${#myarray[*]}
#now traverse the array
counter=584
while [ $counter -lt 778 ]
do
    cd "$(echo "${myarray[$counter]}")"  
    
    cd smali
    echo  "{\"android.provider\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt	; 	grep -roh android.provider . | wc -w>> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt	 ;	    echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"Http\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	grep -roh Http  . | wc -w>> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				; 	    echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"create\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh create . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;	
    echo  "\"intent\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			 	;	grep -roh intent . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getSim\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh getSim . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getDevice\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh getDevice . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getCall\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh getCall . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getClass\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh getClass . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getLine\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh getLine . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getSubscriber\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt		;	grep -roh getSubscriber . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt		;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getPackage\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh getPackage . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"getMethod\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh getMethod . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"java\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh java . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"SMS\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	grep -roh SMS . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"Key\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	grep -roh Key . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"Secret\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh Secret . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"FindClass\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh FindClass . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"crypto\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh crypto . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"DexClass\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh DexClass . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"native\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	grep -roh native . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt				;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"System.load\":" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	grep -roh System.load . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt			;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"BOOT_COMPLETED\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt		;	grep -roh BOOT_COMPLETED. | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt		;	echo "," >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    echo  "\"RUN\":">> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt					;	grep -roh RUN . | wc -w >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt  				 ;   echo "}" >> /media/mukta/myE/BenignSmalis/Dicts/$counter.txt;
    counter=$(( $counter + 1 ))
	 cd ..
	 cd ..
done
