# [예제 B-1] 소수 구하기
import math

m, n = map(int, input().split())

result = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    while i*j <= n:
        result[i*j] = False
        j += 1

for i in range(m, n+1):
    if result[i]:
        print(i)


"""
<기억해둘 것>
1. 입출력 받기
    m, n = map(int, input().split())
    2개의 숫자를 받아서, 입력받으면 문자열이므로 split한 후 map을 사용해서 int로 변환한다.
2. 에라스토테네스의 체
"""