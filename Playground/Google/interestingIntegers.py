'''

Let us call an integer interesting if the product of its digits is divisible by the sum of its digits. You are given two integers A and B. Find the number of interesting integers between A and B (both inclusive).

Sample Input
4
1 9
91 99
451 460
501 1000

Sample Output
Case #1: 9
Case #2: 0
Case #3: 5
Case #4: 176

'''



def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum

def getProduct(n):
    prod = 1
    for digit in str(n):
        prod *= int(digit)
    return prod

def interesting_integers(start, end):
    count = 0
    for i in range(start, end+1):
        prod = getProduct(i)
        sum = getSum(i)
        
        if prod % sum == 0:
            count += 1
    return count


t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n, m = [int(s) for s in input().split(" ")]
    print(f'Case #{i}: {interesting_integers(n,m)}')
    