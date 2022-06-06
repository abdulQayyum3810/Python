import re
str="search inside of this text please search"
a=re.search(r"this",str)  # Returns a match object, and None if no match is found (search is casesensitive)
print(a.span())  # Tuple containing start and end position of searched string

# Other usefull methods are start(), end() and group()


# Advanced methods
print("Pattern Match")
pattern=re.compile(r"search")  # Match object
print(pattern.search(str))
print(pattern.findall(str))  # List of all matches
print(pattern.fullmatch(str))  # Returns match object if str and pattern are exact same otherwise none
print(pattern.match(str))  # Matches the pattern at initial of str and does not care about after (like words after pattern) returns match object, if pattern is not at the start of str the returns None


# website: https://regex101.com/
# Complex Examples

print("COMPLEX EXAMPLES")
pattern=re.compile(r"([a-zA-Z]).([a])")  # r is for raw string (take string as it is like no special meaning for \n,\t etc), ([a-zA-Z]) is a group, and . means any character
a=pattern.search(str)
print(a.group(1))  # Match for the first group 

# Email validation regx: first search email validation regx in google and get some expression used by others and try to understand and manipulate it 
# To understand use regx101.com 
