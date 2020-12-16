three = list(map(int, input().split())) #split(): 공백문자를 기준으로 문자나눔, map(): int형으로 받기 위해 쓰임, list(): list 형태로 입력
three.sort() #오름차순으로 list sort! reverse()는 내림차순
print(three[1])
