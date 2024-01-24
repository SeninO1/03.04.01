class Cassa(object):
    money = 0
    cash = 0
    
    def __init__(self, c):
        
        self.cash = c
        
    def top_up(self):
        self.money += self.cash
        
    def count_1000(self):
        a = self.money // 1000
        return a
        
    def take_away(self):
         if self.money < self.cash:
            print('Недостаточно денег')
         self.money = self.money - self.cash
       
    
h1 = Cassa(3456)

h1.top_up()
print(h1.money)
print(h1.count_1000())
h1.take_away()
print(h1.money)