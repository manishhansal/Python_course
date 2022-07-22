
def print_pattern(n):
    row = 1
    low = 1
    high = 2
    pattern = ""
    while row <= n:
        for num in range(low, high):
            pattern += str(num) + " "
        pattern.strip()    
        pattern += "\n"
        row += 1
        low = high
        high += row
    return pattern.strip()

print(print_pattern(10))