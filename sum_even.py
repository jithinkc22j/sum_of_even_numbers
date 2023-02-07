#Program to find the sum of n even numbers using user defined function
def su(n):
    if n<=2:
        return(n)
    else:
        if n%2==0:
            return(n)+su(n-1)
        else:
            return(su(n-1))
n=int(input('Enter your number: '))
print('\n The sum of',n,'even number is',su(n))
