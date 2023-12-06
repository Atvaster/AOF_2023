import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
times = [int(time) for time in lineLst[0].split(": ")[1].split(" ") if time != ""]
dists = [int(dist) for dist in lineLst[1].split(": ")[1].split(" ") if dist != ""]
races = [(times[i], dists[i]) for i in range(len(times))]
print(races)