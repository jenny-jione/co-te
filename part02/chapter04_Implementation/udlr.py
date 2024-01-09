"""
[예제4-1] 상하좌우
"""

# n = int(input())
# arr = input().split()
n = 5
arr = "R R R U D D".split()
print(arr)
r, c = 1, 1

row_dir = {'U': -1,
           'D': 1,
           'L': 0,
           'R': 0}

col_dir = {'U': 0,
           'D': 0,
           'L': -1,
           'R': 1}

def in_range(x):
    if 1<=x<=n:
        return True
    else:
        return False

for d in arr:
    if in_range(r+row_dir[d]) and in_range(c+col_dir[d]):
        r += row_dir[d]
        c += col_dir[d]

print(r, c)

"""
굳이 딕셔너리를 사용하지 않아도 됨.
"""
dir = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
