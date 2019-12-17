import time

def GPA_calculate():
    t_credits=0
    grade_points=0
    num_courses=1
    while True:
        grade=input("输入第"+str(num_courses)+"门课的百分制成绩，输入q以退出\n")
        if (grade=='q'):
            break
        credit=input("输入这门课的学分\n")
        
        grade=int(grade)
        credit=float(credit)
        grade_point=4-3*(100-grade)*(100-grade)/1600
        grade_points += credit*grade_point
        t_credits += credit
        num_courses += 1
    
    GPA = grade_points / t_credits
    print("课程门数："+str(num_courses))
    print("学分数："+str(t_credits))
    print("GPA："+str(GPA))
    time.sleep(10)
    
GPA_calculate()