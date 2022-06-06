
with open("test.txt") as f:  # f is variable (here file object)
    # reading from large files and not running out of memory
    for line in f:  # only one line is being stored in memory
        print(line, end="")
