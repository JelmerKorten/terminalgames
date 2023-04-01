#a quiz game

print('Welcome to my quiz!')
playing = input('Would you like to play my game? (yes/no) ')
if playing.lower() != 'yes':
    quit()
print('Okay! Let\'s play! :)')
score = 0
name = input('What is your name? ')
print(f'Nice to meet you {name}, let\'s get started!')

#we should do this with a formula or maybe add the questions to a list / dict
questions = ['question1 ', 'question2 ', 'question3 ']
answers = ['answer1', 'answer2', 'answer3']
question_index = 0

for i in range(len(questions)):
    answer = input(questions[i])
    if answer.lower() == answers[i]:
        print('Well done, you have it right!')
        score += 1
    else:
        print('Sorry, not true.')

total_score = float(score / len(questions))*100
print('That were all the questions.\nLet\'s see how you\'ve done...')
print(f'You had {score} out of {len(questions)} correct!')
print('Calculating score, standby!')
print(f'Your score is: {round(total_score)}%')

