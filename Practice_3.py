import os
'''We will create the next practice file with this practice'''
file_name = "Practice_4.py"
# Search for open() , with and os.utime
# See what they are doing
with open(file_name, 'a'):
        os.utime(file_name, None)
print os.listdir(os.getcwd())
print "See now we have file named %s" %file_name
