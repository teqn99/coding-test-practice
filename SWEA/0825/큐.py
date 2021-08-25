# 1MB 이상 길이의 인풋이 들어오는 경우 이 방법을 사용해야 함.
# 제출 시에는 없애야 함.
# import sys
# sys.stdin = open('input.txt', 'r')

# 순환 큐 구현
def enq(data):
    global qsize
    global rear
    global front

    if (rear+1) % qsize == front:
        # print('full')
        front = (front + 1) % qsize

    rear = (rear + 1) % qsize
    q[rear] = data


front = 0
rear = 0
qsize = 4
q = [0]*qsize  # front자리가 존재하기 때문에, 총 3칸을 갖는 큐

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
while front != rear:
    front = (front + 1) % qsize
    print(q[front])
