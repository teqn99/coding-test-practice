n = int(input())
times = []
for i in range(n):
    times.append(list(map(int, input().split())))

prev_time = sorted(times, key= lambda x: x[0])
next_time = sorted(times, key= lambda x: x[1])

if prev_time[-1][0] <= next_time[0][1]:
    print(0)  # 이 경우에는 팬들이 모두 같이 학교에 있기 때문에 학교에 남아있을 시간이 필요없다.
else:
    print(prev_time[-1][0] - next_time[0][1])  # 이런 경우에는 늦게 등교하는 팬과 일찍 하교하는 팬의 시간만큼 학교에 남아서 기다려야 한다.