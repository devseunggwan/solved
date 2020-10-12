db = {"kg": 2.2046, "lb": 0.4536, "l": 0.2642, "g": 3.7854}
db2 = {"kg": "lb", "lb": "kg", "l": "g", "g": "l"}

for i in range(int(input())):
    a, b = input().strip().split()
    print('%.4f %s' % (db[b]*float(a), db2[b]))