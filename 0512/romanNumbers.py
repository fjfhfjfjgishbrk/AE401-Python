while True:
    try:
        n = [int(i) for i in input().split(" ")]
        haveNum = False
        for i in range(n[0], n[1] + 1):
            sum = 0
            for j in str(i):
                sum += int(j) ** len(str(i))
            if sum == i:
                print(i, end=", ")
                haveNum = True
        if not haveNum:
            print("none")
        else:
            print()
    except:
        break