import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
sqnLst = [[int(num) for num in line.split(" ")] for line in lineLst]
nextNums = [0 for i in range(len(sqnLst))]
prevNums = [0 for i in range(len(sqnLst))]

for ind, sqn in enumerate(sqnLst):
  diffsLst = [sqn]
  diffs = sqn
  while any(diffs):
    diffs = [diffs[ind + 1] - diffs[ind] for ind in range(len(diffs) - 1)]
    diffsLst.append(diffs)
  num = 0
  for lst in diffsLst:
    num += lst[-1]
  nextNums[ind] = num

for ind, sqn in enumerate(sqnLst):
  diffsLst = [sqn]
  diffs = sqn
  while any(diffs):
    diffs = [diffs[ind + 1] - diffs[ind] for ind in range(len(diffs) - 1)]
    diffsLst.append(diffs)
  num = 0
  for lst in diffsLst[::-1]:
    num = lst[0] - num
  prevNums[ind] = num

print(sum(nextNums), sum(prevNums))