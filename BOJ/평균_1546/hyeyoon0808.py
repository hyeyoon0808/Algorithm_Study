num = int(input()) # 과목 수

scoreList = list(map(int, input().split()))
maxScore = max(scoreList)

newScoreList = []
for score in scoreList :
    newScoreList.append(score/maxScore *100) # 새로운 점수 리스트 생성
avg = sum(newScoreList)/num # 리스트 합
print(avg)

