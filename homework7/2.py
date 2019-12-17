import re

a=input()
staff="[0-9]{5}"
ug="[0-9]{8}"
dr="BY[0-9]{7}"
sm="ZY[0-9]{7}"
am="SY[0-9]{7}"

if (re.fullmatch(staff,a)):
    print("staff")
elif (re.fullmatch(ug,a)):
    print("undergraduate")
elif (re.fullmatch(dr,a)):
    print("doctor")
elif (re.fullmatch(sm,a)):
    print("specialized master")
elif (re.fullmatch(am,a)):
    print("academic master")
else:
    print("illegal number")