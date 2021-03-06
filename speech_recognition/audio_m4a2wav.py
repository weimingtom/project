import os
import sys
sys.path.insert(0, "/home/speech/deeplearning/lib/python3.5/site-packages")

path = "audio/"
fp = open('people.txt', 'r')
person_number = (int)(fp.readline())
class_size = 100

for i in range(1, person_number+1):
    if i<10:
        personname = "00" + str(i)
    elif i>=10 and i<100:
        personname = "0" + str(i)
    else:
        personname = str(i)
    
    #set to m4a file directory 
    path2person = path + personname + "/"
    
    #make new directory for storing files that be modified using ffmpeg
    newdir =  path + "wav" + personname 
    mkdir = "mkdir " + newdir
    os.system(mkdir)

    for j in range(1, class_size+1):
        if j<10:
            fname = personname + "_00" + str(j) 
            output = fname + ".wav"
            filename = fname + ".m4a"
        elif j>=10 and j<100:
            fname = personname + "_0" + str(j)
            output = fname + ".wav"
            filename = fname + ".m4a"
        else:
            fname = personname + "_" + str(j)
            output = fname + ".wav"
            filename = fname + ".m4a"
        ffmpeg = "ffmpeg -i " + path2person + filename + " " + newdir + "/" + output
        os.system(ffmpeg)
