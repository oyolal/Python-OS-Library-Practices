import os
'''Practice on getting current directory, creating a new directory and deleting it,
changing directory
'''
print "Current directory"
#Getting current directory
print os.getcwd()
#Going to the Desktop directory
os.chdir("")

print "Now we are at Users"
def mkdir():
    print "Current directory"
    print os.getcwd()
    print "Let's create a new directory right here"
    #Creating a new directory named new
    os.mkdir("new")
    print "See we have a new directory called new"
    #Lists the directories
    print os.listdir(os.getcwd())
    print "Let's delete the directory we have created"
    #This removes the directory we have created
    os.rmdir("new")
    print os.getcwd()
    print "As we can see our directory that we have created is gone"
