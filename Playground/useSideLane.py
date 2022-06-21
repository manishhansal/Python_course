def useSideLane(lts, n):
    stack = []
    idx = 0
    next_number = 1
    while idx < n or len(stack) > 0:
        if idx < n and lts[idx] == next_number:
            idx += 1
            next_number += 1
        elif len(stack) > 0 and stack[-1] == next_number:
            stack.pop()
            next_number += 1
        else:
            if idx < n:
                stack.append(lts[idx])
                idx += 1
            else:
                return 'No'
    if next_number > n:
        return 'Yes'
    else:
        return 'No'

my_arr = [7, 5, 1, 2, 3, 4, 6]
n = 7
print(useSideLane(my_arr, n))
