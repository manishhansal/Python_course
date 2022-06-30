import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    match = re.sub(r'%|@|$|&|#|?|;', '', sentence)
    return match
# print(clean_text(sentence))

def is_valid_variable(variable):
    ex = r'[a-z]_?[a-z]'
    print(re.match(ex, variable))
# is_valid_variable('first_name')
