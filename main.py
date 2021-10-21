import random
from questions import *
from results import *
from ui import *
from datetime import date, datetime, timedelta

def main():
    create_table_questions()
    create_table_results()

    respose=check_db_questions()    #checks if there are questions in db
    if respose[0] == 0:
        create_questions()
        
    #select_all_questions()
    categories=db_categories()  #gets distinct topics in the question db
    welcome_message()
    user_topic = get_user_topic(categories) 
    questions= get_questions(user_topic)
    total_points = get_total_point(user_topic)
    results= start_quiz(questions)
    add_results_to_db(results)
    n_correct_ans=numb_of_correct_ans()
    earned_point=earned_points()
    stime, etime =quizz_time()
    
    display_results(user_topic, questions, total_points, n_correct_ans, earned_point, stime, etime)
    delete_results_db()
    
    
def start_quiz(questions):
    results = []

    for question in questions:
        correct_ans= question[2]

        start_time = str(datetime.now().time())

        print('\n'+ question[1])
        
        multi= [question[2], question[3], question[4], question[5]]
        random.shuffle(multi)

        for choice in multi:
            print(choice)
        
        response=get_answer().lower()
        
        end_time = str(datetime.now().time())
        question_id=question[0]
        user_ans = response

        is_correct, earned_point= correct_or_not(response, correct_ans, question)
        
        results.append(result(start_time, question_id, user_ans,
        is_correct, end_time, earned_point))

        
    return results

    
    


if __name__ == '__main__':
    main()