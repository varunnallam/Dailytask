for mutliples of three, print "Fizz" instead of number, and for multiples of five, print "Buzz".
for i in range(1,100+1):
    if(i%3==0):
       print("Fizz")
    elif(i%5==0):
       print("Bizz")
    else:
       print(i)