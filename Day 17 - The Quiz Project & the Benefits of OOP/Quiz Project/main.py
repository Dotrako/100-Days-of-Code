from data import question_data
from question_model import Question

# Initialize an empty list to store Question objects
question_bank = list()

# Iterate over the question_data to create Question objects and add them to the question_bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_quesstion = Question(question_text, question_answer)    
    question_bank.append(new_quesstion)
    
# Print the text and answer of the second question in the question_bank (index starts at 0)
print(question_bank[1].text)
print(question_bank[1].answer)