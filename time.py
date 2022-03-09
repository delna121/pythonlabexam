class Time:
    def __init__(self,h,m,s):
        self._h1 = h
        self._m1 = m
        self._s1 = s
    def __add__(self, x):
        sum1 = self._h1 + x._h1
        sum2 = self._m1 + x._m1
        sum3 = self._s1 + x._s1
        if(sum3 >= 60):
            sum3 = sum3 - 60
            sum2 = sum2 + 1
        if(sum2 >= 60):
            sum2 = sum2 - 60
            sum1 = sum1 + 1
        print(sum1,":",sum2,":",sum3)
print("TIME 1")
h = int(input("enter the houre of time 1:"))
m = int(input("enter the minitue of time 1:"))
s = int(input("enter the second of time 1:"))
obj1 = Time(h, m, s)
print("TIME 2")
h = int(input("enter the houre of time 2:"))
m = int(input("enter the minitue of time 2:"))
s = int(input("enter the second of time 2:"))
obj2 = Time(h, m, s)
print("sum of time is :")
obj1 + obj2

