class Student(object):

    def __init__(self, first_name, last_name, address):
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

student_1 = Student("Jasmine", "Debugger", "0101 Computer Street")
student_2 = Student("Jacqui", "Console", "888 Binary Ave")

class Question(object):

    def __init__(self, question, answer):

        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):

        print(self.question)
        user_answer = input(">")
        if user_answer == self.answer:
            return True
        else:
            return False 
     
alberta_capital = Question("What is the capital of Alberta?", "Edmonton")
python_author = Question("Who is the author of Python?", "Guido Von Rossum")

class Exam(object):

    def __init__(self, name):

        self.name = name 
        self.questions = []

    def add_question(self, question):

        self.questions.append(question)
    
    def administer(self):

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score = score + 1 

        return score / len(self.questions)

class StudentExam(object):

    def __init__(self, student, exam):

        self.score = 0
        self.student = student 
        self.exam = exam
        

    def take_test(self):
        
        self.score = self.exam.administer()
        print(f"Your score is {self.score}")

def example():

    new_exam = Exam("Midterm") 
    new_student = Student("Alex", "Milliron", "the moon")

    new_exam.add_question(alberta_capital)
    new_exam.add_question(python_author)

    alex_test = StudentExam(new_student, new_exam)

    alex_test.take_test()

class Quiz(Exam):

    def __init__(self, name):
        super().__init__(name)

    def administer(self):
        
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score = score + 1 
        
        if score > len(self.questions) // 2:
            return 1
        else:
            return 0

class StudentQuiz(object):

    def __init__(self, student, quiz):

        self.score = None
        self.student = student 
        self.quiz = quiz
        
    def take_test(self):
        
        self.score = self.quiz.administer()

        if self.score:
            print("You passed!")
        else:
            print("Oh no! You failed!")





        

            








        