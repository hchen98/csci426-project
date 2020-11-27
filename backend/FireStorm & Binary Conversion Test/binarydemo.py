def split(word):
	return [char for char in word]

def toString(list):
    str = ""
    return (str.join(list))

#Hard coded index for every binary value, could be automated maybe?
def catIndex(word):
    # locating the user profile (single) element to sub-category
    # INPUT: a user profile key word <-- str
    # OUTPUT: sub-category position <-- int

    if word == "Accounting":
        index = 0
    if word == "Compuer Science":
        index = 1
    if word == "Male":
        index = 2
    if word == "Female":
        index = 3
    if word == "3.0":
        index = 4
    if word == "3.5":
        index = 5 
    if word == "4.0":
        index = 6
    if word == "Italian":
        index = 7
    if word == "Spanish":
        index = 8
    if word == "Hindu":
        index = 9
    if word == "Judaism":
        index = 10
    return index


#To update the binary string
#The binary string is broken down into a list, the term will return an index,
#and that index will be updated with a 1 since it contains it
def updateBin(binary, word):
    ind = catIndex(word)
    list = split(binary)
    list[ind] = "1" 
    return (toString(list))

#This is initializing the binary representation, we could just have a defualt and work off of that.
def formBin(termList):
    binary = "00000000000"
    for item in termList:
        binary = updateBin(binary, item)
    return binary

# dummy entry: assume this is user profile in key words
profile =['Accounting', 'Male', '3.0', 'Spanish', 'Judaism']

print(formBin(profile))
# output: 10101000101