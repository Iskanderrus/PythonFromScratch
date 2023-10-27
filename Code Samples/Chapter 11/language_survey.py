from survery import AnonymousSurvey

# Define a question, and make a survey
question = 'What language did you first learn to speak?'
language_survey = AnonymousSurvey(question=question)

# Display the question and store responses to the questions:
language_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ').strip().title()
    if response.lower() == 'q':
        break
    language_survey.store_response(response)

# Show the survey results:
print("\nThank you to everyone who participated in the survey!")
language_survey.show_results()
