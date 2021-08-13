for tc in range(1):
    N = int(input())
    target = str(input())
    words = str(input())
    result = 0
    for i in range(len(words)-len(target)+1):
        if words[i:i+len(target)] == target:
            result += 1
    print(f'#{N} {result}')