# make a program it shows the product of even and odd numbers from 50 to 1

evn = 1  # start with 1 not 0. if you use 0 the answer is always 0
odd = 1
n = 50

while n >= 1:
    if n%2 == 0:
        evn = evn*n
    else:
        odd = odd*n  
    n = n-1       

print(f"evn_prod: {evn}")
print(f"odd_prod: {odd}")