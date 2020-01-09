a=int(input('Enter a '))
b=int(input('Enter b '))
c=int(input('Enter c '))

if a<b<c:
    print('y=1')
elif a==b==c:
    print('y=2')
elif b<a<c:
    print('y=3')
else:
    print('y=0')