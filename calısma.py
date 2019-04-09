#sözlük yapısındaki değerleri matrise çevirme

sozluk={"1":1,"2":2,"3":0,"4":0,"5":0,"6":0,"7":3,"8":1,"9":0}
list=[]
matris=[[],[],[]]
for i in sozluk.values():
    list.append(i)
#print(list)
for l in range(0,3):
    matris[0].append(list[l])
for k in range(3,6):
    matris[1].append(list[k])
for m in range(6,9):
    matris[2].append(list[m])
#print(matris)
for y in range(len(matris)):

    for z in range (len(matris[y])):

        print(matris[y][z],end=" ")

    print()
