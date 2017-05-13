myDict = {
    'apple':['a round fruit with red skin', '蘋果'],
    'banana':['a long fruit with yellow skin','香蕉'],
    'watermelon':['a large, round fruit with green skin', '西瓜']
    }

def list_all_words():
    print('Your word list:\n')
    for key, value in myDict.items():
        print('{} ({})\n{}\n'.format(key,value[1],value[0]))

def new_words():
    try:
        word, definition, chinese = input('Enter a new word (word, definition, chinese):').split(',')
        myDict[word] = [definition, chinese]
        print('New word "{}" has been added!'.format(word))
    except ValueError:
        print('Please make sure your format is correct!')
    except:
        print('Something happend unexcepted!')

def remove_words():
    word = input('Enter a word you want to removed:')
    if word in myDict:
        del(myDict[word])
        print('The keyword "{}" has been removed!'.format(word))
    else:
        print('There is no "{}" in dictionary!'.format(word))
    
def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_word_list = []
    for key, value in myDict.items():
        while True:
            answear = input('\nWhich word matches the definition? or [c]hinese, [p]ass, [q]uit\n{}'.format(value[0]))
            if answear == 'c':
                print(value[1])
            elif answear == 'p':
                print('The correct answer is "{}"'.format(key))
                incorrect_word_list.append(key)
                break
            elif answear == 'q':
                quit_the_test = True
                break
            elif answear == key:
                points += 1
                print('Correct!')
                break
            else:
                print('It\'s not correct')

        if quit_the_test == True:
            break

    print('\nScore {}/{}'.format(points, len(myDict)))
    print('Incorrect words list:')
    for key in incorrect_word_list:
        value = myDict[key]
        print('{} ({})\n{}\n'.format(key, value[1], value[0]))
                

def run():
    while True:
        cmd = input("""\nWelcome to your dictionary!
1) Test your self!
2) List all words
3) Add new word
4) Remove word
5) Exit\n""")
        
        if cmd == '1':
            test_yourself()
        elif cmd == '2':
            list_all_words()
        elif cmd == '3':
            new_words()
        elif cmd == '4':
            remove_words()
        elif cmd == '5':
            break


run()
