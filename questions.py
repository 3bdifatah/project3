import sqlite3

quiz_db = 'quiz.sqlite'

class Question:
    def __init__(self, id, question_text, correct_answer, wrong_answer_1, 
        wrong_answer_2, wrong_answer_3, category, difficulty, points):
        self.id= id
        self.question_text= question_text
        self.correct_answer= correct_answer
        self.wrong_answer_1= wrong_answer_1
        self.wrong_answer_2= wrong_answer_2
        self.wrong_answer_3= wrong_answer_3
        self.category= category
        self.difficulty= difficulty
        self.points= points
    
    def add(self):
        sql = '''
		INSERT INTO questions (question_id, question_text, correct_answer, wrong_answer_1, 
        wrong_answer_2, wrong_answer_3, category, difficulty, points) 
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
		'''
        with sqlite3.connect(quiz_db) as conn:
            conn.execute(sql, (self.id, self.question_text, self.correct_answer, self.wrong_answer_1, 
        self.wrong_answer_2, self.wrong_answer_3, self.category, self.difficulty, self.points))
        conn.close()


'''
def select_all_questions():
    sql= 'SELECT * from questions'
    conn= sqlite3.connect(quiz_db)
    rows= conn.execute(sql)
    results= rows.fetchall()
    for result in results:
        print(result)
    conn.close()
'''

def create_table_questions():
        with sqlite3.connect(quiz_db) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS questions 
            (question_id INTEGER PRIMARY KEY, question_text TEXT, correct_answer TEXT COLLATE NOCASE, 
            wrong_answer_1 TEXT, wrong_answer_2 TEXT, wrong_answer_3 TEXT, 
            category TEXT, difficulty INTEGER, points INTEGER, UNIQUE(question_text COLLATE NOCASE))''')
        conn.close()


def check_db_questions():
    sql = 'SELECT COUNT(*) FROM questions'
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql)
    questions = data.fetchone()
    conn.close()

    return questions


def create_questions():

    # Is this the best way to organize this data? 

    q_id = [
        1,
        2,
        3,
        4,
        5,
        6
    ]
    q_texts = [
        'Who painted the Mona Lisa?',
        'Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?',
        'Which planet is closest to the sun?',
        'How many moons does Mars have?',
        'Which country has won the soccer world cup the most times?',
        'who won the nba finals 2020?'
    ]
    q_answers = [
        'vincent van gogh',
        'chicago',
        'mercury',
        '2',
        'brazil',
        'los angeles lakers'
    ]
    q_choice_1 = [
        'leonardo da vinci',
        'las vegas',
        'venus',
        '1',
        'england',
        'milwaukee bucks'
    ]

    q_choice_2 = [
        'pablo picasso',
        'philadelphia',
        'jupiter',
        '0',
        'germany',
        'toronto raptors',
    ]

    q_choice_3 = [
        'claude monet',
        'washington d.c.',
        'saturn',
        '3',
        'italy',
        'golden state warriors'
    ]

    q_category =[
        'art',
        'art',
        'space',
        'space',
        'sports',
        'sports'
    ]

    q_difficulty= [
        5,
        3,
        3,
        4,
        2,
        1
    ]
    q_points = [
        100,
        60,
        60,
        80,
        40,
        20
    ]
    questions = []

    for id, text, answer, choice_1, choice_2, choice_3, category, difficulty, points in zip(
        q_id, q_texts, q_answers, q_choice_1, q_choice_2, q_choice_3, q_category, q_difficulty, q_points):
        
        questions.append(Question(id, text, answer, choice_1, choice_2, choice_3, category, difficulty, points))

    for question in questions:
        question.add()

def db_categories():
    sql = 'SELECT DISTINCT category FROM questions'
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql)
    categories = data.fetchall()
    conn.close()

    return categories
    


def get_questions(topic):
    sql = 'SELECT * FROM questions WHERE category = ?'
    with sqlite3.connect(quiz_db) as conn:
        conn.row_factory = sqlite3.Row  # set the row factory. Then you can 
        # access data in each column as question['question_text'] or question['correct_answer'] 
        # instead of question[1] or question[2]
        data=conn.execute(sql, (topic, ))
    questions = data.fetchall()
    conn.close()

    return questions


def get_total_point(topic):
    sql= 'SELECT SUM(points) FROM questions WHERE category = ?'
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql, (topic, ))
    total = data.fetchone()
    conn.close()

    return total