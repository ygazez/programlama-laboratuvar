
import sympy as sym #gerekli kütüphaneleri import ettik
from sympy import Symbol
from sympy import pprint

p=Symbol('p') #değişkenleri symbol sekline cevirdik 
n=Symbol('n')
x=Symbol('x')

my_func_1=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) #formüldeki kombinasyon adımı
my_func_1
pprint(my_func_1)


my_func_2=p**x
my_func_2
pprint(my_func_2)#fonksiyonun p üzeri x kısmı


my_func_3=(1-p)**(n-x)
my_func_3
pprint(my_func_3)


my_func=my_func_1*my_func_2*my_func_3 #adımları birleştirip gerçek fonksiyonu elde ettik
my_func #binom dağılımı fonksiyonu
pprint(my_func)


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

x_values=[] #değerleri oluşturduk
y_values=[]
for value in range (0,10): 
    y=my_f.subs({p:0.25,n:10,x:value},title="Binomial Distribution") 
    y_values.append(y) 
    x_values.append(value)
    print(value,y)
 
 
 plt.plot(x_values,y_values) 
plt.show() #grafiği çizer

#Bir fabrikada uretilen urunlerden arızalı olanların secilmesi durumunu 1 ile arızalı 
#olmayanlarında secilmemesini 0 ile gosterirsek,arızalı gelmesi olasılıgı %25 olduguna gore 10 urun secilmesi durumunda
#binom dagılım fonksiyonun grafiginin cizimi 
#p=0.25=1/4 
#n=10

