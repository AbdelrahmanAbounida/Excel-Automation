
my_dictionary = {'grand', 'mother', 'grandmother', 'has', 'one','box' ,
'strong','strongbox', 'in', 'her','back'  , 'yard'  ,'my', 'backyard'}

def divide_sentence(string, n, result):
    for i in range(1, n + 1):
        word = string[:i]
        if word in my_dictionary:
            if i == n:
                result += word
                print(result)
                return

            divide_sentence(string[i:], n - i, result + word + " ")


def all_sentences(sentence):
    divide_sentence(sentence, len(sentence), "")



# TEST
Sentence =  "mygrandmotherhasonestrongboxinherbackyard"


all_sentences(Sentence)












