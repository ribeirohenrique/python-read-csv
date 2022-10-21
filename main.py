import datetime

d1 = datetime.datetime.now()
print("Inicio do processamento: ", d1)

counter = 0
names = []
dateDonationsCount = []
dateDonations = []
with open("C:\\Users\\henrique.r.mendes\\Documents\\Projetos\\Testes\\by_date\\itcont_big.txt") as f:
    # with open("mock.csv") as f:
    for line in f:
        names.append(line.split("|")[7].split(",")[0])
        # 201903139145683419
        timestamp = line.split("|")[4]
        sliceYearAndDay = slice(0, 6)
        sliceDay = slice(4, 6)
        sliceYear = slice(0, 4)
        formattedTimestamp = timestamp[sliceYear] + "-" + timestamp[sliceDay]
        dateDonationsCount.append(formattedTimestamp)
        counter = counter + 1

print("quantidade de linhas: {:,}".format(counter))

d2 = datetime.datetime.now()
print("Termino do processamento: ", d2)
print("Nome 432: ", names[432])
print("Nome 43243: ", names[43243])
print("Contagem de data 2019-03: ", dateDonationsCount.count("2019-03"))
# print("Array com datas: ", dateDonationsCount)
print("Tempo de processamento total: ", (d2 - d1))
