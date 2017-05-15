import random

colors = ['red','green','blue','purple','black']
lucky_color = random.choice(colors)

for i in range(3):
    print('There are {} colors'.format(colors))
    guess = input('Guess your lucky color:')
    if guess != lucky_color:
        print('Seems like {} is not your lucky color :('.format(guess))
        colors.remove(guess);
    else:
        break

if (guess == lucky_color):
    print("Great! {} is your lucky color.".format(lucky_color))
else:
    print("Actually, {} is your lucky color.".format(lucky_color))
    

