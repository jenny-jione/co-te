"""
예제 B-2 암호 만들기
문제링크: https://www.acmicpc.net/problem/1759
"""

"""
최소 1개의 모음, 2개의 자음으로 이루어짐
알파벳순
L, C 주어짐.
l: 암호 길이
c: 주어진 알파벳 개수
구: 가능성 있는 알파벳 암호를 모두 구한다.

타임라인
24.1.8 2:03pm~2:22pm
"""

import itertools
l, c = map(int, input().split())
alpha = input().split()

# l, c = 4, 6
# alpha = ['a', 't', 'c', 'i', 's', 'w']
alpha.sort()

vowel = 'aeiou'
for x in itertools.combinations(alpha, l):
    mo, ja = 0, 0
    code = ''.join(list(x))
    for ch in code:
        if ch in vowel:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        print(code)

"""
<기억해둘 것>
1. 조합 알고리즘. itertools.combination(리스트, 뽑을 개수)
2. 리스트를 문자열로 붙이기
    ''.join(리스트)
3. 나는 자음 개수도 변수를 선언했지만, ja 대신 l-mo로 하면 변수 선언을 하나 아낄 수 있다.
"""