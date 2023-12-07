import sys; lineLst = open(sys.argv[1:][0]).read().splitlines()
handLst = [line.split(" ")[0] for line in lineLst]
bidLst = [line.split(" ")[1] for line in lineLst]
cardLst = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
