#Benjamin Siege
import random
import time
# use random to randomize puzzles
def genPuzzle(numbS):
    puzzle = []
    for x in range (numbS+1):
        a = list(range(1,numbS+1))#list of possible numbers
        isValid = False
        while (not isValid):
            random.shuffle(a)
            while(a[0]!=1):
                # print(a)
                a.append(a.pop(0))
            isValid = a not in puzzle #not add duplicate pieces
        puzzle.append(a)
    # print(puzzle)
    return puzzle
#check if the puzzle is a solution
def checkEqual(puzzle):
    a = len(puzzle)-1
    for x in range(a):
        if(not(puzzle[0][x] == puzzle[x+1][0])):# check center
            return False
    tempA = puzzle[1:]
    # print("\n")
    for x in range(len(tempA)):
        if(not (tempA[x][-1]==tempA[(x+1)%a][1])):#check side edges
            return False #if discrepency found return false

    # print("yay")
    return True

#brute force search
def permutation(lst):#find all permutations
    if len(lst) == 0:
        return []
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
    l = []
    #for each item in the list
    for i in range(len(lst)):
       m = lst[i] #select that item
       remLst = []
       remLst = lst[:i] + lst[i+1:] #select the rest of the list
       for p in permutation(remLst): #recur for remainder of list
            l.append([m] + p)#append each remainder

    return l

#bredth first search
def permutationP(lst,size):
    if len(lst) == 0:
        return []
    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]
    l = []
    #for each item in the list
    for i in range(len(lst)):
       m = lst[i] #select that item
       remLst = []
       remLst = lst[:i] + lst[i+1:] #select the rest of the list
       for p in permutationP(remLst,size): #recur for remainder of list
            mC = m[:]
            while(p[0][len(p)-1] != mC[0]):
                mC.append(mC.pop(0))#orient each piece towards the centers
            if(((p[-1][-1]==mC[1]) or len(p)<2) and (len(p)+1<size or (p[1][1]==mC[-1]))): #check if it fits
                l.append(p+[mC])#append each remainder

    # print(m)
    return l


#rotates each piece of a puzzle to the center
def rotateToCenter(puzzle):
    for index in range(len(puzzle)-1):
        while(puzzle[0][index] != puzzle[index+1][0]):
            puzzle[index+1].append(puzzle[index+1].pop(0))

    return puzzle

def makeCopyList(list):
    for x in range(len(list)):
        list[x] = list[x].copy()
    return list

#brute force solution
def bruteForceSingle(size):
    puzzle = genPuzzle(size)
    states = permutation(puzzle)#create all possible arrangements
    print(len(states))
    for state in states:
        state = rotateToCenter(makeCopyList(state))
        if(checkEqual(state)):#check if the solution is correct
            return state
    return []
#generate a single solution
def pruneSingle(size):
    solutions = prune(size)
    if(len(solutions)>0):
        return solutions[0]
    return []

#make each list into a tuple and then use set() to check uniqueness, was used for error checking
def checkUniqLen(listL):
    a = set();
    for item in listL:
        b = []
        for num in item:
            c = (num[0],num[1],num[2],num[3],num[4],num[5])
            b.append(c)
        a.add((b[0],b[1],b[2],b[3],b[4],b[5],b[6]))
    print(len(a),len(listL))

#generate all possible solutions
def prune(size):
    puzzle = genPuzzle(size)#generate puzzle
    solutions= permutationP(puzzle,size+1)#
    return solutions



#counts the possible
def countSols(number,size):
    start = time.time()
    numSols = []
    for x in range(number):
        numSols.append(len(prune(size)))
    print(time.time()-start)
    return numSols

def average(list):
    return sum(list)/len(list)

#prints the time elapsed for the calculation of each puzzle
def getTimeForEachPuzzle():
    for x in range(5,13):
        nStart = time.time()
        prune(x)
        time.time()-nStart

def MAIN():
    puzzle =[[1,6,5,4,3,2],[1,6,4,2,5,3],[1,2,3,4,5,6],[1,6,2,4,5,3],[1,4,3,6,5,2],[1,4,6,2,3,5],[1,6,5,3,2,4]]
    solutions = permutationP(puzzle,len(puzzle))
    # print(solutions)
    return solutions
# testPuzz = [[1,2,3,4],[1,4,2,3],[2,1,3,4],[3,2,4,1],[4,3,1,2]]
# practPuzz = [[1,2,3],[1,2,3],[1,2,3]]
# start = time.time()
# print(bruteForceSingle(4))
# print(bruteForceSingle(2))
# print("PRUNE:",round(time.time()-start,4),"Seconds")
# start = time.time()
# print(bruteForceSingle(8))
# print("BRUTE:",round(time.time()-start,4),"Seconds")
# print(bruteForceSingle(2))
# print(permutation([1,2,3,4]))
# solvePuzz= [[1,2,3,4,5],[1,5,3,2,4],[2,1,4,3,5],[3,5,2,4,1],[4,1,2,3,5],[5,4,3,2,1]]
# print(checkEqual(solvePuzz))
# print(prune(4))
print(MAIN())
