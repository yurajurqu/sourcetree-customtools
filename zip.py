import sys
from zipfile import ZipFile
import os
from os.path import basename
import uuid
import datetime
sessionId = str(uuid.uuid1())
sessionTimestampId = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S%f")[:-3]

outputDir ="C:\\yuraq\\output\\"

base = ""
files=[]
for i in range(0, len(sys.argv)):
    if i == 1:
        #este campo es $REPO del custom action de sourcetree
        base = sys.argv[i] + "\\"
        name = base.split('\\')[-2]
        print(name)
        outputfileName=name + ("%s_%s" % (sessionTimestampId,sessionId))+".zip"
    if i > 1:
        #este campo es "n" $FILE del custom action de sourcetree (eg file1 file2 file3)
        files.append(sys.argv[i])
        
zipObj = ZipFile(outputDir+outputfileName, 'w')

for file in files:
    if file != "":
        zipObj.write(base+file,file)
        
zipObj.close()