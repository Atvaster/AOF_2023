import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()

resList = [2**(c-1) if (c:=sum([(num in line.split(": ")[1].split(" | ")[1].split(" ")) for num in line.split(": ")[1].split(" | ")[0].split(" ") if num])) else 0 for line in lineLst]
resList2 = [sum([(num in line.split(": ")[1].split(" | ")[1].split(" ")) for num in line.split(": ")[1].split(" | ")[0].split(" ") if num]) for line in lineLst]
listRes = [1]*len(lineLst)
for ind, item in enumerate(listRes):
  for ind2, check in enumerate(resList2[:ind]):
    if check >= abs(ind - ind2):
      listRes[ind] += listRes[ind2]
print(sum(resList), sum(listRes))