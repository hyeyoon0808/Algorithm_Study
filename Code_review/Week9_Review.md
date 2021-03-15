# :pencil: Week9 코드 리뷰

### :round_pushpin: 빵집_3109

input()을 받거나 출력할 때, 처음이나 마지막에 공백이 있을경우

- input().strip()과 같이 stript()을 써줄 시 양쪽 공백 제거

- rstrip(): 인자로 전달된 문자를 string의 오른쪽에서 제거함

- lstrip():  인자로 전달된 문자를 string의 왼쪽에서 제거함

### :round_pushpin: 정수삼각형_43105

eval()

: eval 함수는 한줄로 정리하자면
매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수

Ex) [x, y, z]를 input()으로 입력 받을 시, "[x, y, z]"와 같이 문자열이 되는데 eval(input())을 사용하게 되면 자동으로 배열로 됨.