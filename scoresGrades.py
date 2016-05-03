#Scores & Grades
count = 10

while count > 0:

    print 'What is your grade?'
    grade = raw_input()

    if grade >= '100':
        print 'score :', grade, 'Your grade is A'
    elif grade >= '90':
        print 'score :', grade, 'Your grade is A'
    elif grade >= '80':
        print 'score :', grade, 'Your grade is B'
    elif grade >= '70':
        print 'score :', grade, 'Your grade is C'
    elif grade >= '60':
        print 'score :', grade, 'Your grade is D'
    else:
        print 'You failed!'

    count = count - 1

raw_input('\n\nEnd of Program.')
