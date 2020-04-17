# Задание: гадалка с памятью и слегка переформулированными вопросами
from random import choice
from pprint import pprint
pars={}
def answer(question):
    def Compare(S1,S2):
        ngrams = [S1[i:i+3] for i in range(len(S1))]
        n=0
        for j in ngrams:
            n += S2.count(j)
        return (n/max(len(S1),len(S2)))
    if len(pars) >0:
        for key in pars.keys():
           print (Compare(key,question))
           if Compare(key,question)>0.5: 
             return key, pars[key]
             break
           pars.update([(question,choice(['yes', 'no']))])
           return question, pars[question]
    else:
        pars.update([(question,choice(['yes', 'no']))])
        return question, pars[question]
questions= ["It's you?","Are you Article Intelligent?",
           "Do you like Arduino?",
           "Do you eat Mushrooms?",
           "It's youuu?"
            ]
for question in questions:
    pprint(answer(question))
