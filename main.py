import collections
import csv
import datetime

d1 = datetime.datetime.now()
counter = 0
names = []
dateDonationsCount = []
dateDonations = []
with open("C:\\Users\\henrique.r.mendes\\Documents\\Projetos\\Testes\\by_date\\itcont_big.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    for line in csv_reader:
        names.append(line[7].split(",")[0])
        timestamp = line[4]
        sliceMonth = slice(4, 6)
        sliceYear = slice(0, 4)
        formattedTimestamp = timestamp[sliceYear] + "-" + timestamp[sliceMonth]
        dateDonationsCount.append(formattedTimestamp)
        counter = counter + 1

d2 = datetime.datetime.now()

print("Ini do processamento: ", d1)
print("Ter do processamento: ", d2)
print("Tempo total de processamento: ", (d2 - d1))
print("quantidade de linhas: {:,}".format(counter))
print("Nome 432: ", names[432])
print("Nome 43243: ", names[43243])
print(collections.Counter(dateDonationsCount))
