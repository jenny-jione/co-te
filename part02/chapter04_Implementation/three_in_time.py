"""
[예제4-2] 시각
113쪽
"""

n = int(input())
n = 5
total = n*3600 + 59*60 + 59

h = total//3600
s = total%60
m = (total-h*3600-s)//60

result = 0
for i in range(total):
    h = i//3600
    s = i%60
    m = (i-h*3600-s)//60
    hms = ''.join(map(str, [h,m,s]))
    if '3' in hms:
        result += 1
print(result)

"""
내가 문제를 너무 어렵게 접근했다.. 굳이 전체 초로 바꿔서 그걸 다시 시:분:초 형식으로 변경하지 않아도 되는데..
3중 반복문을 쓰더라도, 전체 경우의 수가 최대 86400이므로 제한 시간 안에 문제를 해결할 수 있다.
"""

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)