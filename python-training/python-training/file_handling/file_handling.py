#File handling

#file operation can be done in the following order:
#step1: Open a file
#step2: read or write a file - performing operation
#step3: close the file

#opening a file
#open()
#syntax :
#fileObj=open(filename,accessmode, buffering)


#files can be accesed using various modes
#1. read
#2. write
#3. append

#opens a file in read mode

fileptr=open("file.txt","r")

if fileptr:
    print("file opened successfully!")
fileptr.close()