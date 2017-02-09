import os
import fnmatch
import shutil
import datetime
import calendar

os.chdir("D:\Backup")
#Here I have my videos and photos you can write the directory that you have your files
#code below is setting variable to current date
now = datetime.datetime.now()
newFolderName = str(now.day) + ' ' + calendar.month_name[now.month] + ' ' + str(now.year)
#Creating new directories for our files that we backed up
os.mkdir("Videos")
os.mkdir("Photos")
os.mkdir("ScreenShots")

#looping through directory and putting every file where it belongs
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.JPG'):        #Finding Matching file
        shutil.move(file, "D:\Backup\Photos") #Moving file
    elif fnmatch.fnmatch(file, '*.MOV'):
        shutil.move(file, "D:\Backup\Videos")
    elif fnmatch.fnmatch(file, '*.mp4'):
        shutil.move(file, "D:\Backup\Videos")
    elif fnmatch.fnmatch(file, '*.PNG'):
        shutil.move(file, "D:\Backup\ScreenShots")
    elif fnmatch.fnmatch(file, '*.AAE'):
        os.remove(file)
#after putting every thing where it belongs we change name to
#current day_month_year
os.chdir("..")
os.rename("Backup",a) #change the Backup name with your folder name
