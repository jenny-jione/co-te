"""
[실전문제 3] 게임 개발
118쪽

타임라인
2024.1.10 12:17pm~1:02pm
"""

n, m = map(int, input().split())
r, c, dir = map(int, input().split())
maps = []
maps_status = []
for i in range(n):
    maps.append(map(int, input().split()))
    tmp = []
    for j in maps[-1]:
        if j == 1:
            tmp.append(-1)
        else:
            tmp.append(0)
    maps_status.append(tmp)
"""
0123
nesw
"""
# 입력 예시
# n, m = 4, 4
# r, c, dir = 1, 1, 0
# maps = []
# maps_input = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
# maps_status = []
# for i in range(n):
#     maps.append(maps_input[i])
#     tmp = []
#     for j in maps[-1]:
#         if j == 1:
#             tmp.append(-1)
#         else:
#             tmp.append(0)
#     maps_status.append(tmp)


dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

result = 0
if maps_status[r][c] == 0:
    result += 1
while True:
    # 현재 캐릭터가 바라보고 있는 방향 확인.
    # 그 방향을 기준으로 왼쪽 지점 확인.
    """
    북: 왼쪽지점 -> (행, 열-1)
    동: 왼쪽지점 -> (행-1, 열)
    남: 왼쪽지점 -> (행, 열+1)
    서: 왼쪽지점 -> (행+1, 열)
    """
    flag = False
    for i in range(4):
        nr = r + dr[dir%4]
        nc = c + dc[dir%4]
        if maps_status[nr][nc] == 0:
            dir -= 1
            r = nr
            c = nc
            maps_status[nr][nc] = 1
            result += 1
            flag = True
            break
        dir -= 1
    
    # 4방향 모두 가본 칸이거나 바다일 경우
    if not flag:
        r -= dr[dir%4]
        c -= dc[dir%4]
        if maps_status[r][c] == -1:
            break

print(result)

    





    # nr = r + dr[dir%4]
    # nc = c + dc[dir%4]
    # if maps_status[nr][nc] == 0:
    #     dir -= 1
    #     r = nr
    #     c = nc
    #     maps_status[nr][nc] = 1
    # else:
    #     dir -= 1
