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

def seedRangeRecurse(curRange, dctInd):
  pieces = []
  for ind, numRange in enumerate(dctLst[dctInd]):
    if numRange[0] <= curRange[0] <= numRange[0] + numRange[2] or numRange[0] <= curRange[0] + curRange[1] <= numRange[0] + numRange[2]:
      start = max(curRange[0], numRange[0])
      step = curRange[1] if curRange[0] + curRange[1] < numRange[0] + numRange[2] else numRange[2]
      splitRange = (start, step)
      pieces.append((splitRange, ind))
  if pieces:
    pieces.sort(key = lambda x: x[0][0])
    newPieces = []
    if pieces[0][0][0] != curRange[0]:
      newPieces.append(((curRange[0], pieces[0][0][0] - curRange[0]), -1))
    for ind, piece in enumerate(pieces):
      newPieces.append(piece)
      piece = piece[0]
      if ind + 1 < len(pieces) and piece[0] + piece[1] != pieces[ind+1][0][0]:
        newPieces.append(((piece[0] + piece[1], pieces[ind+1][0] - piece[0] + piece[1]), -1))
    if pieces[-1][0][0] + pieces[-1][0][1] != curRange[0] + curRange[1]:
      newPieces.append(((pieces[-1][0][0] + pieces[-1][0][1], curRange[1] - pieces[-1][0][0] + pieces[-1][0][1]), -1))

    if dctInd + 1 < len(dctLst):
      mainLst = []
      for piece, ind in newPieces:
        if ind == -1:
          mainLst.append(seedRangeRecurse(piece, dctInd + 1))
        else:
          mainLst.append(seedRangeRecurse((dctLst[dctInd][ind][0], piece[1]), dctInd + 1))
      return [el for lst in mainLst for el in lst]
    else:
      return newPieces
  else:
    return([])

for sRange in seedRanges:
  print(seedRangeRecurse(sRange, 0))

# for seed in range(sRange[0], sRange[0] + sRange[1]):
#   num = seed
#   for dct in dctLst:
#     for numRange in dct:
#       diff = num - numRange[0]
#       if 0 <= diff < numRange[2]:
#         num = numRange[1] + diff
#         break
#   locs2.add(num)

print(min(locs))