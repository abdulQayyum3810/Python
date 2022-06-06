import os
from datetime import datetime

# Print all attributes of an object/module
#print(os.__dir__()) # or dir(os)
print(os.getcwd()) # pwd
#os.chdir("C:/Users/AQ/Desktop/New Folder")
print(os.getcwd())
print(os.listdir())  # directory to be listed can be specified by default current

print("\n")
os.mkdir("OS-DEMO-1")  # creates specific dir if top level exists 
os.makedirs("OS-DEMO-2/Sub dir/sub2 dir")  # Makes deep level dir if top levels dont exist it will creat them (Recommende)
print(os.listdir("OS-DEMO-2"),"\n")
print(os.listdir())

print("\n")
os.rmdir("OS-DEMO-1")  # Deletes only specific dir (Recommended)
os.removedirs("OS-DEMO-2/Sub dir/sub2 dir")  # Deletes all tree (if empty)
print(os.listdir())


#os.rename("test.txt","test2.txt")
print(os.stat("test.txt"))  # stats object
modification_time=os.stat("test.txt").st_mtime # not human readable 
print(datetime.fromtimestamp(modification_time))  # now it is human readable

for dir_path, dir_names, file_names in os.walk(os.getcwd()): # walk through all dirs
    print("Current Path: ",dir_path)
    print("Directories: ", dir_names)
    print("Files: ", file_names)
    
    
""" print("\n",os.environ.get("TEMP"))
file_path=os.path.join(os.environ.get("TEMP"), "text.txt")  # getting environment variable path and joining it
print(file_path) """

#linux
""" print("\n",os.environ.get("HOME"))
file_path=os.path.join(os.environ.get("HOME"), "text.txt")  # getting environment variable path and joining it
print(file_path) """

print(os.path.basename("tax cop/fff fff/text.txt"))
print(os.path.dirname("tax copy/fff/text.txt"))
print(os.path.split("tax copy/fff/text.txt"))

print(os.path.exists("tax copy/fff/text.txt"))
print(os.path.isdir("tax copy/fff/text.txt"))
print(os.path.isfile("tax copy/fff/text.txt"))
print(os.path.splitext("tax copy/fff/text.txt"))




# LINUX
""" os.chdir("/mnt/d/Education/UET/CS/Python/CoreySchafer/Corey Schafers python")
print(os.listdir("./Decorator/"))
print(os.getcwd()) """
