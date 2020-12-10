from itertools import combinations 
f = open("input.txt", "r+").read().splitlines()

def part1():
    preamble = 25
    count = 0
    preambleHold = f[0:preamble]
    sumList = list(map(lambda x: int(x[0])+int(x[1]), (list(combinations(preambleHold, 2)))))


    for thing in f[preamble:]:
        print(thing)
        #print(sumList)
        if int(thing) not in sumList:
            print(f"{thing=}")
            break
        else:
            count+=1
            preambleHold = f[count:preamble+count]
            print(preambleHold)
            sumList = list(map(lambda x: int(x[0])+int(x[1]), (list(combinations(preambleHold, 2)))))
#part1()
goal = 22406676
def part2():
    flag = False
    clearedFile = [i for i in f if int(i) < goal]
    #print(clearedFile) 
    i = 0
    while i < len(clearedFile):
        startingPoint = [int(clearedFile[i-1])]
        for thing in clearedFile[i:]:
            print(sum(startingPoint))
            if sum(startingPoint) >= goal:
                i+=1
                break
            #print(f"adding {thing} to list")
            startingPoint.append(int(thing))
        #print(sum(startingPoint))
        if(sum(startingPoint) == goal):
            
            startingPoint.sort()
            print(startingPoint)
            print(int(startingPoint[0]+int(startingPoint[len(startingPoint)-1])))
            break
        else:
            #print(sum(startingPoint))
            i+=1


part2()
        