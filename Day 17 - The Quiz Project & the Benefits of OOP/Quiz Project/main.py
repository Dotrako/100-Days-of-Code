from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Initialize an empty list to store Question objects
question_bank = list()

# Iterate over the question_data to create Question objects and add them to the question_bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_quesstion = Question(question_text, question_answer)    
    question_bank.append(new_quesstion)

# Create a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)
# Call the next_question method to display the first question
quiz.next_question()