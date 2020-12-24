line = input()
lineLen = len(line)
x =0
for i in range(lineLen//10 + 1): # // : 몫
    print(line[x : x+10])
    x += 10

