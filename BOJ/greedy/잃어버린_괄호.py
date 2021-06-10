input_word = str(input())
word_list = input_word.split('-')

for i in range(len(word_list)):
    cnt = word_list[i].split('+')
    if word_list[i] == cnt:
        word_list[i] = int(word_list[i])
    else:
        for j in range(len(cnt)):
            cnt[j] = int(cnt[j])
        word_list[i] = sum(cnt)

result = word_list[0]
for i in range(1, len(word_list)):
    result -= word_list[i]

print(result) 