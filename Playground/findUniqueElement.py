def FindUniqueElement(lts):
    ans = lts[0]
    for num in lts[1:]:
        ans = ans ^ num
    return ans

my_arr = [2,3,1,4,5,4,1,3,5]
print(FindUniqueElement(my_arr))
