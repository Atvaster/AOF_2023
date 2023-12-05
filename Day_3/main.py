import numpy
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()

numSet = {*"0123456789"}
excludeSet = numSet | {"."}
pzlW = len(lineLst[0])
pzlH = len(lineLst)
puzzle = "".join(lineLst)

def checkNbrs(board, x, y):
  if x > 0:
    if board[x - 1 + y*pzlW] not in excludeSet:
      return True
    if y > 0 and board[x - 1 + (y - 1)*pzlW] not in excludeSet:
      return True
    if y < pzlH - 1 and board[x - 1 + (y + 1)*pzlW] not in excludeSet:
      return True
  if x < pzlW - 1:
    if board[x + 1 + y*pzlW] not in excludeSet:
      return True
    if y > 0 and board[x + 1 + (y - 1)*pzlW] not in excludeSet:
      return True
    if y < pzlH - 1 and board[x + 1 + (y + 1)*pzlW] not in excludeSet:
      return True
  if y > 0:
    if board[x + (y - 1)*pzlW] not in excludeSet:
      return True
  if y < pzlH - 1:
    if board[x + (y + 1)*pzlW] not in excludeSet:
      return True
  return False

numLst = []
for y in range(pzlH):
  curNum = ""
  prev = False
  valid = False
  for x in range(pzlW):
    char = puzzle[x + y*pzlW]
    if char in numSet:
      prev = True
    if prev:
      if char in numSet:
        curNum += char
        if checkNbrs(puzzle, x, y):
          valid = True
      else:
        prev = False
        if valid:
          numLst.append(int(curNum))
        valid = False
        curNum = ""
  if curNum and valid:
    numLst.append(int(curNum))
print(sum(numLst))

numDict = {}
numDictSecondary = {}
for y in range(pzlH):
  curNum = ""
  prev = False
  valid = False
  for x in range(pzlW):
    char = puzzle[x + y*pzlW]
    if char in numSet:
      prev = True
    if prev:
      if char in numSet:
        curNum += char
        if checkNbrs(puzzle, x, y):
          valid = True
      else:
        prev = False
        if valid:
          for i in range(len(curNum)):
            numDict[x + y*pzlW - i - 1] = curNum
            numDictSecondary[x + y*pzlW - i - 1] = x + y*pzlW - 1
        valid = False
        curNum = ""
  if curNum and valid:
    for i in range(len(curNum)):
      numDict[x + y*pzlW - i - 1] = curNum
      numDictSecondary[x + y*pzlW - i - 1] = x + y*pzlW - 1

ratioLst = []
for pos, val in enumerate(puzzle):
  if val == "*":
    numPoses = []
    x, y = pos%pzlW, pos//pzlH
    if x > 0:
      if puzzle[x - 1 + y*pzlW] in numSet:
        numPoses.append(x - 1 + y*pzlW)
      if y > 0 and puzzle[x - 1 + (y - 1)*pzlW] in numSet:
        numPoses.append(x - 1 + (y - 1)*pzlW)
      if y < pzlH - 1 and puzzle[x - 1 + (y + 1)*pzlW] in numSet:
        numPoses.append(x - 1 + (y + 1)*pzlW)
    if x < pzlW - 1:
      if puzzle[x + 1 + y*pzlW] in numSet:
        numPoses.append(x + 1 + y*pzlW)
      if y > 0 and puzzle[x + 1 + (y - 1)*pzlW] in numSet:
        numPoses.append(x + 1 + (y - 1)*pzlW)
      if y < pzlH - 1 and puzzle[x + 1 + (y + 1)*pzlW] in numSet:
        numPoses.append(x + 1 + (y + 1)*pzlW)
    if y > 0:
      if puzzle[x + (y - 1)*pzlW] in numSet:
        numPoses.append(x + (y - 1)*pzlW)
    if y < pzlH - 1:
      if puzzle[x + (y + 1)*pzlW] in numSet:
        numPoses.append(x + (y + 1)*pzlW)

    seen = set()
    secondSet = set()
    for num in numPoses:
      secondSet.add(int(numDict[numDictSecondary[num]]))

    if len(secondSet) == 2:
      ratio = numpy.prod([*secondSet])
      ratioLst.append(ratio)

print(sum(ratioLst))
