totalweight = float(input())
weighto1 = float(input())

if totalweight%weighto1 == 0:
    print("well done")
else:
    print("if the bag weight is right then you need", totalweight%weighto1, "more")