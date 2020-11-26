def split(word):
	return [char for char in word]

def toString(list):
    str = ""
    return (str.join(list))

#Hard coded index for every binary value, could be automated maybe?
def catIndex(word):
    if word == "Accounting":
        x = 0
    if word == "Compuer Science":
        x = 1
    if word == "Male":
        x = 2
    if word == "Female":
        x = 3
    if word == "3.0":
        x = 4
    if word == "3.5":
        x = 5 
    if word == "4.0":
        x = 6
    if word == "Italian":
        x = 7
    if word == "Spanish":
        x = 8
    if word == "Hindu":
        x = 9
    if word == "Judaism":
        x = 10
    return x

#To update the binary string
#The binary string is broken down into a list, the term will return an index,
#and that index will be updated with a 1 since it contains it
def updateBin(binary, word):
    ind = catIndex(word)
    list = split(binary)
    list[ind] = "1" 
    return (toString(list))

#This is initializing the binary representation, we could just have a defualt and work off of that.
def binRep(termList):
    binary = "00000000000"
    for y in range(len(termList)):
        term = termList[y]
        binary = updateBin(binary, term)
    return binary

#Demo
terms =['Accounting', 'Male', '3.0', 'Spanish', 'Judaism']



print(binRep(terms))
