
# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
# 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

def solution(s):
    word_list = list(s)
    cnt = 0
    answer = ''
    for i in range(len(word_list)):
        if word_list[i] == ' ':
            cnt = 0
            answer += ' '
            continue
        if cnt%2 == 0:
            answer += word_list[i].upper()
        else:
            answer += word_list[i].lower()
        cnt += 1
    
    return answer

# 생각하지 못한 사항 : 입력 받는 문자가 모두 소문자라는 법은 없다!!
# 위 사항을 생각하지 못하여 23줄에 .lower()를 추가하지 않아 시간이 많이 끌렸다. 