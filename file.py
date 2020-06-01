#importing OS module
import os

#Reading inputs
PATH=input("Enter the path to scan : ")
FORMAT=input("Enter the file format as .jpg or .png : ")

# Adding a . if not entered by user
FORMAT="."+FORMAT if "." not in FORMAT else FORMAT

#Grabbing all file names in given directory
data=os.listdir(PATH)

#Filtering files with given format
filtered=list(filter(lambda a:FORMAT in a,data))

print("TOTAL FILES ARE ",len(filtered))
for each in filtered:
    print(each)