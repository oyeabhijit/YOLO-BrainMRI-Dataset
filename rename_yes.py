import os

path=os.chdir(input("Enter folder path for YES images: "))

i=0
for file in os.listdir(path):
    new_file_name = "yes{}.jpeg".format(i)
    os.rename(file, new_file_name)
    i=i+1