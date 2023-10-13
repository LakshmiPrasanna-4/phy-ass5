#Calculate Shopping Bill

chu=500
jea=250
frock=300
saree=800
tops=150
cname=input('Enter the customer name:')
cphno=input('Enter the customer phone number:')
ch=int(input('Enter no of chunidar sets:'))
je=int(input('Enter no of jeans:'))
fro=int(input('Enter no of frocks:'))
sar=int(input('Enter no of sarees:'))
top=int(input('Enter no of tops:'))
pc=input('Enter promo code:')
bill=(chu*ch)+(jea*je)+(frock*fro)+(saree*sar)+(tops*top)
if(pc=='DUSSEHRA' or pc=='dussehra'):
    disc=bill*12/100
elif(bill>=3000):
    disc=bill*15/100
elif(bill>=2000):
    disc=bill*12/100
elif(bill>=1000):
    disc=bill*10/100
elif(bill>=800):
    disc=bill*5/100
elif(bill>=500):
    disc=bill*3/100
else:
    disc=0
tbill=bill-disc
gst=tbill*10/100
obill=tbill+gst
print('Enter customer name:',cname)
print('Enter customer phno:',cphno)
print('Bill:',bill)
print('Discount:',disc)
print('Total bill:',tbill)
print('Gst:',gst)
print('Overall bill:',obill)
print('Thank You! Visit Again')


