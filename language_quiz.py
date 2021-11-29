import random
import csv

#First quiz
def single_select_choice_questions():
    score = 0

    question1 = print('Incertidumbre es: \na.Falta de seguridad, de confianza o de certeza sobre algo, especialmente cuando crea inquietud. \nb.gracias \nc.adios \nd.de nada \n')
    answer1 = input('')

    if answer1 == 'a':
        score = score + 1
        print('Correct!')
        print('Score: ', score)
        print('\n')

    else:
        print('''Incorrect! The answer is a''')
        print('Score: ', score)
        print('\n')

    question2 = print('Desigualdad significa: \na.hola \nb.Condición o circunstancia de no tener una misma naturaleza, cantidad, calidad, valor o forma que otro, o de diferenciarse de él en uno o más aspectos. \nc.adios \nd.de nada \n')
    answer2 = input('')

    if answer2 == 'b':
        score = score + 1
        print('Correct!')
        print('Score: ', score)
        print('\n')

    else:
        print('''Incorrect! The answer is b''')
        print('Score: ', score)
        print('\n')

    if score == 2:
        print('Your final score is: ', score)
        print('Fantastic')
        print('''Do you want to choose another quiz? Input 'yes' if this is the case, input 'no' to return to the main menu: ''')
        user_input1 = input('')
        if user_input1 == 'yes' or 'Yes':
            main_menu()
        else:
            main_menu()

    else:
        print('Your final score is: ', score)
        print('You could do better.')
        print('''Do you want to chose another quiz? Input 'yes' if this is the case, input 'no' to play the same quiz again: ''')
        user_input2 = input('')
        if user_input2 == 'yes' or 'Yes' or 'y' or 'Y':
            main_menu()
        else:
            main_menu()

def play_single_select_choice():
    print('---------------------------------------------------------------------------------------')
    print('Welcome to the Single Select Choice Quiz, you have made a great choice!')
    print('In this quiz you will learn challenging vocabulary in Spanish.')
    print('You have to select the correct definition of a word.')
    print('There is only one correct answer.')
    print('---------------------------------------------------------------------------------------')
    print('Are you up for the challenge? Please state your name below: ')

    player_name = input('')
    single_select_choice_questions()

#Second quiz
#
def multiple_choice_questions():

        score = 0

        question1 = print(
            'Incertidumbre es: \na.Falta de seguridad, de confianza o de certeza sobre algo, especialmente cuando crea inquietud. \nb.gracias \nc.niepewność \nd.de nada \n')
        answer1 = input('')

        if answer1 == 'a' and 'b':
            score = score + 1
            print('Correct!')
            print('Score: ', score)
            print('\n')
        if answer1 == ('a' or 'b') or ('a' and 'c') or ('a' and 'd') or ('b' and 'c') or ('b' and 'd'):
            score = score - 0.5
            print('Correct!')
            print('Score: ', score)
            print('\n')
        else:
            score = score - 1
            print('''Incorrect! The answer is a''')
            print('Score: ', score)
            print('\n')

        question2 = print(
            'Desigualdad significa: \na.nierówność \nb.Condición o circunstancia de no tener una misma naturaleza, cantidad, calidad, valor o forma que otro, o de diferenciarse de él en uno o más aspectos. \nc.adios \nd.de nada \n')
        answer2 = input('')

        if answer2 == 'a' and 'b':
            score = score + 1
            print('Correct!')
            print('Score: ', score)
            print('\n')
        if answer2 == ('a' or 'b') or ('a' and 'c') or ('a' and 'd') or ('b' and 'c') or ('b' and 'd'):
            score = score - 0.5
            print('Correct!')
            print('Score: ', score)
            print('\n')

        else:
            score = -1
            print('''Incorrect! The answer is b''')
            print('Score: ', score)
            print('\n')

        if score == 2:
            print('Your final score is: ', score)
            print('Fantastic!')
            print(
                '''Do you want to chose another quiz? Input 'yes' if this is the case, input 'no' to return to the main menu: ''')
            user_input1 = input('')
            if user_input1 == 'yes' or 'Yes':
                main_menu()
            else:
                main_menu()

        else:
            print('Your final score is: ', score)
            print('You could do better.')
            print('''Do you want to chose another quiz? Input 'yes' if this is the case, input 'no' to play the same quiz again: ''')
            user_input2 = input('')
            if user_input1 == 'yes' or 'Yes':
                main_menu()
            else:
                main_menu()

