N = int(input())
word = []
for _ in range(N):
    word.append(list(input()))

dic = {}
#문자의 자릿수에 따라 10의 n승 더해주기
#ex. G:100, C:10, F:1
for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] not in dic:
            dic[word[i][j]] = pow(10, len(word[i])-j-1)
        else:
            dic[word[i][j]] += pow(10, len(word[i])-j-1)

#value의 값을 기준으로 정렬
sort_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
result, num = 0, 9
#정렬된 값이 앞에 있을수록 자릿수가 크다는 거니까 9부터 곱해주면서 결과에 더해주기
for i in range(len(sort_list)):
    result += num * sort_list[i][1]
    num -= 1

print(result)