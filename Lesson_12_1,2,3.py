class Tolkien_subjects(): # выбран класс обобщающий логически всех персонажей, имя выбано в соответствии с рекомендациями PEP8
    def __init__(self,rasa,name,family,height,weight): #  в качестве методов выбраны характеристики персонажей
        self.rasa = rasa
        self.name = name
        self.family = family
        self.height = height
        self.weight = weight
    def go(self): # Выбран глагол в соответствии с рекомeнlациями PEP8 
        return "going"
    def stop(self): # Выбран глагол в соответствии с рекомeнlациями PEP8 
        return "stopping"
