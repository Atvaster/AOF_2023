import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
import time; sT = time.time()


def getDist(pos1, pos2):
  pos1X, pos1Y = pos1%mapW, pos1//mapW
  pos2X, pos2Y = pos2%mapW, pos2//mapW
  return abs(pos1X - pos2X) + abs(pos1Y - pos2Y)


def getSkyMap(lineLst, expansion):
  #Adjust to account for already present row
  expansion += -1

  global mapW, mapH
  mapW = len(lineLst[0])
  mapH = len(lineLst)

  #inMap = "".join(lineLst)
  newMap1 = []
  newMapH = 0

  gRows = []
  for y, row in enumerate(lineLst):
    if "#" in row:
      gRows.append(y+expansion*newMapH)
    if row == "."*mapW:
      newMapH += 1
      newMap1.extend([row]*expansion)
    newMap1.append(row)

  newMap1 = "".join(newMap1)
  mapH = mapH + newMapH*expansion

  newMap2 = []
  newMapW = 0

  gCols = []
  for x in range(mapW):
    col = newMap1[x::mapW]
    if "#" in col:
      gCols.append(x+expansion*newMapW)
    if col == "."*mapH:
      newMapW += 1
      newMap2.extend([col]*expansion)
    newMap2.append(col)

  mapW = mapW + newMapW*expansion

  return newMap2, gRows, gCols


def getDistances(skyMap, gRows, gCols):
  galaxies = [y*mapW+x for x in gCols for y in gRows if skyMap[x][y] == "#"]
  distances = []
  for g1 in range(len(galaxies)):
    for g2 in range(len(galaxies)):
      if g1 < g2:
        distances.append(getDist(galaxies[g1], galaxies[g2]))
  return distances

#Part 1
distances1 = getDistances(*getSkyMap(lineLst, 2))
#Part 2
distances2 = getDistances(*getSkyMap(lineLst, 1000000))
print(f"Part 1: {sum(distances1)}, Part 2: {sum(distances2)}")

print(f"Computation time: {time.time()-sT:.6}s")