##n=input("Enter the string:")
##print(int(n[0])*sum(int(i) for i in n[1:]))


##n=int(input())
##even_sum= sum(int(i) for i in str(n) if int(i)%2==0)
##print(even_sum)


##n=list(input("Enter string:"))
##if n[0]=='(':
##    if n[-1]==')':
##        print ('True')
##    else:
##        print ('False')
##elif n[0]=='[':
##    if n[-1]==']':
##        print ('True')
##    else:
##        print ('False')
##elif n[0]=='{':
##    if n[-1]=='}':
##        print ('True')
##    else:
##        print ('False')  
##else:
##    print('False')

        
##A=100
##def addit(a,b):
##    v=A
##    total=v+b
##    return total
##a=int(input())
##b=int(input())
##print(addit(A,b))


##k=5
##n=[int(input("Enter values:"))for i in range(k)]
##j=n.sort()
##print('The largest number in the list is:',n[-1])


##k=5
##n=[int(input("Enter values:"))for i in range(k)]
##print('The largest number in the list is:',max(n))


##a=input("Enter string:")
##for i in a:
##    if i == 'a' and i == 'e' and i == 'i' and i == 'o' and i=='u':
##        print(count(i))
##    if i=='a':
##        count(i)
##    if i=='e':
##        count(i)


##n=int(input())
##print(n**2)


##l= int(input())
##m = int(input())
##n = int(input())
##
##
##a = [l+i*m for i in range(n)]
##print(*a)
##    
##k=l+m+n
##print(k)
##j=k/l 
##print(j)


##import math
##n=int(input())
##print(math.factorial(n))


##n=int(input())
##fact=1
##if (n>0):
##    for i in range(1,n+1):
##        fact*=i
##    print(fact)


##m=int(input("Enter Number:"))
##j=m+1
##n=[x for x in range(m,j)]
##print(n)


##n=[x for x in range(1,11)]
##print(n)


x=int(input("Enter number:"))
y=int(input("Enter value to be added:"))
n=[int(i) for i in str(x+y)]
print(n)









