"""
OneLiner !!
!!파이썬의 최고 장점 다른 언어에서 거의 불가능함
1. oneliner 으로 된 오픈소스가 70% 
2. 아는만큼 보인다
3. 파이썬을 잘하는 사람은 대부분 one line 을 선호한다
"""
employees = {'Alice': 100000,
             'Bob' : 99999,
             'Carol': 122908,
             'SH' : 12112111,
             'Youngho' : 2}

top_earners = []
for key, val in employees.items():
    if val >= 1000000:
        top_earners.append((key, val))
print(top_earners)

top_earners = [(key, val) for key, val in employees.items() if val >= 1000000]

# List comprehension
#lst = [expression context]

lst = [x for x in range(10)]
lst = [x**2 for x in range(10) if x == 5 ]