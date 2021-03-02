def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else: 
                triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])

    answer=max(triangle[-1])
    return answer
    

# def solution(triangle):
#     answer = 0
#     answerList=[]
    
#     for i in range(2):
#         add=triangle[0][0]
#         add+=triangle[1][i]

#         for j in range(2, len(triangle)):
#             if triangle[j][i] > triangle[j][i+1]:
#                 add+=triangle[j][i]
                
#             else: 
#                 add+=triangle[j][i+1]
#                 i=i+1

#         answerList.append(add)
    
#     answer=max(answerList)
#     return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))