"""
[실전문제 2] 왕실의 나이트
115

타임라인
2024.1.10 11:50am~12:04pm
"""

# s = input()
# 입력 예시
s = 'a1'
s = 'c2'
#
col = 'abcdefgh'
c, r = col.index(s[0])+1, int(s[1])

# ddr, ddl, uur, uul, rru, rrd, llu, lld
dr = [2, 2, -2, -2, -1, 1, -1, 1]
dc = [1, -1, 1, -1, 2, 2, -2, -2]

result = 0
for i in range(8):
    nr = r + dr[i]
    nc = c + dc[i]
    if 1<=nr<=8 and 1<=nc<=8:
        result += 1
print(result)


"""
col을 선언해서 index를 구하는 방법 말고, 아래처럼 할 수도 있다.
    c = ord(s[0]) - ord('a') + 1
하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환한다.
ord('a')를 넣으면 정수 97을 반환한다.
"""