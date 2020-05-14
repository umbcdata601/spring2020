# from mehmet Sarica, 20180907

def palindromic7():
    for i in range(1000, 10000):
        x = str(i)[:-1][::-1]
        print (str(i) + x)

def palindromicOdd(num=7):
    if num % 2 == 0:
        return ("enter an odd number")
        
    m = int((num - 1)/2)
    for i in range(10**m, 10**(m+1)):
        x = str(i)[:-1][::-1]
        print (str(i) + x)

def palindromicAll(num=7):
    if num % 2 == 1:
        m = int((num - 1)/2)
        isOdd=True
    else: 
        m = int(num/2-1)
        isOdd=False
        
    for i in range(10**m, 10**(m+1)):
        x =   str(i)[:-1][::-1] if isOdd else str(i)[::-1]
        print (str(i) + x)

