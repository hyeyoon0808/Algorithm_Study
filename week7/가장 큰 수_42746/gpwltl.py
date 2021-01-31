# numbers=[6,10,2]
numbers=[0,0,0]
# numbers=[1000, 0, 5, 99, 100]

def solution(numbers):
    answer = ''
    if sum(numbers)==0:
        answer='0'      #0도 string으로 주어야 정답처리
    else: 
        num=list(map(str, numbers))
        num.sort(key=lambda x:x*3, reverse=True)
        answer=''.join(num)

    return answer

print(solution(numbers))