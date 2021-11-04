import random
# avoid importing everything from a module. It's hard to read your code and know which functions are 
# defined in questions, which are defined in results, which are defined in ui.

# either 
# import ui
# and then use the functions like this, 
# ui.welcome_message()   # really obvious that this function is part of ui.py

# or, import by name, so you can look at the list of imports and know where things came from 

# from ui import welcome_message, get_user_topic, etc... 

# Another disadvantage of importing everything, is you may have two functions with the same 
# name in two of these modules - how will you tell them apart? Easy to have conflicts. 
from questions import *
from results import *
from ui import *

# good import 
from datetime import date, datetime, timedelta

""" This is a nice, clean, high-level file for managing the program """

def main():
    create_table_questions()
    create_table_results()

    respose = check_db_questions()    # checks if there are questions in db
    if respose[0] == 0:
        create_questions()
        
    #select_all_questions()
    # be consistent with spacing. It's most common to add one space before and after the 
    # equals sign in an assignment statement, one space after the # in a comment 
    categories = db_categories()  # gets distinct topics in the question db
    welcome_message()
    user_topic = get_user_topic(categories) 
    questions= get_questions(user_topic)
    total_points = get_total_point(user_topic)
    results= start_quiz(questions)
    add_results_to_db(results)
    n_correct_ans=numb_of_correct_ans()  # avoid abbreviations. number_of_correct_answers is a better name 
    earned_point=earned_points()
    stime, etime =quizz_time()  # same as previous comment - start_time and end_time are better names 
    
    display_results(user_topic, questions, total_points, n_correct_ans, earned_point, stime, etime)
    delete_results_db()  # Keep all the results 
    
    
def start_quiz(questions):
    results = []

    for question in questions:

        # this code would be more readable if you used row_factory
        # set the row factory in the database code . Then you can 
        # access data in each column using the column names, so this line can be 
        correct_ans = question['correct_answer']
        # correct_ans= question[2]

        start_time = str(datetime.now().time())  # usually better to store times as timestamps numbers instead of 
        # string human-readable times. It's easy to convert a timestamp to a human-readable time, not so easy the other way round. 

        print('\n'+ question[1])
        
        # using row_factory would make this clearer too 
        multi= [question[2], question[3], question[4], question[5]]
        random.shuffle(multi)

        for choice in multi:
            print(choice)
        
        response=get_answer().lower()
        
        end_time = str(datetime.now().time())  # store this as a timestamp too
        question_id=question[0]
        user_ans = response

        is_correct, earned_point= correct_or_not(response, correct_ans, question)
        
        results.append(result(start_time, question_id, user_ans,
        is_correct, end_time, earned_point))

        
    return results

    
    


if __name__ == '__main__':
    main()