# start the quiz
score = 0
print('Hi, I’m your quiz bot.')
print('\n')
print('Let’s test your knowledge about Orion and your fellow Orioneers!')
print('\n')

# persuade the user to give answers the program can understand
#print('I don’t know English very well yet, so I’m easily confused. Will you promise to write in lowercase?')
#lowercase_consent = input()
#if lowercase_consent == 'yes' or lowercase_consent == 'ok' or lowercase_consent == 'sure' or lowercase_consent == 'y':
#       print('Thanks so much. Let’s get started.')
#else:
#       print('Well, you either responded no or wrote in a way I don’t understand. Please type in all lowercase letters. Good luck!')
#print('\n')

# spicy question
print('Who at Orion is known for their love of spicy foods?')
spicy_lover = input()
if spicy_lover	== 'dan' or spicy_lover == 'Dan' or spicy_lover == 'Dan Phung' or spicy_lover == 'dan phung':
	score = score + 1
	print('Correct! Your score is now ' + str(score) + '. Did you know Meet is also really into spicy food?')
elif spicy_lover == 'meet':
	score = score + 1
	print('Nice! Most people guess Dan, but Meet also loves spicy food. Your score is now ' + str(score) + '.')
else:
       print('Hmm, I didn’t know that. Sounds like someone I should get to know!') 
print('\n')

# remote team question
print('Name a state that one of our remote employees lives in.')
remote_employee_guess = input()
if remote_employee_guess == 'arizona' or remote_employee_guess == 'Arizona' or remote_employee_guess == 'new york' or remote_employee_guess == 'New York' or remote_employee_guess == 'california' or remote_employee_guess == 'California' or remote_employee_guess == 'south carolina' or remote_employee_guess == 'virginia' or remote_employee_guess == 'georgia':
       score = score + 1
       print('Well done! Your score is now ' + str(score) + '.')
else:
       print('I don’t think so. Did we add somebody new?')
print('\n')

# orion name question
print('Orion (or Orion Labs) was not the company’s original name. What was Orion originally called?')
orion_company_name = input()
if orion_company_name == 'onbeep':
       score = score + 1
       print ('You got it! Orion used to be called OnBeep. I think I like the new name more. Your score is now ' + str(score) + '.')
else:
       print('Er, no. When Orion was founded, it was called OnBeep. We changed the name in 2015.')
print('\n')

# first employee question
print('Who was the first employee of Orion (after Greg and Jesse)?')
first_employee = input()
if first_employee == 'neil':
    score = score + 1
    print('That’s right! It was Neil Girling. Your current score is ' + str(score) + '.')
else:
       print('I’m sorry, that guess was not correct.')
print('\n')

# company safeword
print('You can always cut an awkward conversation short with this fruity password. What is it?')
fruit_safeword = input()
if fruit_safeword == 'blueberries': 
	score = score + 1
	print('That’s right. Sometimes you’ll hear Greg or Jesse shout "blueberries!" to stop discussion on an awkward topic.')
else:
	print('That’s not right. You’ll have to ask around for the answer.')
print('\n')

# end the quiz
print('That’s all for now. Thanks for playing. Your final score was: ' + str(score) + '.')
