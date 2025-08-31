
# base case 1
# n * n-1 
# call func

def facrorial(n) :

    if n == 1 or n == 0:
        return 1
    
    return n * facrorial(n -1 )

print(facrorial(int(input("enter a number"))))