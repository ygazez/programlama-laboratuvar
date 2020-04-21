
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


sym.plot(my_func.subs({p:1/4,n:3}),(x,0,3),title='binomial distribution plot for n=3')


#Bir fabrikada uretilen urunlerden arızalı olanların secilmesi durumunu 1 ile arızalı olmayanlarında secilmemesini 0 ile gosterirsek,
 #arızalı gelmesi olasılıgı %25 olduguna gore 3 urun secilmesi
 #durumunda binom dagılım fonksiyonun grafiginin cizimi
 #p=0.25=1/4
 #n=3
 
 
