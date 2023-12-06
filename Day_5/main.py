#Import and simple init line list
import time; sT = time.time()
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
initSeeds = [int(seed) for seed in lineLst[0].split(": ")[1].split(" ")]
lineLst = lineLst[1:] + [""]


#
mapLst = []
for ind, line in enumerate(lineLst):
  if ":" in line:
    curConvert = []
    for subInd, subLine in enumerate(lineLst[ind+1:lineLst[ind:].index("")+ind]):
      val1, val2, amnt = subLine.split(" ")
      curConvert.append((int(val2), int(val1), int(amnt)))
    mapLst.append(curConvert)


locs = set()
for seed in initSeeds:
  num = seed
  for dct in mapLst:
    for numRange in dct:
      diff = num - numRange[0]
      if 0 <= diff < numRange[2]:
        num = numRange[1] + diff
        break
  locs.add(num)


seedRanges = [(initSeeds[ind], initSeeds[ind] + initSeeds[ind+1] - 1) for ind in range(0, len(initSeeds), 2)]
mapRanges = [sorted([(val[0], val[0] + val[2] - 1, val[1] - val[0])for val in dct]) for dct in mapLst]


def seedRangeRecurse(curRange, curDctInd):
  retLst = []
  lstUsed = []
  for chkRange in mapRanges[curDctInd]:
    if chkRange[0] <= curRange[0] <= chkRange[1] or chkRange[0] <= curRange[1] <= chkRange[1]:
      newRange = (max(chkRange[0], curRange[0]), min(chkRange[1], curRange[1]))
      updatedRange = (newRange[0] + chkRange[2], newRange[1] + chkRange[2])
      lstUsed.append(newRange)
      retLst.append(seedRangeRecurse(updatedRange, curDctInd + 1) if curDctInd + 1 < len(mapRanges) else [updatedRange])

  if not lstUsed:
    retLst.append(seedRangeRecurse(curRange, curDctInd + 1) if curDctInd + 1 < len(mapRanges) else [curRange])
    return [el for lst in retLst for el in lst]

  if lstUsed[0][0] != curRange[0]:
    lstUsed = [(curRange[0], curRange[0])] + lstUsed
  if lstUsed[-1][1] != curRange[1]:
    lstUsed = lstUsed + [(curRange[1], curRange[1])]
  for ind in range(len(lstUsed) - 1):
    if lstUsed[ind][1] != lstUsed[ind+1][0]:
      passRange = (lstUsed[ind][1], lstUsed[ind+1][0])
      retLst.append(seedRangeRecurse(passRange, curDctInd + 1) if curDctInd + 1 < len(mapRanges) else [passRange])

  return [el for lst in retLst for el in lst]


allNums = [el for sRange in seedRanges for el in seedRangeRecurse(sRange, 0)]

print(f"Part 1: {min(locs)}; Part 2: {min(allNums)[0]}")

print(f"Runtime: {(time.time() - sT)*1000:.6}ms")