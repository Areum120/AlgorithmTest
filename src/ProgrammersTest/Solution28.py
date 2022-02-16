'''
소수 찾기
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

'''


# 소수란, 1과 자기 자신만을 약수로 갖는다. 자신보다 작은 두개의 자연수를 곱하여 만들 수 없는 자연수(1보다 큼)

# 방법 3
from math import sqrt

# 제곱근
# num_sqrt = int(sqrt(50))
# print(num_sqrt)

# 나누어 떨어지면 지우기
# def sieve(N):
#   ns = list(range(2, N+1)) # 2부터 50까지 정수 생성
#   for i in range(2, int(sqrt(N)) + 1): # 루트 N 이하의 자연수
#     for j in range(len(ns)-1, 1, -1): # 2부터 50 49개이지만 인덱스 49는 index error 발생하므로 0~48개까지 생성, 49부터 2,3을 제외한 4까지(2번째 인덱스) 뒤에 있는 큰수부터 작은수까지이므로 -1
#       if ns[j] % i == 0 and ns[j] > i : # 맨 뒤에있는 숫자부터 2,3,4,5,6...숫자로 나누어 떨어지면 합성수, 5, 7등 자기 자신은 지우면 안 되기 때문에 ns[j] 인덱스 숫자는 > 5 , >7보다 큰 숫자인 조건 추가
#         ns.pop(j) # 뒤에서부터 하나씩 꺼내어 제거한다
#   print(f'{i}의 배수제거:', '제거한 갯수:', len(ns), '지우고 난 결과:', ns)
#   return ns
#
# sieve(100)

# 위 로직은 직관적이지면 N이 커지면 속도 저하 문제가 있음
# 소수도 매번 연산의 대상이 되는 문제가 됨 ex 2의 배수는 지워졌는지 4의 배수 8의 배수도 계속 지우는 등의 불필요한 연산이 진행됨

# 속도 개선
# for문은 몇 번 실행될 지를 미리 정해놓고 작업을 반복하기 때문에 중간에 불필요한 연산이 있어도 건너띄거나 중단할 수 없음
# while은 조건이 True인 경우에만 작동을 하므로 숫자 범위가 아닌 식을 써서 넣을 수 있음

# 남아 있는 소수만 연산
def sieve(N):
  ns = list(range(2, N+1))
  i = 0
  while ns[i] * ns[i] <= N:#제곱근에서 반대로 역으로 곱하기, 2의 배수, 3의 배수들이 지워지고 4는 2의 배수를 지울 때 지웠으므로 그다음 5의 배수인 소수들이 모두 지워짐
    for j in range(len(ns)-1, 1, -1):
      if ns[j] % ns[i] == 0 and ns[j] > ns[i]:
        ns.pop(j)
    print(i, ns[i], len(ns), ns)
    i += 1
  return ns

print(sieve(50))

# 연산 횟수를 줄이긴 했지만 ns에서 숫자를 제거할 때 -1이 적용된 ns 길이로 배열을 생성하고 값을 복사하는 식으로 연산이 계속됨

# check 배열 만들기
# True가 들어 있는 배열에 지우려고 하는 2의 배수가 들어 있는 자리를 False로 바꾸는 연산 하기(pop() 기능 대체)
# True 배열은 ns의 크기와 같은 크기로 만들어주기
'''
N = 50
ns = list(range(2, N+1))
check = [True] * len(ns)

print(len(ns))
print(len(check))
print(check)
'''
'''
N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
  if check[i]: #check[i]가 True라면
    print(i, ns[i], check[i]) #print함
  i += 1
'''

'''
ns[i]의 배수를 False로 표시하기
장점 : 배수마다 False를 해주기 때문에 나머지를 구하는 계산을 할 필요가 없고, if조건을 태울 필요가 없어
알고리즘의 효율이 높아짐
2의 배수 4부터 False 체크를 해주기
'''

'''
N = 50
ns = list(range(2, N + 1))
check = [True] * len(ns)

i = 0
while ns[i] * ns[i] <= N:
  if check[i]: #check[i]가 True라면
    for j in range(2, len(ns), 2):
      check[j] = False #배수면 False로 바꿈
      print(i, ns[i], check[i]) #print함
  i += 1
'''

