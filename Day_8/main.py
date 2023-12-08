import math
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()

pattern = [0 if char == "L" else 1 for char in lineLst[0]]
nodeDct = {(w:=line.split(" = "))[0]:((v:=w[1][1:-1].split(", "))[0], v[1]) for line in lineLst[2:]}


def getNumSteps():
  flag = False
  curVal = "AAA"
  stepNum = 0
  while flag != True:
    for move in pattern:
      curVal = nodeDct[curVal][move]
      stepNum += 1
      if curVal == "ZZZ":
        return stepNum


def getCycles():
  stepNum = 0
  initLocs = [val for val in nodeDct if val[2] == "A"]
  repeats = [0 for i in range(len(initLocs))]
  cycles = [0 for i in range(len(initLocs))]
  stepNums = [0 for i in range(len(initLocs))]
  while True:
    for move in pattern:
      for ind in range(len(initLocs)):
        initLocs[ind] = nodeDct[initLocs[ind]][move]
        if initLocs[ind][2] == "Z":
          repeats[ind] += 1
          if repeats[ind] == 2:
            cycles[ind] = stepNum - stepNums[ind]
          stepNums[ind] = stepNum
      stepNum += 1
      if all(cycles):
        return cycles


print(f"Part 1: {getNumSteps()}, Part 2: {math.lcm(*getCycles())}")