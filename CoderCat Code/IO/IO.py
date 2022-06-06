# I: Means getting input from outside world
# O: Giving output to the outside world
# Outside world: Database, website, file etc



my_file=open("text.txt")  # Opens a file and returns a file object
# print(my_file) # Prints information
print(my_file.read())  # Read the file and remembers the cursor position 
print(my_file.read())  # Nothing will be printed as cursor is at the end
# To print again we have to move the cursor back to the position where we want to start reading
my_file.seek(0)  # Moves the cursor to position 0 i.e. to start of the file
print(my_file.read())

my_file.seek(0)  # set cursor to start for next opperations
print("Readline method")

print(my_file.readline())  # will read the one line starting from cursor current position
print(my_file.readline())  
print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())  # will read the all lines starting from cursor current position and return them in a list,it also remembers the cursor position
print(my_file.readlines())  # [] will be printed as cursor is at last position


my_file.close()  # with method open() we have to close the files manually


# Standard way to read a file
print("\nREADING WITH STATDARD METHOD")
with open("text.txt") as my_file:  #open file as my_file object
    print(my_file.read())  # Perform any oppperation and no need to close the file
    

# MODES
# Every time file is opened cursor position is reset
# Other opperations: Read, write, append (all opperations remembers the cursor except append)
# mode r: (by default)
# mode w:it creates the file if does not exist already, if file is already present it will replace the file (assumes that new file is created with the same name so overwrites the file)
# mode a: appends to the file, creates file if does not exist, and remembers the cursor but its opperation is dependent on currsor position (i.e. it always writes at the end of the file)
# mode r+:  read and write >> both opperations remembrs the cursor position, 
# for write opperation start writting from cursor position and overwrite the text after cursor position upto the point where this writing ends
# mode rb, wb: read and write in byte mode
with open("text2.txt",mode="r+") as my_file:  # we can access my_file variable in later code but can only do info opperations (my_file.name, etc)
    text=my_file.write("hello boy") # As cursor is at start and mode is r+ so it will start writting from start and overwrite the text in the file upto the point where this writing ends set cursor using seek and start writting where we want
    print(text)  # prints how many characters are added
    
with open("text.txt",mode="a") as my_file:
    my_file.write("I am added at the end")
    
# If file does not exist in the same directory Then relative and absolute path can be given
# Relative path
with open("IO_Relative_path/text3.txt",mode="r") as my_file:
    print(my_file.read())

# Absolute path for linux 
with open("/mnt/c/users/aq/Desktop/New Folder/channels.txt",mode="r") as my_file:
    print(my_file.read())
    
# Absolute path for windows
""" with open("C:/Users/AQ/Desktop/New Folder/channels.txt",mode="r") as my_file:
    print(my_file.read()) """
    
#Handling errors

try:
    with open("text7.txt",mode="r") as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("file does not exist")