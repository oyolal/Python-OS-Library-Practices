import os
'''In this practice i will practice renaming files'''
path = os.getcwd()
filenames = os.listdir(path)
# listing directories
print "The directories are: %s"%os.listdir(os.getcwd())
# Renaming all files to lower cases
for i in filenames:
    os.rename(i,i.replace(" ", "-").lower())
print "Successfully lowered."
# listing directories after lowering all files
print "The directories are: %s" %os.listdir(os.getcwd())
print "Let's fix it back shall we"
for i in filenames:
#obviously .capitalize()
    os.rename(i,i.replace(" ", "-").capitalize())
print "The directories are: %s" %os.listdir(os.getcwd())
