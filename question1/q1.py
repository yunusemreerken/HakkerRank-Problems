#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#
def staircase(n):
    # Write your code here
    for i in range(n):
        
        for a in range(n):
            if(i+a<n-1):
                print(" ",end='')
            else:
                print("#",end='')
        print()

staircase(6)
