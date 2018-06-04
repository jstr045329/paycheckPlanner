#!/usr/bin/env python

from datetime import datetime, timedelta

KNOWN_PAYDAY = "2018-01-01"
PERIODS_FWD = 5

class book:
    def __init__(self):
        x = {}
        for m in range(-3, 32):
            x[m] = []
        self.book = x
        self.dt = datetime.strptime(KNOWN_PAYDAY, "%Y-%M-%d")

    def addExpense(self, nm, dayNum, amt):
        self.book[dayNum].append({"name":nm, "amount":amt})

    def oneCycle(self):
        dStart = self.dt
        tot = 0
        rep = ''
        for m in range(0, 14):
            k = self.dt.day
            for n in self.book[k]:
                tot += n["amount"]
                rep += str(k) + " " + n["name"] + " : " + str(n["amount"]) + "\n"
            self.dt = self.dt + timedelta(1)
        return [tot, rep]

    def nCycles(self, N):
        for m in range(0, N):
            print("For pay period starting: ", str(self.dt))
            x, y = self.oneCycle()
            print(y)
            print("Total is ", x)
            print("\n\n")

if __name__=="__main__":
    b = book()
    b.addExpense("house", 1, 1000)
    b.addExpense("car", 2, 380)
    b.addExpense("credit 1", 13, 300)
    b.addExpense("credit 2", 17, 320)
    b.addExpense("phone", 22, 90)
    b.nCycles(8)



























