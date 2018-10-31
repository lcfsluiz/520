#!/usr/bin/python3

from conta import Conta, Poupanca
c1 = Conta('luiz', 12333, 10000)
c2 = Conta('maria', 12344, 20000)

c2.sacar(500)
print(c2.saldo)

c1.sacar(100)
print(c1.saldo)