def play_multiple_choice():

    print('---------------------------------------------------------------------------------------')
    print('Welcome to the Multiple Choice Quiz, you have made an excellent choice!')
    print('In this quiz you will learn challenging vocabulary in Spanish.')
    print('You have to select the correct answers for each question.')
    print('Attention! There might be more than one correct answer.')
    print('---------------------------------------------------------------------------------------')
    print('Are you up for the challenge? Please state your name below: ')

    player_name = input('')
    multiple_choice_questions()

#Third quiz
def get_true_or_false_statements():

    statements = []
    statements.append(['El perro es un animal.', 'T'])
    statements.append(['El perro es un mamífero.', 'T'])
    statements.append(['El perro es una pez.', 'F'])
    statements.append(['El gato es un animal.', 'T'])
    statements.append(['El gato es un mamífero.', 'T'])
    statements.append(['El gato es una pez.', 'F'])

    return statements

def play_true_or_false():

    print('-----------------------------------------------------------------------------------------------')
    print('Welcome to the True or False Quiz, you have made yet another great choice!')
    print('In this quiz you will learn Spanish vocabulary by deciding whether a sentence is true or false.')
    print('You have to type in T or F in capital letters to answer.')
    print('Points for incorrect answers will be deducted fro your score.')
    print('-----------------------------------------------------------------------------------------------')
    print('Are you up for the challenge? Please state your name below: ')

    player_name = input('')
    print('Hello '+player_name+'. Let the game begin!')

    true_or_false_statements = get_true_or_false_statements()
    random.shuffle(true_or_false_statements)

    score = 0

    for statement in true_or_false_statements:
        print('True or false: ' + statement[0])
        guess = input('Enter T or F: ')
        if guess == statement[1]:
            print('Correct')
            score = score + 1
            print('Your score is:',score)
        else:
            print('Incorrect')
            score = score - 1
            print('Your score is: ',score)

    print('Your final score is: ', score)

    print('''Do you want to export the questions? Input 'Y' or 'N'.''')
    user_choice3 = input('')
    if user_choice3 == 'Y' or 'y':
        with open('true_or_false_export2.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(get_true_or_false_statements())
            print('Done.')
            main_menu()
    else:
        print('''Do you want to play this quiz again? Input 'Y' if this is the case. Else, input 'N'''')
        user_tof = input('')
        if user_tof == 'Y' or 'y':
            play_true_or_false()
        else:
            print('''Do you want to play another game? Input 'Y' if this is the case. If you want to quit playing, input 'N'''')
            final_input = input('')
            if final_input == 'Y' or 'y':
                main_menu()
            else:
                exit()

#Fourth quiz
def short_answer_questions():
    import csv

    with open("C:/Users/KATARZYNA/OneDrive/Desktop/quiz/conjugacion.csv") as f:
        reader = csv.reader(f)
        quiz_qas = list(reader)


    q, a = random.choice(quiz_qas)

    print(q)
    answer = input(">>> ")
    if answer == a:
        print('correct')
    else:
        print('false')
    print('''Do you want to answer another question? Input 'Y' if this is the case, 'N' to return to main menu.''')
    user_input4 = input('')
    if user_input4 == 'y' or 'Y':
        play_short_answer()
    else:
        main_menu()

def play_short_answer():
    print('---------------------------------------------------------------------------------------')
    print('Welcome to the Short Answer Quiz, you have made a great choice!')
    print('In this quiz you will learn the conjugation of Spanish verbs.')
    print('You have to type in the correct answer.')
    print('You will be deducted points for incorrect answers.')
    print('---------------------------------------------------------------------------------------')
    print('Are you up for the challenge? Please state your name below: ')
    player_name = input('')
    print('Hello ', player_name,'! Let the game begin.')

    short_answer_questions()

def main_menu():

    print('--------------------------------')
    print('Welcome to my quiz!')
    print('--------------------------------')
    print('Please select a quiz option:')
    print('--------------------------------')
    print('1. Single Select Choice Quiz')
    #easy quiz, one answer, score is kept but no negative points
    print('2. Multiple Choice Quiz')
    #more answers, negative points and half points
    print('3. True or False Quiz')
    #negative points for wrong answers, shuffled questions, export to cvs
    print('4. Short Answer Quiz')
    #questions imported from csv file, shuffled question choice
    print('0. Quit Game')
    print('--------------------------------')

    choice = input('Enter 1,2,3,4 or 0: ')

    if choice == '1':
        play_single_select_choice()
    elif choice == '2':
        play_multiple_choice()
    elif choice == '3':
        play_true_or_false()
    elif choice == '4':
        play_short_answer()
    elif choice == '0':
        print('----------------------------------')
        print('Thank you for playing and goodbye!')
        print('----------------------------------')
        exit()

main_menu()


