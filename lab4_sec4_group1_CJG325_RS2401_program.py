# Programmers: Cameron Gruich (cjg325) and Ramesh Shrestha (rs2401)

# import randint to generate random numbers for our list
from random import randint

# import time to record function run times
from time import time

# import log2
from math import log2

# Function: binary_search(listVar, numVar)
# Purpose: Performn a binary search on an ordered list for a desired value.
# Paramters: listVar (The list to look through), numVar (The number to look for)
#____________________________________________________________________________________
def binary_search(listVar, numVar):

    listLength = len(listVar)

    l_index = 0
    r_index = listLength - 1

    while l_index <= r_index:
        mid_index = int((l_index + r_index)/2)

        if listVar[mid_index] == numVar:
            choice = mid_index

            # break the loop if the desired value has been found
            break
        
        elif listVar[mid_index] > numVar:
            # If the desired value is less than the middle index, stop looking to the right.
            r_index = mid_index - 1
            
        else:
            # If the desired value is more than the middle index, stop looking to the left.
            l_index = mid_index + 1

        if l_index > r_index:
            # return -1 for choice if the value is not found in the list
            choice = -1

    return choice
#____________________________________________________________________________________


# Function: sequential_search(listVar, valueVar)
# Purpose: Find a desired value in a list via sequential searching
# Parameters: listVar (the list we want to search in) and valueVar
# (the value we want to look for)
# _____________________________________________
def sequential_search(listVar, valueVar):

    listLen = len(listVar)

    for ind in range(0, listLen):
        
        if listVar[ind] == valueVar:
            choice = listVar.index(valueVar)
            
            # Break the loop if the desired value has been found
            break
        else:
            # return -1 for choice if the value is not found in the list
            choice = -1


    return choice
#____________________________________________________________________________________





# BEGIN MAIN PROGRAM #
#____________________________________________________________________________________

# Make lists to hold our single run times and C values for our algorithms later.
timeSeq = []
timeBin = []
timePyth = []

CSeq = []
CBin = []
CPyth = []





# Define a list of sample sizes we want to test.
sampleSize = [5000, 6000, 7000, 8000, 9000, 10000]

# Run the algorithms for a list of each sample size specified.
for value in sampleSize:
    unorderedList = []

    # Assign n random numbers to a list from 1 to n*n. Making the random integer range large helps prevent duplicates.
    for i in range(value):

        unorderedList.append(randint(1, value*value))

    # We may have duplicates numbers next to each other in the list, which may give inaccurate results for the algorithm.
    # So, we need to eliminate duplicates.
    # We can do this by converting the list into a set using set(). Sets are unordered collections that only accept unique values.
    # So, using set() will automatically remove duplicates.
    orderedSet = set(unorderedList)

    # Convert the set with removed duplicates back into a list again
    myList = list(orderedSet)

    # Sort the list
    myList.sort()

    listLength = len(myList)

    # If we did remove m duplicates from the list of size n, then our new list size is n - m.
    # To give accurate results, let's re-add m terms randomly to the list and re-sort it.
    # i.e. A list of 2000 values with 2 duplicates removed is now 1998 values,
    # so lets add 2 values back to the list and re-sort it to make a new 2000 value'd list.
    while listLength < value:
        
        myList.append(randint(1, value))

        myList.sort()

        listLength = len(myList)
    

    # Being timing for sequential search
    timeStart1 = time()
    for rep1 in range(10000):
        seqSearch = sequential_search(myList, myList[value - 1])
    # End timing
    timeEnd1 = time()

    timeDiff1 = timeEnd1 - timeStart1

    timeSeq.append(format((timeDiff1/10000), ".3g"))

    # C = f(n) / n because sequential search is linear growth

    C1 = timeDiff1 / (10000 * value)
    # Format for 3 significant values
    CSeq.append(format(C1, ".3g"))



    # Being timing for binary search
    timeStart2 = time()
    for rep2 in range(10000):
        binSearch = binary_search(myList, myList[value - 1])
    # End timing
    timeEnd2 = time()

    timeDiff2 = timeEnd2 - timeStart2

    timeBin.append(format((timeDiff2/10000), ".3g"))



    # C = f(n)/log2(n) because the binary search is base 2 logarithmic growth (f(n) = C*log2(n))
    C2 = timeDiff2 / (10000*log2(value))
    # Format for 3 significant values
    CBin.append(format(C2, ".3g"))

    # Being timing for Python built in search
    timeStart3 = time()
    for rep3 in range(10000):
        indPyth = myList.index(myList[value - 1])
    # End timing
    timeEnd3 = time()

    timeDiff3 = timeEnd3 - timeStart3

    timePyth.append(format((timeDiff3/10000), ".3g"))

    # C = f(n) / n because the python index search is linear growth
    C3 = timeDiff3 / (10000 * value)
    # Format for 3 significant values
    CPyth.append(format(C3, ".3g"))

    # put try or except code here



#___________________________________________#
# Print the results to the user.
print("\n\n")

# Sequential Search Results
print("SAMPLE SIZES")
print(sampleSize)
print("\nRESULTS")
print("Sequential Search Results")
print("Times")
print(timeSeq)
print("Sequential Search C Values")
print(CSeq)

# Binary Search Results
print("\nBinary Search Results")
print("Times")
print(timeBin)
print("Binary Search C Values")
print(CBin)

# Python Built In Search Results
print("\nPython Built In Search Results")
print("Times")
print(timePyth)
print("Python Build In Search C Values")
print(CPyth)
