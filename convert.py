import csv


b = []

with open('/Users/harden/Downloads/已发送.csv', newline='') as f1:
    r = csv.reader(f1, delimiter=' ', quotechar='|')
    for row in r:
        info = row[0].split(',')[0]
        # print(info)
        b.append(info)
print(b.__len__())

a = []
with open('/Users/harden/Downloads/4231ffqwe.csv', newline='') as f2:
    r = csv.reader(f2, delimiter=' ', quotechar='|')
    for row in r:
        info = row[0].split(',')[0]
        if info not in b:
          print(info)
          a.append(info)

print(a.__len__())

with open('/Users/harden/Downloads/output.csv', 'w', newline='') as f3:
    write = csv.writer(f3, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in a:
      write.writerow([row])