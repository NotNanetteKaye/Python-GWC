from perro import Perro
from toy import Toy
from collar import Collar

Toffee = Perro()
pink_collar = Collar()
pink_collar.color = 'pink'
coffee = Toy()


Toffee.collar.append(pink_collar)

print(Toffee.collar[0].color)