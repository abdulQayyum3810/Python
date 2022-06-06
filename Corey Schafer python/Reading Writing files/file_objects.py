
""" # Efficiently reading large files
with open("test.txt") as f:  # f is variable (here file object)
    # reading from large files and not running out of memory
    for line in f:  # only one line is being stored in memory
        print(line, end="")
 """
 # Second way of fficiently reading large files
with open("test.txt","r+") as f:
    size_to_read=100
    f_content=f.read(size_to_read)  # will read first 10 characters and remembers the cursor
    
    # print(f.tell()) # cursor's current position
    # f.seek(2) # set cursor position
    while len(f_content)>0:
        print(f_content)
        f_content=f.read(size_to_read)
    print(f.tell())
    
with open("test2.txt","a") as f:  # append mode remmebers the cursors but opperation is not dependent on cursor
    f.seek(3)
    print(f.tell())
    f.write("writting from 3")
    print(f.tell())

# Reading from one file and writting to other
with open("test.txt","r") as rf:
    with open("test_copy.txt","w") as wf:
        for line in rf:
            wf.write(line)

#  Reading from one file and writting to other in byte mode
with open("pic.jpg","rb") as rf:
    with open("pic_copy.jpg","wb") as wf:
        for line in rf:
            wf.write(line)
            
#  Second way Reading from one file and writting to other in byte mode
with open("pic.jpg","rb") as rf:
    with open("pic_junck.jpg","wb") as wf:
        junck_size=40
        junck_content=rf.read(junck_size)
        while len(junck_content)>0:
            wf.write(junck_content)
            junck_content=rf.read(junck_size)

with open("pic.jpg","rb") as rf:
    with open("pic_shattered.jpg","wb") as wf:
        for line in rf:
            wf.write(line)
            wf.seek(wf.tell()-5)