import time; sT = time.time()
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines() + [""]
initSeeds = [int(seed) for seed in lineLst[0].split(": ")[1].split(" ")]
lineLst = lineLst[1:]
dctLst = []
for ind, line in enumerate(lineLst):
  if ":" in line:
    curDct = []
    for subInd, subLine in enumerate(lineLst[ind+1:lineLst[ind:].index("")+ind]):
      val1, val2, amnt = subLine.split(" ")
      val1 = int(val1); val2 = int(val2); amnt = int(amnt)
      curDct.append((val2, val1, amnt))
    dctLst.append(curDct)

locs = set()
for seed in initSeeds:
  num = seed
  for dct in dctLst:
    for numRange in dct:
      diff = num - numRange[0]
      if 0 <= diff < numRange[2]:
        num = numRange[1] + diff
        break
  locs.add(num)

seedRanges = [(initSeeds[ind], initSeeds[ind+1]) for ind in range(0, len(initSeeds), 2)]
sdRange2 = [(val[0], val[0] + val[1] - 1) for val in seedRanges]
dctLst2 = [sorted([(val[0], val[0] + val[2] - 1, val[1] - val[0])for val in dct]) for dct in dctLst]
locs2 = set()


def seedRangeRecurse(curRange, curDctInd):
  retLst = []
  lstUsed = []
  for chkRange in dctLst2[curDctInd]:
    if chkRange[0] <= curRange[0] <= chkRange[1] or chkRange[0] <= curRange[1] <= chkRange[1]:
      newRange = (max(chkRange[0], curRange[0]), min(chkRange[1], curRange[1]))
      lstUsed.append(newRange)
      updatedRange = (newRange[0] + chkRange[2], newRange[1] + chkRange[2])
      retLst.append(seedRangeRecurse(updatedRange, curDctInd + 1) if curDctInd + 1 < len(dctLst2) else [(newRange[0] + chkRange[2], newRange[1] + chkRange[2])])

  notFound = []
  if lstUsed:
    if lstUsed[0][0] != curRange[0]:
      lstUsed = [(curRange[0], curRange[0])] + lstUsed
    if lstUsed[-1][1] != curRange[1]:
      lstUsed += [(curRange[1], curRange[1])]
    for ind in range(len(lstUsed) - 1):
      if lstUsed[ind][1] != lstUsed[ind+1][0]:
        notFound.append((lstUsed[ind][1], lstUsed[ind+1][0]))
  else:
    notFound.append(curRange)
  for passRange in notFound:
    retLst.append(seedRangeRecurse(passRange, curDctInd + 1) if curDctInd + 1 < len(dctLst2) else [passRange])
  return [el for lst in retLst for el in lst]

allNums = []
for sRange in sdRange2:
  allNums += seedRangeRecurse(sRange, 0)


print(f"Part 1: {min(locs)}; Part 2: {min(allNums)[0]}")

print(f"Runtime: {(time.time() - sT)*1000:.6}ms")