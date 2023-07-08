x = int(input())
y = int(input())
z = int(input())
n = int(input())

maxUtil = {}

if x >= n:
    xDiff = x - n
    maxUtil[xDiff] = "L1"
if y >= n:
    yDiff = y - n
    maxUtil[yDiff] = "L2"
if z >= n:
    zDiff = z - n
    maxUtil[zDiff] = "L3"

print(maxUtil[min(maxUtil.keys())])
