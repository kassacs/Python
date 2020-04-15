""" 1. Описать классом ваши данные
    2. Реализовать поиск по полям: Вес больше 30, Имя Боромир
    3.Сделать поиск нечетким """
from pprint import pprint
class Person:
    def __init__ (self,rasa,name,rost,ves):
        self.rasa,self.name,self.rost,self.ves = rasa,name,rost,ves
        self.key=(rasa,name)
    def __repr__(self):
            return "Person('%s', '%s', %d, %d)" % (self.rasa, self.name, self.rost, self.ves)
def compare(S1,S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    n=0
    for j in ngrams:
        n += S2.count(j)
    return (n/max(len(S1),len(S2)))
    
fedor = Person("хоббит", "Федор Сумкин",120, 40)  
arven = Person("эльф","Арвен",188,25)
boromir = Person("человек","Боромир",79,105)
subj = { fedor.key:fedor, arven.key:arven, boromir.key:boromir}
pprint(subj)
for j in subj.values(): # Поиск 
    if j.ves > 30:   # по весу больше 30 
        print ("Вес больше 30",j)
    if j.name == "Боромир": # или имени Боромир
        print ("Имя Боромир",j)
    if compare("Арв",j.name)> 0.5: # по наиболее релевантному имени 
        print("Cамое релевантное имя",j)
    if (j.ves + 0.1*j.ves)>= 23 and (j.ves - 0.1*j.ves)<= 23:#по примерному весу
        print ("Наиболее близкий вес",j)
