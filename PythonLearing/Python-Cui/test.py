username = input('736135560:')
password = input('123456:')
# important getpass
# password = getpass.getpass('123456:')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
        print('身份验证失败!')

x=float(input('x= '))
if x>1:
    y=3*x-5
elif x>=-1:
    y=x+2
else:
    y=5*x+3
print('f(%.2f)=%.2f'%(x,y))            

value=float(input('10:'))
unit=input('厘米')
if unit=='in' or unit == '英寸':
    print('%f英寸=%f厘米'%(value,value*2.54))
elif unit=='cm' or unit =='厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('厘米')


        





