def judge(yy):
    if yy%4==0:
        if yy%100==0:
            if yy%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
            
def date_plus(yy,mm,dd):
    mm_31=[1,3,5,7,8,10,12]
    mm_30=[4,6,9,11]
    if mm in mm_31:
        if dd<31:
            return yy,mm,dd+1
        else:
            if mm!=12:
                return yy,mm+1,1
            else:
                return yy+1,1,1
    if mm in mm_30:
        if dd<30:
            return yy,mm,dd+1
        else:
            if mm!=12:
                return yy,mm+1,1
            else:
                return yy+1,1,1
    if mm==2:
        if dd<28:
            return yy,mm,dd+1
        elif dd==28:
            if judge(yy):
                return yy,mm,dd+1
            else:
                return yy,3,1
        elif dd==29:
            return yy,3,1    

str_=input()
n=int(input())
lst=str_.split("-")
yy=int(lst[0])
mm=int(lst[1])
dd=int(lst[2])
for _ in range(n):
    yy,mm,dd=date_plus(yy,mm,dd)
if mm>=10:
    print(f"{yy}-{mm}-{dd}")
else:
    print(f"{yy}-0{mm}-{dd}")