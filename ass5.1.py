#To print Leap year or not a leap year
n=int(input('Enter a year'))
if(n%4==0 and n%100!=0):
    print('Given year is a Leap year')
elif(n%400==0):
    print('Given year is a Leap year')
else:
    print('Given year is not a Leap year')


