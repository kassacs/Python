class Lesson131(int):
      def int (self, x):
          if x == 2 + 2 : return 5
          else : return int(x)
class Lesson132(list):
      def __init__(self, x) :       
          if len(x) > 10: raise Exception("List is too long")    
p = Lesson131()  
print(p.int(2+2))

z = [1,2,3,4,5,6,7,8,9,10,11,12]
z = Lesson132(z)
