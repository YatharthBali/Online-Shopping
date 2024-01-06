import random
import csv
import os
oo=open('Online Shoping.csv','a')
hmm=csv.writer(oo,delimiter=',')
print('WELCOME TO YATHARTH ONLINE SHOPING')
print('|-Login with GOOGLE(1)    |-LOGIN WITH FACEBOOK(2)')
a=input('Login Through')
if a=='1':
    b=input('Please Enter your Email Id')
    c=input('Please Enter your Password')
    d=input('Please Enter your Name')
    print('Welcome Mr.',d)
    print('''Please Select your Option Below
|-JEANS(3)
|-SHIRT(4)
|-SHOES(5)''')
    e=input('What you like to buy')
    if e=='3':
        print('LEVIS(6),DENIM(7),SPYKAR(8)')
        f=input('Please Select Brand')
        if f=='6':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 5000')
            print('your total cost is=',i*5000)
            j=i*5000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                bye=random.randint(123456,789999345)
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
        elif f=='7':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 6000')
            print('your total cost is=',i*6000)
            j=i*6000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
        elif f=='8':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 4000')
            print('your total cost is=',i*4000)
            j=i*4000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
    elif e=='4':
        print('|-Peter England(11)  |-Louis Phillippe(12)')
        u=input('Please Select your brand')
        if u=='11':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            v=input('Please Select your size')
            x=input('Colour')
            y=int(input('how many?'))
            print('Price of ine shirt is 4500')
            print('your total cost is=',y*4500)
            z=y*4500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',z)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',z-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',z)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p])
                oo.close()
        elif u=='12':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            v=input('Please Select your size')
            x=input('Colour')
            y=int(input('how many?'))
            print('Price of ine shirt is 6500')
            print('your total cost is=',y*6500)
            z=y*6500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',z)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',z-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',z)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
    elif e=='5':
        print('|-Nike(13) |-Reebok(14)')
        gg=input('Please Select Brand')
        if gg=='13':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red,Yellow
Size= 6,7,8,9,10,11''')
            hh=input('Colour')
            ii=input('Size')
            print('Cost of 1 shoe is 7500')
            jj=int(input('How many ?'))
            kk=jj*7500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',kk)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',kk-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',kk)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p])
                oo.close()
        elif gg=='14':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red,Yellow
Size= 6,7,8,9,10,11''')
            hh=input('Colour')
            ii=input('Size')
            print('Cost of 1 shoe is 6500')
            jj=int(input('How many ?'))
            kk=jj*6500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',kk)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',kk-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',kk)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p])
                oo.close()
    else:
        print('Please Select Correct Option')
elif a=='2':
    b=input('Please Enter your Email Id')
    c=input('Please Enter your Password')
    d=input('Please Enter your Name')
    print('Hi Mr.',d)
    print('''Please Select your Option Below
|-JEANS(3)
|-SHIRT(4)
|-SHOES(5)''')
    e=input('What you like to buy')
    if e=='3':
        print('LEVIS(6),DENIM(7),SPYKAR(8)')
        f=input('Please Select Brand')
        if f=='6':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 5000')
            print('your total cost is=',i*5000)
            j=i*5000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
        elif f=='7':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 6000')
            print('your total cost is=',i*6000)
            j=i*6000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
        elif f=='8':
            print('''-----.-----
|   | |   |
|   | |   |
|___| |___|
Colour Available=BLUE,BLACK
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            g=input('Please Select the Colour')
            h=input('SIZE?')
            i=int(input('How many?'))
            print('cost of 1 jeans is 4000')
            print('your total cost is=',i*4000)
            j=i*4000
            print('Please fill all the details below')
            k=input('Please Enter your Contact Number')
            m=input('Please Enter your Address')
            n=input('Please Enter your email Id')
            o=input('Please Enter your Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',k)
            print('Address:',m)
            print('Pincode',o)
            print('Email Id:',n)
            print('Total Cost:',j)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',j-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,k,n,f,i,m,o,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',j)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,k,n,f,i,m,o,p])
                oo.close()
    elif e=='4':
        print('|-Peter England(11)  |-Louis Phillippe(12)')
        u=input('Please Select your brand')
        if u=='11':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            v=input('Please Select your size')
            x=input('Colour')
            y=int(input('how many?'))
            print('Price of ine shirt is 4500')
            print('your total cost is=',y*4500)
            z=y*4500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',z)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',z-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',z)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p])
                oo.close()
        elif u=='12':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            v=input('Please Select your size')
            x=input('Colour')
            y=int(input('how many?'))
            print('Price of ine shirt is 6500')
            print('your total cost is=',y*6500)
            z=y*6500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',z)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',z-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',z)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,u,y,dd,ee,p,q,s])
                oo.close()
    elif e=='5':
        print('|-Nike(13) |-Reebok(14)')
        gg=input('Please Select Brand')
        if gg=='13':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            hh=input('Colour')
            ii=input('Size')
            print('Cost of 1 shoe is 7500')
            jj=int(input('How many ?'))
            kk=jj*7500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',kk)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',kk-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',kk)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p])
                oo.close()
        elif gg=='14':
            print('''-----.-----
Colour Available=BLUE,BLACK,White,Red
SIZE=S=30,M=32,L=34,XL=36,XXL=38,XXL=40''')
            hh=input('Colour')
            ii=input('Size')
            print('Cost of 1 shoe is 6500')
            jj=int(input('How many ?'))
            kk=jj*6500
            print('Please Fill the Details Below')
            bb=input('Phone Number')
            cc=input('Email.Id')
            dd=input('Enter Address')
            ee=input('Enter Pincode')
            print('Please Check ALL Details Below:-')
            print('Name:',d)
            print('Contact Number:',bb)
            print('Address:',dd)
            print('Pincode',ee)
            print('Email Id:',cc)
            print('Total Cost:',kk)
            print('If you pay by card now you will get 50 Ruppees off')
            print('|-CREDIT CARD(9)  CASH ON DELIVERY(10)')
            p=input('Please Select one option')
            if p=='9':
                print('Your total cost is=',kk-50)
                q=input('Card Number')
                r=input('Card Holder Name')
                s=input('CVV')
                t=input('OTP')
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p,q,s])
                oo.close()
            elif p=='10':
                print('Please Pay the cash to delivery Guy an amount of :',kk)
                us=random.randint(1,31)
                uss=random.randint(8,12)
                usss='2021'
                ww,www,wwww=us,uss,usss
                print('SUCCESS,YOU WILL RECIEVE ORDER BY',ww,'-',www,'-',wwww)
                bye=random.randint(123456,789999345)
                print('Your order number is',bye)
                print('For any query contact us via mail')
                hmm.writerow(['Name','Phone Number','Email ID','Brand','Quantity','Address','Pincode','MODE OF Payment','Card Number','CVV'])
                hmm.writerow([d,bb,cc,gg,jj,dd,ee,p])
                oo.close()
    else:
        print('Please Select Correct Option')






print('your csv is in this address',os.getcwd())
print('Thank you Visit Again')
