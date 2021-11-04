import sqlite3

quiz_db = 'quiz.sqlite'

class result:  # class names typically start with uppercase letters, so Result 
    def __init__(self, start_time, question_id, user_ans, is_correct, end_time, earned_points):
        self.start_time= start_time
        self.question_id= question_id
        self.user_ans= user_ans
        self.is_correct= is_correct
        self.end_time= end_time
        self.earned_points= earned_points

    def add_result(self):
        sql = '''
		INSERT INTO results (start_time, question_id, user_ans, is_correct, end_time, earned_points) 
		VALUES (?, ?, ?, ?, ?, ?)
		'''
        with sqlite3.connect(quiz_db) as conn:
            conn.execute(sql, (self.start_time, self.question_id, self.user_ans, self.is_correct, self.end_time, self.earned_points))
        conn.close()
        


def create_table_results():
        with sqlite3.connect(quiz_db) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS results 
            (start_time TEXT, question_id INTEGER, 
            user_ans TEXT, is_correct BOOLEAN, end_time TEXT, earned_points INTEGER, 
            FOREIGN KEY(question_id) REFERENCES questions(question_id))''')
        conn.close()


def add_results_to_db(results):
    for r in results:
        r.add_result()

def numb_of_correct_ans():
    sql = 'SELECT COUNT(*) FROM results WHERE is_correct = ? '
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql, '1',)
    n_correct_ans = data.fetchone()
    conn.close()

    return n_correct_ans

def earned_points():
    sql = 'SELECT SUM(earned_points) FROM results'
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql)
    earned_point = data.fetchone()
    conn.close()

    return earned_point

def quizz_time():
    sql = 'SELECT start_time, end_time from RESULTS'
    with sqlite3.connect(quiz_db) as conn:
        data=conn.execute(sql)
    stimes, etime=data.fetchall()
    conn.close()

    return stimes, etime

def delete_results_db():
    sql = 'Delete  FROM results'
    with sqlite3.connect(quiz_db) as conn:
        conn.execute(sql)
    conn.close()

