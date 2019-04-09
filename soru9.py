#soru9
#en büyük satır toplamı ve en büyük sutun toplamı
matris=[[1,2,3],[2,4,6],[1,2,1]]

toplamsutundizisi =[]
toplamsatirdizisi =[]
for i in range(0,3):

    toplamsatir = 0
    toplamsutun = 0

    for j in range(0,3):
        toplamsatir += matris[i][j]
        toplamsutun += matris[j][i]

    toplamsatirdizisi.append(toplamsatir)

    toplamsutundizisi.append(toplamsutun)


print(max(toplamsutundizisi),max(toplamsatirdizisi))