# 그렇다면 3, 5, 7의 배수를 False로 바꾸려면?
# for j in range(ns[i]*2, len(ns), ns[i]) #2일 때는 4부터, 3일 때는 6부터 4일 때는 8부터 False로 바꿔야하므로 2배수를 해줌

'''
반복문 시작 숫자를 식(statement)으로 
ns[i] + i 으로 하면 2, 4, 6, 8 이런 식으로 바뀜
2+0
3+1
4+2
5+3
...

5의 배수를 False로 바꾸려면 5는 10부터 표시, 인덱스 8이 10이므로
ns[i] + i = 8 위치로 설정하면 됨
'''

def sieve(N):
  ns = list(range(2, N + 1))
  check = [True] * len(ns)

  i = 0
  while ns[i] * ns[i] <= N:
    if check[i]: #check[i]가 True라면
      for j in range(ns[i]+i, len(ns), ns[i]):
        check[j] = False #배수면 False로 바꿈
        # print(ns[i], ns[j]) #print함
    i += 1

  # check에서 True인 값을 ns에서 뽑아 새로운 리스트로 만드는 작업

  primes = []
  for i in range(len(ns)):
    if check[i]:
      primes.append(ns[i])
  # print(len(primes), primes)
  return primes

print(sieve(50))

#속도 테스트

from datetime import datetime

start_time = datetime.now()
N = 300000
res = sieve(N)
end_time = datetime.now()
print(len(res), max(res))
print(end_time - start_time)

# while문 중복 처리 할 때처럼 중복으로 false 처리 건너띄기 위해
# if check[j] :
#   check[j] = False
# 위 로직 처리를 하면 1초 정도 속도가 좀 더 느려짐



# 방법 2 사용해도 정답x -> 123의 숫자를 넣으면 2,3,5,7,11의 소수의 배수를 지워줘야 함
# 2,3,5,7,11,13....소수의 배수를 계속 지워줘야 하는 건 알았지만 루트에 int를 씌워서 공식을 세우는 것까지는 계산 못함
# 앞에서부터 숫자를 지우면 인덱스가 바뀌면서 연산을 건너띄는 경우도 생김->뒤에서부터 지워야함
# 또 n에서 숫자 하나를 지우는 계산을 하면 n-1개의 배열을 만든 다음에 숫자를 지운 나머지 숫자를 채워놓음 즉, n이 클수록 연산속도가 현저히 떨어짐
# def solution(n):
#   num = [x for x in range(2, n+1)]
#   for i in range(1, n+1):
#     if i!= 2 and i!= 3 and i!=5 and i!=7:#2,3,5,7은 살린다
#       if i%2==0 or i%3==0 or i%5==0 or i%7==0: #에라토스테네스의 체 2,3,5,7의 배수를 모두 지운다
#         num.remove(i)
#   print(num)
#   print(len(num))
#   return len(num)


  # 약수의 갯수 구하기
  # 약수의 갯수가 2개인 것만 소수임

        # 방법 1: 속도 느림, 효율성 떨어짐
        # 약수의 갯수
        # for i in range(1, n+1):
        #         num = []
        #         for j in range(1, n+1):
        #         # print(i) #55555, 44444, 33333, 22222, 11111,
        #         # print(j) #12345, 12345, 12345, 12345, 12345
        #          if i % j == 0: #5%1, 5%2, 5%3, 5%4, 5%5, 4%1, 4%2, 4%3, 4%4, 4%5
        #             num.append(j)#5의 약수, 4의 약수, 3의 약수, 2의 약수, 1의 약수
        #             print(num)
        #     if len(num)==2:#5의 약수 갯수, 4의 약수 갯수, 3의 약수 갯수, 2의 약수 갯수, 1의 약수 갯수가 2개일 때
        #         prime_num.append(i)#소수리스트에 넣기
        # print(prime_num)
        # return len(prime_num)#소수리스트 갯수 반환
# solution(1010)
