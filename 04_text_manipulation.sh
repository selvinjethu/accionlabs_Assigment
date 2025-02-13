AWK - Extract only ERROR logs  
awk '$3 == "ERROR" {print}' logs.txt  

SED - Replace `ERROR` with `CRITICAL`  
sed 's/ERROR/CRITICAL/g' logs.txt  

TR - Convert all lowercase to uppercase  
cat logs.txt | tr 'a-z' 'A-Z'  

GREP - Find all logs with "CPU"  
grep "CPU" logs.txt  
