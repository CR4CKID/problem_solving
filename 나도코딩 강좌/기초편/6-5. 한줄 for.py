#출석번호에 100을 붙힘  
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Black Widow"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자
students = ["Iron man", "Thor", "Black Widow"]
students = [i.upper() for i in students]
print(students)