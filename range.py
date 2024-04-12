##1. Write a program in py to display the first 10 natural numbers.

##for i in range(1,11):
##    print(i,end = " ")

##2. Write a py program to compute the sum of the first 10 natural numbers.

##sum=0
##for i in range(1,11):
##    print(i,end=" ")
##    sum+=i    
##print("The Sum is:",sum)

##3. Write a program in py to display n terms of natural numbers and their sum.

##sum=0
##n=int(input("Enter a number:"))
##for i in range(1,n+1):
##    print(i,end=" ")
##    sum+=i
##print("The sum is:",sum)

##4.Write a program in py to read 10 numbers from the keyboard and find their sum and average.

##x=0
##for i in range(1,11):
##    print("enter number:",i,"=",i)
##    x+=i
##avg = x/10
##print(avg,x)

##5. Write a program in py to display the cube of the number up to an integer.

##y=0
##x=int(input("Enter number of terms:"))
##for i in range(1,x+1):
##    y=i**3
##    print("The number is:",i, "and the cube of the number is:",y)
    
##6. Write a program in py to display the multiplication table for a given integer.

##x=int(input("Enter the number to be calculated:"))
##for i in range(1,11):
##    y=i*x
##    print(f"{x} x",i," = ",y)

##8. Write a py program to display the n terms of odd natural numbers and their sum.

x=0
n=int(input("Enter no of terms:"))
for i in range(1,n+1):
    if i%2!=0:
        print(i,end=" ")
        x+=i
print("The sum of odd number upto",n,"terms are",x)
  
##9. Write a program in py to display a pattern like a right angle triangle using an asterisk.

##x=int(input("Enter the term:"))
##for i in range(0,x):
##    for j in range(0,x):
##        print("*",end=" ")
##    print()


##15. Write a py program to calculate the factorial of a given number.

##y=1
##x=int(input("Enter a number:"))
##for i in range(1,x+1):
##    y*=i
##print("The factorial of",x,"is",y)
    
##16. Write a py program to display the sum of n terms of even natural numbers.

##a=0
##x=int(input("Number of terms:"))
##for i in range(1,x+1):
##    if i%2==0:
##        print("The even numbers are:",i)
##        a+=i
##print("The Sum of even Natural Number upto",x," terms:",a)



