import sys #input() 대신 sys.stdin.readlin() -> 시간적 효율성 높아짐
p = []
flag= False

for i in range(9):
    p.append(int(sys.stdin.readline()))

sum = sum(p) #난쟁이 키 다 더한 sum
    
#이중for문을 통해 난쟁이가 아닌 사람 찾기
for i in range(8):
    for x in range(i+1, 9):
        if(p[i] + p[x] == sum -100):
            # 두명을 합친 값이 전체 값에서 100을 뺀 값일떼
            non_p=[i,x]
            flag = True
            break
    if(flag): #flag가 True일때
        break

del p[non_p[0]]
del p[non_p[1]-1] # 0을 뺐을때 1자리가 0으로

p.sort()
for i in p:
    print(i)