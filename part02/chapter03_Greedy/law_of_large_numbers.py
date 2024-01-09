"""
[2.실전문제] 큰 수의 법칙
92쪽
"""

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

#
# n, m, k = 5, 8, 3
# array = list(map(int, "2 4 5 4 6".split()))

# n, m, k = 5, 7, 2
# array = list(map(int, "3 4 3 4 3".split()))
#
array.sort()

first = array[-1]
second = array[-2]

result = 0

subsum = first*k + second
result = subsum*(m//(k+1)) + first*(m%(k+1))
print(result)


"""
<내 코드 설명>
부분합: (6+6+6+5)라고 정의.
m=8이면 (6+6+6+5)+(6+6+6+5)
m=7이면 (6+6+6+5)+(6+6+6)
즉 전체 합은 부분합을 x번 곱한 후에 m%(k+1) (=전체를 부분합 길이로 나눈 나머지)만큼 가장 큰 수를 더하는 것이다.
부분합 = 가장 큰 수 * k + 두번째로 큰 수
"""