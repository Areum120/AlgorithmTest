'''
1+(-2)+3+(-4)+... 과 같은 식으로 계속 더해나갔을 때,
몇까지 더해야 총합이 100이상이 되는지 구하시오.
'''

# 1. 홀수 1+=2
# 2. 짝수 -2+=-2
# 100이 될 때까지 1.2.를 번갈아 더한다.

answer=0
num = 0
while answer<100:#반복문 계속 돌기
    num+=1#1부터 계속 증가
    if num % 2==0:#짝수이면
        answer-=num#짝수를 계속 뺸다, answer = answer -0, answer = answer -2, answer = answer -4
    else:#홀수이면
        answer+=num#홀수를 계속 더한다, answer = answer + 1, answer = answer +3, answer = answer +5
    #if answer >= 100: #답이 100 이상이면
    #    break#while문 나가기
print(num, "까지 더하면 ", answer, "이 된다")





