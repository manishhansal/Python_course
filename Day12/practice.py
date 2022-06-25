import random


def generate_Id():
    length = int(input('Enter length of the id: '))
    num_id = int(input('Enter number of ids: '))
    alpha_num = ["a",
             "b",
             1,
             "c",
             "d",
             "e",
             2,
             "f",
             "g",
             3,
             "h",
             "i",
             4,
             "j",
             "k",
             5,
             "l",
             "m",
             6,
             "n",
             "o",
             7,
             "p",
             "q",
             8,
             "r",
             "s",
             9,
             "t",
             "u",
             0,
             "v",
             "w",
             "x",
             "y",
             "z", 1,2,3,4,5,6,7,8,9,0]
    for i in range(num_id):
        ans = ""
        for i in range(length):
            ans += str(random.choice(alpha_num))
        print(ans)
# generate_Id()

def rgb_color_gen():
    return f'rgb({random.randint(0, 255)},{random.randint(0,255)},{random.randint(0,255)})'
# print(rgb_color_gen())

def list_of_hexa_colors():
    alpha_num = [0,7,"a",1,"b",2,"c",3,9,"d",4,"e",5,"f",6,8]
    ans = ""
    for i in range(6):
        ans += str(random.choice(alpha_num))
    return f'#{ans}'
# print(list_of_hexa_colors())

def generate_colors(pram1, num):
    if pram1 == 'hexa':
        ans = []
        for i in range(num):
            ans.append(list_of_hexa_colors())
        return ans
    elif pram1 == 'rgb':
        ans = []
        for i in range(num):
            ans.append(rgb_color_gen())
        return ans
    else:
        return 'Param1 should be valid.'
# print(generate_colors('rgb', 5))

def random_unique():
    unique = []
    while len(unique) <= 7:
        temp = random.randint(0,9)
        if not temp in unique:
            unique.append(temp)
    return unique
print(random_unique())



