from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Initialize an empty list to store Question objects
question_bank = list()

# Iterate over the question_data to create Question objects and add them to the question_bank
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)    
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Loop through questions while there are still questions left
while quiz.still_has_question():
    quiz.next_question()

# Display the final score after completing the quiz
print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
