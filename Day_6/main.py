import numpy as np
import math
import decimal
import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
import time; sT = time.time()
sys.set_int_max_str_digits(50000)
decimal.getcontext().prec = 7000
times = [int(time) for time in lineLst[0].split(": ")[1].split(" ") if time != ""]
dists = [int(dist) for dist in lineLst[1].split(": ")[1].split(" ") if dist != ""]
# races = [(times[i], dists[i]) for i in range(len(times))]

# amnts = []
# for race in races:
#   cumDist = []
#   for time in range(1, race[0] + 1):
#     cumDist.append(time*(race[0]-time))
#   amnt = sum([dist > race[1] for dist in cumDist])
#   amnts.append(amnt)
# print(np.prod(amnts))

bigTime = decimal.Decimal(int("".join([str(time) for time in times])))
bigDist = decimal.Decimal(int("".join([str(dist) for dist in dists])))

print(int(((bigTime + (bigTime**decimal.Decimal(2) - decimal.Decimal(4)*bigDist)**((decimal.Decimal(0.5)))/decimal.Decimal(2) - (bigTime - (bigTime**2 - decimal.Decimal(4)*bigDist)**(decimal.Decimal(0.5)))/decimal.Decimal(2))//decimal.Decimal(1))))
print(f"Computation time: {time.time()-sT}s")