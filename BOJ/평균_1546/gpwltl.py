leng = int(input())
points = list(map(int, input().split()))  # map은 Iterator 리턴 -> list 변환
m = max(points)

# map(함수, 리스트)
# map function 사용시에는 lambda 사용할 것 -> map(lambda x:x표현식, 리스트)
for i in range(leng):
    answer = list(map(lambda x: x/m*100, points))

print(sum(answer)/len(answer))
