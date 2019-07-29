print("green")
print("he"* 5)
print(5*45)
name="jackfrued"
fruits=["apple","orange","grape"]
owners={'1001':"呵呵",'1002':"哈哈"}
if name and fruits and owners:
    print('A')
a=123
b=321
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
a=int(input('a = '))
b=int(input('b = '))
print('%d + %d = %d'%(a,b,a + b))
print('%d + %d = %d'%(a,b,a - b))
print('%d + %d = %d'%(a,b,a * b))
print('%d + %d = %d'%(a,b,a / b))
print('%d + %d = %d'%(a,b,a // b))
print('%d + %d = %d'%(a,b,a % b))
print('%d + %d = %d'%(a,b,a ** b))
f=float(input('120:'))
c=(f-32)/1.8
print('%.1f华氏度=%.1f摄氏度'%(f,c))
import math
radius=float(input('50: '))
perimeter=2 * math.pi * radius
area= math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
year= int(input('2017: '))
is_leap=(year % 4==0 and year % 100 !=0 or year % 400 == 0)
print(is_leap)

