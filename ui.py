from datetime import datetime, date

def welcome_message():
    print(
        '''
        Welcome to the Quiz program
        choose a category
        answer the multiple choices

        '''
    )
    

def get_user_topic(categories):
    for category in categories:
        print(category)
    
    user_topic=input('please enter category: ').lower()

    return user_topic


def get_answer():
    response=input('Enter the correct answer: ')
    
    return response

def correct_or_not(response, correct_ans, question):
    
    if response == correct_ans:
        print('correct! ')
        is_correct= True
        earned_point= question[8]
    else:
        print(f'incorrect! the correct answer is {correct_ans}')
        is_correct= False
        earned_point= 0
    return is_correct, earned_point

def display_results(user_topic, questions, t_points, n_correct_ans, e_point, stime, etime):
    start = datetime.strptime(stime[0], '%H:%M:%S.%f').time()
    end = datetime.strptime(etime[-1], '%H:%M:%S.%f').time()
    time_taken = datetime.combine(date.min,end)- datetime.combine(date.min, start)
    
    number_of_questions=len(questions)

    earned_point= int(''.join(map(str, e_point)))
    total_points = int(''.join(map(str, t_points)))
    percentage = (earned_point/total_points)*100

    print('\nHere is the results of the quiz')
    print(f'''
    Topic: {user_topic}
    Time: {time_taken}
    number of questions asked: {number_of_questions}
    number of correct answers: {int(''.join(map(str, n_correct_ans)))}
    available points: {total_points}
    earned_points: {earned_point}
    percentage: {percentage}%
        
    ''')
