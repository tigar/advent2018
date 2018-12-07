with open("day1input.txt", "r") as f:
    lines = f.readlines()
res = 0
check = set()
yes = True
while yes:
    for line in lines:
        line.replace("\n", "")
        line.replace("+", "")
        res += int(line)
        if res in check:
            print("this is: " + str(res))
            exit(0)
        check.add(res)