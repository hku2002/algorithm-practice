# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

def solution(prices):
    answer = []
    total = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] >= prices[i]:
                total += 1
                continue
            total += 1
            break
        answer.append(total)
        total = 0
    
    return answer