word = input()
for i in range(len(word)):
    # 10의 배수 번째일때 줄바꿈(이때, 0번째는 줄바꿈 필요없음)
    if(i % 10 == 0 and i != 0):
        print()
    print(word[i], end="")  # end="" : 뒤에 출력값에 이어서 출력(줄바꿈x)
    # sep="@" : 영단어를 분리하여 출력(사이에 @가 들어감)
# / :나눗셈, // :몫, % :나머지
