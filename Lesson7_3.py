''' Задание: Добавить вывод неподходящих запросов и отладку.
   Примечание: Вместо имени,фамилии, возраста, улицы, номера дома использована раса, имя, фамилия, рост, вес'''
   
   from pprint import pprint
from itertools import product
RASA_WORDS = {'раса','народность','гражданство'}
NAME_WORDS    = {'имя','зовут',"персонаж"}
FAMIL_WORDS = {'фамилия','второе имя','прозвище'}
ROST_WORDS     = {'рост', 'выше', 'ниже'}
VES_WORDS = {"вес","больше","меньше"}
def compare(S1,S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    n=0
    for j in ngrams:
        n += S2.count(j)
    return (n/max(len(S1),len(S2)))
def int_val(s):
    try:
        return int(s)
    except ValueError:
        return 0
class Person:
    def __init__ (self,rasa,name,famil,rost,ves):
        self.rasa,self.name,self.famil,self.rost,self.ves = rasa, famil,name,rost,ves
        self.key=(rasa,name)
    def __repr__(self):
            return "Person('%s', '%s', '%s', %d, %d)" % (self.rasa, self.name, self.famil, self.rost, self.ves)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.rasa, self.name, self.famil,self.rost,self.ves) == (obj.rasa, obj.name, obj.famil, obj.rost, obj.ves)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()
       
    def __fuzzy_compare(self, query):
        def by_rasa(Q):
            Q = Q - RASA_WORDS
            W = set(self.rasa.replace(',','').split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
            return max(rez)[0]
           
       
        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
 
            return max(rez)[0]

        def by_famil(Q):
            Q = Q - NAME_WORDS
            W = set(self.famil.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a,b),a,b)]
 
            return max(rez)[0]       
        def by_rost(Q):
            query_rost = max([ int_val(q) for q in Q ])
            if 'выше' in Q:
                return query_rost < self.rost
            if 'ниже' in Q:
                return query_rost > self.rost
            return query_rost + 15 >= self.rost >= query_rost - 15
        def by_ves(Q):
            query_ves = max([ int_val(q) for q in Q ])
            if 'больше' in Q:
                return query_ves < self.ves
            if 'меньше' in Q:
                return query_ves > self.ves
            return query_ves + 10 >= self.ves >= query_ves - 10
        q_words = set(query.split())
        score = 0
        for m_words, method in zip([RASA_WORDS, NAME_WORDS, FAMIL_WORDS, ROST_WORDS,VES_WORDS],
                                   [by_rasa, by_famil,   by_name,    by_rost, by_ves]):
            if m_words & q_words:
                score += method(q_words)
               
        return score > 0.49
fedor = Person("хоббит", "Федор", "Сумкин",120, 40)  
arven = Person("эльф","Арвен","Ундомиэль",188,25)
gendalf = Person("человек","Гендальф","Серый",179,59)
subj = { fedor.key:fedor, arven.key:arven, gendalf.key:gendalf}
queries = [
    'имя Арвен',
    'рост 188',
    'больше 25',
    'меньше 50',
    'раса хоббит',
    'выше 120',
    'фамилия эльф',
    'зовут Федо',
    'фамилия Сумк',
    'прозвище Серый'
    
]
for query, person in product(queries, subj.values()):
    if person == query:
        pprint((query, person))
if __name__ == '__main__':
    out = []
    for a,b in [
            ('алгоритм','алгоритм'),
            ('алгоритм','алгоритмы'),
            ('алгоритм','алгоритмов'),
            ('стол','столик'),
            ('стол','стул'),
            ('федор','фродо'),
            ('гендальф','гена'),
            ('эльф','ильф'),
            ('арвен','арвуша'),
        ]:
        out += [(a,b,compare(a,b))]
        pprint(out)
    pprint([ int_val(s) for s in ['выше','30','но','101'] ] )
