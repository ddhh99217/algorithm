T = int(input())

for x in range(T):
    open_close = input() #T번 괄호들 받기
    score = 0 #score 초기화 해줘야 또 YES, NO를 판별

    for i in open_close:
        if i == '(':
            score += 1
        elif i == ')':
            score -= 1
            if score < 0: # )( 같은 상황도 NO 이기 때문
                break

    if score == 0:
        print("YES")
    else:
        print("NO")