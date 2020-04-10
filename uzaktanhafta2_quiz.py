from sympy import Symbol

x = Symbol('x')
y = Symbol('y')

p = x * (x + x)
print(p)

p = (x + 2) * (x + 3)
print(p)

from sympy import factor, expand
expr = x ** 2 - y ** 2

factors = factor(expr)
expand = expand(factors)

print(expand, factors)

expr = x ** 3 + 3 * x ** 2 * y + 3 * x * y ** 2 + y ** 3
factors = factor(expr)
print(factors)

from sympy import pprint
pprint(expr)
pprint(factors)
x = Symbol('x')
series = x
n = 5
for i in range(2, n + 1):
    series = series + (x ** i) / i
pprint(series)

expr = x * x + x * y + x * y + y * y
res = expr.subs({x: 1, y: 2})
print(res)

r = expr.subs({x:1-y})
print(r)

x = Symbol('x')
series = x
n = 5
x_value = 10
for i in range(2, n + 1):
    series = series + (x ** i) / i
pprint(series)

series_value = series.subs({x:x_value})
print(series_value)
pprint(series_value)
 
 
import sympy as sym
from sympy import Symbol
from sympy import pprint

import sympy.plotting as syp

sigma= Symbol('sigma')
mu = Symbol('mu')
x = Symbol('x')


sym.sqrt(2*sym.pi*sigma)
pprint(1/(sym.sqrt(2*sym.pi*sigma*sigma)))

part1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gaussfunction = part1*part2
pprint(my_gaussfunction)



syp.plot(my_gaussfunction.subs({mu:10, sigma:30}), (x, -100, 100), title='gauss distribution')


x_values = []
y_values = []

for value in range (-5, 5):
    y = my_gaussfunction.subs({mu:10, sigma:30, x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

import matplotlib.pyplot as plt

plt.plot(x_values,y_values)
plt.show()

#symbol : sembolik değerleri pyhton kütüphanesine ekleme
#factor : çarpanlarına ayırma
#expand : ifadeyi açma
#expr : fonk tanımı
#pprint : günlük kullanımlara yakın matematiksel yazım
#expr.subs({prmtr1:1 , prmtr2:2}) : parametre1, parametre2ye göre yazılır
#sqrt : kök alma
#syp.plot : fonksiyon grafiğini çizmek için
#function : fonksiyon demek
#evalf : sayısal form elde eder
#exp(x) : e üzeri x demek
#plt.show : grafik gösterimi
#append : listeye ekleme
#symbol('y') : verilen değeri semboliğe çevirmek için
#f.subs : değişkenlere değer atar

