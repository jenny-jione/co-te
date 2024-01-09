"""
[실전문제 4] 1이 될 때까지
99쪽
"""

# n, k = map(int, input().split())
n, k = 17, 4
count = 0
while(n!=1):
    if n%k == 0:
        n = n/k
    else:
        n -= 1
    count += 1
print(count)


"""
내 풀이는 단순히 n이 1이 될 때까지 반복문을 도는 건데,
책의 해설을 보니, n<k인 순간부터는 반복문을 돌 필요 없이 n-1을 더해주면 효율성이 증가될 것 같다.
그리고, n이 k의 배수가 되는 순간까지도 마찬가지로 반복문을 돌지 말고 (n//k)*k를 계산해서 result에 더해주는 것이 맞는 것 같다.
예를 들어, n이 1000999이고 k가 1000이라면 999를 미리 빼주면 999만큼의 필요없는 반복을 줄일 수 있다.
"""

result = 0
while True:
    target = (n//k)*k
    result += (n-target)
    n = target

    if n<k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)