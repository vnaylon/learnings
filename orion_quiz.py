# start the quiz
score = 0
print('Hi, I’m your quiz bot. Let’s test your knowledge about your fellow Orioneers!' + '\n')

# persuade the user not to give weird answers
# print('I don’t know English very well yet, so I’m easily confused. Will you be straightforward with me?')
# honesty_consent = input()
# if honesty_consent == 'yes' or 'y' or 'Yes' or 'Y':
#        print('Thanks so much. Let’s get started.' + '\n')

# first employee question
print('Who was the first employee of Orion (after Greg and Jesse)?')
first_employee = input()
if first_employee == 'neil':
        score = score + 1
        print('That’s right! It was Neil Girling.')
