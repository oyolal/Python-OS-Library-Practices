import os
import shutil
os.chdir("..")
desktopPath = os.getcwd()

# Checking if there is directory exist named Backup
# if no creating one
def directory_check():
    os.chdir("D:")
    if os.path.isdir("Backup") == True:
        break
    else:
        os.mkdir("Backup")
#Copying all files from Iphone to D:/Backup folder
def copying(src, dst, symlinks=False, ignore=None):
#    os.chdir("Iphone media") --> This part is missing since iphone's are not
#   mounted as drives without jailbreak
    src = os.getcwd()
    dst = "D:\Backup"
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        shutil.copytree(s, d, symlinks, ignore)


def main():
    dircheck()
    copying()
