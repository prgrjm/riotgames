def check(count):
    answer = set()
    for i in count:
        for j in count:
            if i != j:
                answer.add(i + j)
    if len(answer) * 2 == len(count) * (len(count) - 1):
        return True
    else:
        return False

count = [1, 2]

for i in range(100):
    var = 1
    while True:
        if check(count + [count[-1] + var]):
            count.append(count[-1] + var)
            break
        else:
            var += 1
    print(count)

print()
print()
print(count)

# 어떤 식으로 정리해야 하는가 이 관계표를
# 승률분석을 하려면 일단 관계표를 만드는게 좋은거같기는한데
# 으음 이 csv파일로 되나이게? 피클파일이 맞아보이는데
# 하여튼 튜플로 (1,8) 이렇게 딕셔너리를 찾자.

"""

,1,2,3,4
1
2
3
4

이 데이터테이블을 200*200으로 만들면 챔피언 승률 데이터테이블이고
 그걸 다시 10 * 10으로 만들면 그중에 대각선으로 반 자르면 충분하다 이거거든요

"""
