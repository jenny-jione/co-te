# 정렬되어 있는 두 리스트의 합집합

# 사전에 정렬된 리스트 A와 B 선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0] * (n+m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 A의 원소가 B보다 작거나, 리스트 B의 모든 원소가 처리되었을 때
    if (i<n and a[i] <= b[j]) or j>=m:
        result[k] = a[i]
        i += 1
    # 리스트 B의 원소가 A보다 작거나, 리스트 A의 모든 원소가 처리되었을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end=' ')