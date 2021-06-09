"""
제인은 몸매를 유지하기위해 최선의 노력을 다한다.
그녀의 여동생이 이것을 알고 제인에게 장난을 치기로 한다: 제인의 오래된 체중계가 고장난 이후 제인의 여동생은 실제 몸무게가 아니라 몸무게의 제곱을 보여주는 체중계를 제인에게 줬다.

이 사실을 모른채 제인은 몸무게를 얼마간 사용해왔다.
어느 날 아침 그녀는 " apparentGain 만큼 살이 쪘어!"라고 소리지른다.
주어진 apparentGain (제인 현재 몸무게의 제곱과 예전 몸무게의 제곱의 차이)을 이용해서 가장 최근의 측정 이후 가능한 제인의 실제 몸무게를 오름차순으로 정렬한 정수값의 배열을 리턴하시오.

모든 무게(체중계에 표시된 몸무게와 실제 몸무게, 예전 몸무게와 현재 몸무게)는 양의 정수이다.


참고 / 제약 사항
apparentGain은 최소값 1, 최대값 100000의 범위를 가진다.
"""
import math

def solution(apparentGain):
    result_list = []
    x = [i for i in range(1, apparentGain//2+2) if i**2 > apparentGain]

    for i in x:
        if math.sqrt(i**2 - apparentGain) == int(math.sqrt(i**2 - apparentGain)):
            result_list.append(i)

    return result_list


r = solution(233)
print(r)
