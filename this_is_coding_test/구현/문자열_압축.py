# def solution(s):
#     length = []
#     result = ""
#
#     if len(s) == 1:
#         return 1
#
#     for cut in range(1, len(s) // 2 + 1):
#         count = 1
#         tempStr = s[:cut]
#         for i in range(cut, len(s), cut):
#             if s[i:i + cut] == tempStr:
#                 count += 1
#             else:
#                 if count == 1:
#                     count = ""
#                 result += str(count) + tempStr
#                 tempStr = s[i:i + cut]
#                 count = 1
#
#         if count == 1:
#             count = ""
#         result += str(count) + tempStr
#         length.append(len(result))
#         result = ""
#
#     return min(length)

# a = solution('aabbaccc')
# print(a)

#----------------------------------------------------------------------------------

def solution(s):
    answer = len(s)
    unit = 1
    while unit <= len(s)//2:
        comp = s[:unit]
        word = ""
        count = 1
        for i in range(unit, len(s), unit):
            if comp == s[i:i+unit]:
                count += 1
            else:
                if count == 1:
                    word += comp
                else:
                    word += str(count) + comp

                comp = s[i:i+unit]
                count = 1

        if count == 1:
            word += comp
        else:
            word += str(count) + comp

        unit += 1
        #print(word)
        if len(word) < answer:
            answer = len(word)

    return answer

s = solution('aabbaccc')
print(s)