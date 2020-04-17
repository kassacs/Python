from random import choice
pars={}
def answer(question):
     if question  not in pars.keys(): 
         pars.update([(question,choice(['yes', 'no']))])
     return question, pars[question]
questions= ["It's you?","Are you Article Intelligent?",
           "Do you like Arduino?",
           "Do you eat Mushrooms?",
           "It's you?",
           "Do you eat Mushrooms?"
           ]
for question in questions:
    print(answer(question))
