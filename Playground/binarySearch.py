# Binary Search
def binary_search(lts, target):
    low = 0
    high = len(lts)-1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if lts[mid] == target:
            return f'Target is found at index {mid}'
        elif lts[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 'Target is not found.'

lts = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    target = input('Enter a number: ')
    if target.isnumeric():
        print(binary_search(lts, int(target)))
    else:
        print('Invalid input')