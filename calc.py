from itertools import combinations 
f = open("input.txt", "r+").read().splitlines()
f = list(map(lambda x: int(x), f))
f.sort()
f.append(f[-1]+3)
f = [0]+ f
print(f)
for thing in range(len(f)):
    if(thing < len(f)-1):
        f[thing] = (f[thing+1] - f[thing])
count3=f.count(3)
count1=f.count(1)
print(count3*count1)
f = open("input.txt", "r+").read().splitlines()
f = list(map(lambda x: int(x), f))
f.sort()
f.append(f[-1]+3)
final = {}
final[0] = 1
for thing in f:
    #I think this is called
    final[thing] = final.get(thing - 3, 0) + final.get(thing - 2, 0) + final.get(thing - 1, 0) 

print(f'Answer: {final[f[-1]]}')