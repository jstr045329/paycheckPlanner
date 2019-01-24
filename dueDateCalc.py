#!/usr/bin/env python

from datetime import datetime, timedelta

def twoDecimals(x):
    return int(x*100)/100

class book:
    def __init__(self, knownPayday):
        x = {}
        for m in range(-3, 32):
            x[m] = []
        self.book = x
        self.dt = datetime.strptime(knownPayday, "%Y-%M-%d")
        self.payCheck=1 # Set this manually before using
        self.savings=0
        self.saveRatio=0.5

    def addExpense(self, nm, dayNum, amt):
        self.book[dayNum].append({"name":nm, "amount":amt})

    def oneCycle(self):
        dStart = self.dt
        tot = 0
        rep = '' # Report string
        for m in range(0, 14):
            k = self.dt.day
            for n in self.book[k]:
                tot += n["amount"]
                rep += str(k) + " " + n["name"] + " : " + str(n["amount"]) + "\n"
            self.dt = self.dt + timedelta(1)
        deltaSavings = self.saveRatio * (self.payCheck-tot)
        self.savings += deltaSavings
        rep += "Money Saved This Pay Cycle: " + str(twoDecimals(deltaSavings)) + "\n"
        rep += "Total Saved: " + str(twoDecimals(self.savings)) + "\n"
        return [tot, rep]

    def nCycles(self, N):
        for m in range(0, N):
            print("For pay period starting: ", str(self.dt))
            x, y = self.oneCycle()
            print(y)
            print("Expenses This Pay Cycle:   ", twoDecimals(x))
            print("\n\n")

if __name__=="__main__":
    b = book("2018-01-01")
    b.addExpense("house", 1, 1000)
    b.addExpense("car", 2, 380)
    b.addExpense("credit 1", 13, 300)
    b.addExpense("credit 2", 17, 320)
    b.addExpense("phone", 22, 90)
    b.nCycles(8)



























