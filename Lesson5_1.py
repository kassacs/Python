from pprint import pprint
class Person:
    def __init__ (self,rasa,name,rost,ves):
        self.rasa,self.name,self.rost,self.ves = rasa,name,rost,ves
        self.key=(rasa,name)
    def __repr__(self):
            return "Person('%s', '%s', %d, %d)" % (self.rasa, self.name, self.rost, self.ves)
fedor = Person("хоббит", "Федор Сумкин",120, 40)  
arven = Person("эльф","Арвен",188,25)
boromir = Person("человек","Боромир",79,105)
subj = { fedor.key:fedor, arven.key:arven, boromir.key:boromir}
pprint(subj)
pprint(subj[arven.key])
