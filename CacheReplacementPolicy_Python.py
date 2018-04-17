##Casey Floyd  -  CS440  -  Project 4
from random import choice, randint
from string import ascii_uppercase as AU

##get user input
pattern = int(input("Enter page reference pattern length: "))
pages = int(input("Enter number of unique pages: "))
slots = int(input("Enter number of slots: "))

##gathering possible letter choices
letters = list(AU)[:pages]

##creating the reference string
refString = [choice(letters) for i in range(pattern)]

##initializing spots for cache entry
s = [None for j in range(slots)]

##FIFO Algorithm
def FIFO(pattern, s):
    hitcount = 0
    i = 0
    spots = s[:]

    ##initializing print statement
    output = ["FIFO  " + str(j) + ": " for j in range(len(spots) + 1)]
    output[0] = "\nRef Str: " + " ".join(pattern)

    for j in pattern:
        ##if item exists and a cache hit happens
        if j in spots:
            for g in range(1,len(output)):
                if g - 1 == spots.index(j):
                    output[g] += "+ "
                    hitcount+=1
                else:
                    output[g] += "  "
        ##if there is an empty slot           
        elif None in spots:
            for g in range(1,len(output)):
                if g - 1 == spots.index(None):
                    output[g] += j + " "
                else:
                    output[g] += "  "
            spots[spots.index(None)] = j
        ##if there are no empty slots
        else:
            for g in range(1,len(output)):
                if g - 1 == i:
                    output[g] += j + " "
                else:
                    output[g] += "  "
            spots[i] = j
            if i < len(spots) - 1:
                i += 1
            else:
                i = 0
    for i in range(len(output)):
        print(output[i])		
    return(hitcount)

##LRU Algorithm
def LRU(pattern, s):
    hitcount = 0
    last = [0 for h in s]
    spots = s[:]

    output1 = ["LRU  " + str(j) + ":  " for j in range(len(spots) + 1)]
    output1[0] = "\nRef Str: " + " ".join(pattern)

    for j in range(len(pattern)):
        ##if item exists and a cache hit happens
        if pattern[j] in spots:
            for g in range(1,len(output1)):
                if g - 1 == spots.index(pattern[j]):
                    output1[g] += "+ "
                    hitcount+=1
                else:
                    output1[g] += "  "
            last[spots.index(pattern[j])] = j
        ##if there is an empty slot
        elif None in spots:
            i = spots.index(None)
            for g in range(1, len(output1)):
                if g - 1 == i:
                    output1[g] += pattern[j] + " "
                else:
                    output1[g] += "  "
            spots[i] = pattern[j]
            last[i] = j
        ##if there are no empty slots
        else:
            i = last.index(min(last))
            for g in range(1, len(output1)):
                if g - 1 == i:
                    output1[g] += pattern[j] + " "
                else:
                    output1[g] += "  "
            spots[i] = pattern[j]
            last[i] = j

    for i in range(len(output1)):
        print(output1[i])
    return(hitcount)
    
def MIN(pattern,s):
    hitcount = 0
    spots = s[:]

    ##initializing print statement
    output2 = ["MIN  " + str(j) + ":  " for j in range(len(spots) + 1)]
    output2[0] = "\nRef Str: " + " ".join(pattern)

    for j in range(len(pattern)):
	##if item exists and a cache hit happens
        if pattern[j] in spots:
            for g in range(1,len(output2)):
                if g - 1 == spots.index(pattern[j]):
                    output2[g] += "+ "
                    hitcount+=1
                else:
                    output2[g] += "  "

	##if there is an empty slot
        elif None in spots:
            i = spots.index(None)
            for g in range(1,len(output2)):
                if g - 1 == i:
                    output2[g] += pattern[j] + " "
                else:
                    output2[g] += "  "
            ##setting spot to missed page
            spots[i] = pattern[j]

	##if there are no empty slots
        else:
            ##find when it will be used next
            nextUse = []
            ##assign an index to each item
            for g in spots:
                if g in pattern[j:]:
                    nextUse.append(pattern[j:].index(g) + j)
                else:
                    nextUse.append(200)
	    ##setting slot index to page furthest from current position
            if 200 in nextUse:
                ##setting the index to the first one no longer on the list, if any apply
                i = nextUse.index(200)
            else:
                i = spots.index(pattern[max(nextUse)])
            for g in range(1,len(output2)):
                if g - 1 == i: output2[g] += pattern[j] + " "
                else: output2[g] += "  "
            spots[i] = pattern[j]

    for i in range(len(output2)):
        print(output2[i])
    return(hitcount)

def RAND(pattern,s):
    hitcount = 0
    spots = s[:]

    ##initializing print statement
    output3 = ["RAND  " + str(j) + ": " for j in range(len(spots) + 1)]
    output3[0] = "\nRef Str: " + " ".join(pattern)

    for j in pattern:
        ##if item exists and a cache hit happens
        if j in spots:
            for g in range(1,len(output3)):
                if g - 1 == spots.index(j):
                    output3[g] += "+ "
                    hitcount += 1
                else:
                    output3[g] += "  "
        ##if there is an empty slot
        elif None in spots:
            i = spots.index(None)
            for g in range(1,len(output3)):
                if g - 1 == i:
                    output3[g] += j + " "
                else:
                    output3[g] += "  "
                spots[i] = j
        ##if there are no empty slots
        else:
            ##randomly find an index to replace
            i = randint(0,len(spots) - 1)
            for g in range(1,len(output3)):
                if g - 1 == i:
                    output3[g] += j + " "
                else:
                    output3[g] += "  "
            spots[i] = j
            
    for i in range(len(output3)):
        print(output3[i])
    return(hitcount)
                

##getting number of hits of each algorithm
fifo = FIFO(refString, s)
lru = LRU(refString, s)
m = MIN(refString, s)
rand = RAND(refString, s)

##getting the hit rate by dividing number of hits by how many pages
fHitRate = int(fifo)/int(pattern)
lHitRate = int(lru)/int(pattern)
mHitRate = int(m)/int(pattern)
rHitRate = int(rand)/int(pattern)

##print out hit rates for each
print("\nCache Hit Rates:")
print("\nFIFO : " + str(fifo) + " of " + str(pattern) + " = " + str(fHitRate))
print("LRU  : " + str(lru) + " of " + str(pattern) + " = " + str(lHitRate))
print("MIN  : " + str(m) + " of " + str(pattern) + " = " + str(mHitRate))
print("RAND : " + str(rand) + " of " + str(pattern) + " = " + str(rHitRate))

#finding highest and lowest hit rates
hitRateList = [fHitRate, lHitRate, mHitRate, rHitRate]
hrMax = max(hitRateList)
hrMin = min(hitRateList)

print()

if hrMax == fHitRate: 
    print("Best:  FIFO")
if hrMax == lHitRate:
    print("Best:  LRU")
if hrMax == mHitRate:
    print("Best:  MIN")
if hrMax == rHitRate:
    print("Best:  RAND")

if hrMin == fHitRate:
    print("Worst: FIFO")
if hrMin == lHitRate:
    print("Worst: LRU")
if hrMin == mHitRate:
    print("Worst: MIN")
if hrMin == rHitRate:
    print("Worst: RAND")


