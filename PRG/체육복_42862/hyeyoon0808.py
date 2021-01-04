def solution(n, lost, reserve):
    # 자료형과 연산자를 이용하여 중복된 학생의 번호 제거
    setLost = set(lost)-set(reserve) 
    setReserve = set(reserve)-set(lost) 
    for i in setReserve:
        #양옆번호에 잃어버린 학생이 있다면 왼쪽학생을 우선으로 빌려주는 방법
        if i-1 in setLost:
            setLost.remove(i-1)
        elif i+1 in setLost:
            setLost.remove(i+1)
            
 #전체학생수 - 체육복갯수
    return n-len(setLost)
    