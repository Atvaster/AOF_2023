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
locs2 = set()
#for sRange in seedRanges:
sRange = seedRanges[0]
  for seed in range(sRange[0], sRange[0] + sRange[1]):
    num = seed
    for dct in dctLst:
      for numRange in dct:
        diff = num - numRange[0]
        if 0 <= diff < numRange[2]:
          num = numRange[1] + diff
          break
    locs2.add(num)

print(min(locs), min(locs2))