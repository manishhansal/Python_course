# def ArrangeList(lts):
#     result = []
#     zero = 0
#     one = 0
#     two = 0
#     for item in lts:
#         if item == 0:
#             zero += 1
#         elif item == 1:
#             one += 1
#         else:
#             two += 1
    
#     zero_idx = 0
#     while zero_idx <= zero:
#         result.append(0)
#         zero_idx += 1
#     one_idx = 0
#     while one_idx <= one:
#         result.append(1)
#         one_idx += 1
#     two_idx = 0
#     while two_idx <= two:
#         result.append(2)
#         two_idx += 1
#     return result

# my_arr = [2,1,0,2,0,2,1,1,0]
# print(ArrangeList(my_arr))

def ArrangeList(lts):
    l = 0;
    m = 0;
    h = len(lts) - 1

    while m <= h:
        if lts[m] == 0:
            temp = lts[l];
            lts[l] = lts[m];
            lts[m] = temp;
            m += 1
            l += 1
        elif lts[m] == 1:
            m += 1
        else:
            temp = lts[h];
            lts[h] = lts[m];
            lts[m] = temp;
            h -= 1
    return (lts)

my_arr = [2,1,0,2,0,2,1,1,0,1]
print(ArrangeList(my_arr))
