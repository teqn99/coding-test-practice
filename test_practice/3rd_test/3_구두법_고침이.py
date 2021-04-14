"""
가끔 몇몇 작가들은 강조를 하기 위해서 과도하게 느낌표를 남발한다.
느낌표와 물음표를 섞어서 놀라움을 표시하는 경우도 있다.
예를 들자면 "정말 그렇게 생각해요??!!".
출판을 하려면 이런 식의 과도한 느낌표와 물음표의 남발을 고쳐야 된다.
만약 느낌표가 연속으로 여러 개가 사용 되었다면 한 개의 느낌표로 바꾸고, 느낌표와 물음표가 섞여있다면 하나의 물음표로 바꿔야 한다.
이렇게 고쳐진 문자열을 리턴하시오.

참고 / 제약 사항
Document의 길이는 1이상 50이하다.
Document는 알파벳, 공백, 물음표, 느낌표로만 이루어져있다.
"""

class Solution:
    def solution(self, document):
        document = list(document)
        for idx, val in enumerate(document):
            if val == '!':
                if (idx + 1) < len(document):  # 뒤의 것과 비교하기 때문에 len보다 클 수 없다.
                    if document[idx + 1] == '!' or document[idx + 1] == '?':
                        document[idx] = ''  # 뒤의 글자가 !나 ?면 앞의 글자를 ''로 바꿔준다.
            elif val == '?':
                if (idx + 1) < len(document):  # 뒤의 것과 비교하기 때문에 len보다 클 수 없다.
                    if document[idx + 1] == '!' or document[idx + 1] == '?':
                        document[idx] = ''  # 뒤의 글자가 !나 ?면 앞의 글자를 ''로 바꿔준다.
                        document[idx + 1] = '?'  # 이 경우는 !도 ?로 바꿔줘야하기 때문
        return ''.join(document)



def solution(document):
    document = list(document)
    for idx, val in enumerate(document):
        if val == '!':
            if (idx + 1) < len(document):
                if document[idx+1] == '!' or document[idx+1] == '?':
                    document[idx] = ''
        elif val == '?':
            if (idx + 1) < len(document):
                if document[idx+1] == '!' or document[idx+1] == '?':
                    document[idx] = ''
                    document[idx+1] = '?'
    return ''.join(document)

s = solution( "a??a ?!a a!?b b!?!C C?!!D D?!?EE ??? FF!!! !???!")
print(s)