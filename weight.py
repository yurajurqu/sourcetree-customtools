import sys
import os

base = ""
files=[]
weight=0
for i in range(0, len(sys.argv)):
    if i == 1:
        base = sys.argv[i] + "\\"
    if i > 1:
		fileName= base +sys.argv[i].replace('/','\\')
		#print(fileName)
		files.append(fileName)

for file in files:
    if file != "":
		weight+=os.path.getsize(file)
#print(weight)
print("Selected files weight: " + str(weight) +"Bytes")
weight=(weight*1.0)/1000000        
print("Selected files weight: " + str(weight) +"MB")