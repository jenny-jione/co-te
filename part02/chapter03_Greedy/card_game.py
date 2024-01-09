"""
[3.실전문제] 숫자 카드 게임
96쪽
"""

n, m = map(int, input().split())
result = 0
for i in range(n):
    row = list(map(int, input().split()))
    min_in_row = min(row)
    if result < min_in_row:
        result = min_in_row
print(result)

"""
<기억해둘 것>
비교연산자로 비교해서 result 값을 업데이트할 수도 있지만, max 함수를 사용하면 더 간편해진다.
result = max(result, min_in_row)
"""