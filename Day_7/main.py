import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
handLst = {line.split(" ")[0]:int(line.split(" ")[1]) for line in lineLst}
cardLst = [['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1], ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]]

def cardVal(card, num):
  res = "0x"
  for char in card:
    res += hex(cardLst[num - 1].index(char))[2:]
  return int(res, 16)


typeLst = [[],[],[],[],[],[],[]]
for hand in handLst:
  handSet = {*hand}
  counts = sorted([hand.count(char) for char in handSet])
  if len(handSet) == len(hand):
    typeLst[0].append(hand)
  elif counts[-2:] == [1, 2]:
    typeLst[1].append(hand)
  elif counts[-2:] == [2, 2]:
    typeLst[2].append(hand)
  elif counts[-2:] == [1, 3]:
    typeLst[3].append(hand)
  elif counts[-2:] == [2, 3]:
    typeLst[4].append(hand)
  elif counts[-2:] == [1, 4]:
    typeLst[5].append(hand)
  elif len(handSet) == 1:
    typeLst[6].append(hand)

for cType in typeLst:
  cType.sort(key = lambda x:cardVal(x, 1))
#print(typeLst)
masterLst = [el for type in typeLst for el in type]
sumLst = [handLst[hand]*(ind+1) for ind, hand in enumerate(masterLst)]

typeLst2 = [[],[],[],[],[],[],[]]
for hand in handLst:
  jCount = hand.count("J")
  if jCount != 5:
    handSet = {*hand} - {"J"}
    counts = sorted([hand.count(char) for char in handSet])
    counts[-1] += jCount
  else:
    handSet = {*hand}
    counts = [5]
  if len(handSet) == len(hand):
    typeLst2[0].append(hand)
  elif counts[-2:] == [1, 2]:
    typeLst2[1].append(hand)
  elif counts[-2:] == [2, 2]:
    typeLst2[2].append(hand)
  elif counts[-2:] == [1, 3]:
    typeLst2[3].append(hand)
  elif counts[-2:] == [2, 3]:
    typeLst2[4].append(hand)
  elif counts[-2:] == [1, 4]:
    typeLst2[5].append(hand)
  elif len(handSet) == 1:
    typeLst2[6].append(hand)

for cType in typeLst2:
  cType.sort(key = lambda x:cardVal(x, 2))

masterLst2 = [el for type in typeLst2 for el in type]
sumLst2 = [handLst[hand]*(ind+1) for ind, hand in enumerate(masterLst2)]

print(sum(sumLst), sum(sumLst2))