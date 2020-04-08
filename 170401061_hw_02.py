import csv
import datetime
 
 def my_frequency_with_list_of_tuples(inlist):
     frekans_liste=[]
     for i in range(len(inlist)):
        s=False
        for j in range(len(frekans_liste)):
            if(inlist[i]==frekans_liste[j][0]):
                frekans_liste[j][1]=frekans_liste[j][1]+1
                s=True
        if(s==False):
            frekans_liste.append([inlist[i],1])
      return frekans_liste 
      
def mean(inlist):
   sum = 0
   count = len(inlist)
   for index in inlist:
       sum += index
        # count += 1
    mean = sum / count
    return mean
      
      
def median(inlist):
    newInlist = sorted(inlist)
    n = len(newInlist)
    if n % 2 == 1:
        middle = int(n/2)+1
        median = newInlist[middle - 1]
    else:
        middle_1 = int(n/2) - 1
        middle_2 = middle_1 + 1
        median = (newInlist[middle_1] + newInlist[middle_2]) / 2
    return median      
      
      

with open ("input_hw_2.csv") as csv_file:
      okur=csv.reader(csv_file)
      tarihler=[]
      aylar=[]
      for satir in okur:
          a=satir[3]
          tarihler.append(a)
      for i in tarihler:
          ay=datetime.datetime.strptime( tarihler[i], "%Y-%m-%d %H:%M:%S.%f")
          aylar.append(ay.month)
          
      list=my_frequency_with_list_of_tuples(aylar) 
      
     			

    
dosya=open('170401061_hw_02_output.txt','w+')
dosya.write(f"Median : {median(list)}")
dosya.write(f"Ortalama : {mean(list)}")
