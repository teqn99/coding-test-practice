N = int(input())
times = []
result = []
for i in range(N):
    time = list(map(int, input().split()))
    times.append(time)
# times = sorted(times, key=lambda x: (x[0], x[1]))
times = sorted(times, key=lambda x: (x[1], x[0]))
print(times)

# small, big = times[0][0], times[0][1]
# result.append([small, big])
# for i in range(1, N):
#     if times[i][0] == small:
#         if times[i][1] < big:
#             big = times[i][1]
#             del result[-1]
#             result.append(times[i])
#         elif times[i][1] == big:
#             small = times[i][0]
#             big = times[i][1]
#             result.append(times[i])
#     elif times[i][0] > small:
#         if times[i][1] < big:
#             small = times[i][0]
#             big = times[i][1]
#             del result[-1]
#             result.append(times[i])
#         elif times[i][1] >= big:
#             if times[i][0] >= big:
#                 small = times[i][0]
#                 big = times[i][1]
#                 result.append(times[i])

cnt = 1 
end_time = times[0][1] 
for i in range(1, N): 
    if times[i][0] >= end_time: 
        cnt += 1 
        end_time = times[i][1]

print(cnt)
# print(result)
# print(len(result))

#####################################################
# 여기가 정리된 옳은 풀이
N = int(input())
times = []
for i in range(N):
    time = list(map(int, input().split()))
    times.append(time)
times = sorted(times, key=lambda x: (x[1], x[0]))

result = 1 
end = times[0][1] 
for i in range(1, N): 
    if times[i][0] >= end: 
        result += 1 
        end = times[i][1]

print(result)