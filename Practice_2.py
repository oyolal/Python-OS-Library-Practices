#In this practice we will cover renaming files
import os, sys
path = os.getcwd()
filenames = os.listdir(path)
# listing directories
print "The dir is: %s"%os.listdir(os.getcwd())
# Renaming all files to lower cases
for i in filenames:
# Take a look .replace() <-- search it on google see how it works
# Do couple exercise yourself
    os.rename(i,i.replace(" ", "-"))
print "Successfully lowered."
# listing directories after renaming "tutorialsdir"
print "The dir is: %s" %os.listdir(os.getcwd())
