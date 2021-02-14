def solution(record):
    answer = []
    id_nic={}

   
    # uid / 닉네임 딕셔너리 생성
    for i in range(len(record)):
        temp=record[i].split(" ")
        if temp[0]!="Leave":
            id_nic[temp[1]]=temp[2]
            
    # 결과값 출력
    for i in range(len(record)):
        temp=record[i].split(" ")
        if temp[0]=="Enter":
            answer.append(id_nic[temp[1]]+"님이 "+"들어왔습니다.")
        elif temp[0]=="Leave":
            answer.append(id_nic[temp[1]]+"님이 "+"나갔습니다.")
            
    return answer