month, life = 17, 5
answer = [0] * (month + 1)
dying = [0] * (month + life + 1)


def mortal_rab(month):
    if month <= 2:
        dying[life + 1] = 1
        answer[month] = 1
    if answer[month] == 0:
        answer[month] = mortal_rab(month - 1) + mortal_rab(month - 2) - dying[month]
        dying[month + life - 1] = mortal_rab(month - 2)
    return answer[month]


mortal_rab(month)
print(answer)
