from Question import Question

question_prompts = [
    "What is the colour of the Netflix logo?\n(a) Blue\n(b) Green\n(c) Red\n(d) Yellow\n\n",
    "What is the colour of the Sunflower?\n(a) Red\n(b) Green\n(c) Violet\n(d) Yellow\n\n",
    "What is the colour of SunLight? ?\n(a) Red\n(b) Green\n(c) White\n(d) Yellow\n\n",
    "What is the colour of the Water?\n(a) Red\n(b) Green\n(c) Violet\n(d) Colourless\n\n",
    "What is the colour of the Grass?\n(a) Red\n(b) Green\n(c) Violet\n(d) Yellow\n\n"
 ]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "d"),
    Question(question_prompts[4], "b"),
]
def run(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run(questions)


