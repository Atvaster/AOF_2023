import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
import math
mapW = len(lineLst[0])
mapH = len(lineLst)
global pipeMap, startType
pipeMap = "".join(lineLst)
start = pipeMap.find("S")
startType = 0

def neighbors(node):
  curChar = pipeMap[node]
  if curChar == ".": return set()
  adjs = []
  nodeX = node%mapW
  nodeY = node//mapW
  adjs.append(node - 1 if nodeX > 0 else -1)
  adjs.append(node + 1 if nodeX < mapW - 1 else -1)
  adjs.append(node - mapW if nodeY > 0 else -1)
  adjs.append(node + mapW if nodeY < mapH - 1 else -1)

  if curChar == "|" and 0 < nodeY < mapH - 1:
    return (adjs[2], adjs[3])
  if curChar == "-" and 0 < nodeX < mapW - 1:
    return (adjs[0], adjs[1])
  if curChar == "J" and nodeX > 0 and nodeY > 0:
    return (adjs[0], adjs[2])
  if curChar == "L" and nodeX < mapW - 1 and nodeY > 0:
    return (adjs[1], adjs[2])
  if curChar == "7" and nodeX > 0 and nodeY < mapH - 1:
    return (adjs[0], adjs[3])
  if curChar == "F" and nodeX < mapW - 1 and nodeY < mapH - 1:
    return (adjs[1], adjs[3])
  if curChar == "S":
    return [pos for pos in adjs if node in neighbors(pos)]
  return set()


def BFS(root, goal):
  counter = 0
  toParse = [root]
  if root == goal:
    return toParse
  parsed = {root: root}
  while counter < len(toParse):
    node = toParse[counter]
    nbrs = neighbors(node)
    if pipeMap[node] == "S":
      global startType
      startType = not(any((node-pos) < 0 for pos in nbrs))
    for nbr in nbrs:
      if nbr and nbr not in parsed:
        parsed[nbr] = node
        toParse.append(nbr)
        if nbr == goal:
          return parsed
    counter += 1
  return parsed


def getInner():
  vertChars = {"|", "L", "J", "J"}
  if startType:
    vertChars.add("S")
  positions = set()
  for pos in range(len(pipeMap)):
    posX = pos%mapW
    posY = pos//mapW
    if pos not in mainLoop:
        if len([char for ind, char in enumerate(pipeMap[posY*mapW+posX:posY*mapW+mapW]) if char in vertChars and ind+pos in mainLoop])%2 == 1:
          positions.add(pos)
  return positions

global mainLoop
mainLoop = {*BFS(start, "")}
print(f"Part 1: {len(mainLoop)//2}, Part 2: {len(getInner())}")
