# 에라스토테네스의 체
import math

# 2부터 1000까지의 모든 수에 대해 소수 판별
n = 1000

for i in range(10+1):
    print(i)

# 0부터 1000까지 True로 초기화.
# 나중에 출력할 때 2부터 출력하거나, 혹은 array[0], array[1]에 False를 넣어주면 된다.
array = [True for i in range(n+1)]

# n의 제곱근까지만 확인하면 된다.
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지운다.
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

# 0과 1은 제외하고, 남은 수(소수) 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')