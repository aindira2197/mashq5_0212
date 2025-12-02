#1 - misol
roy = [12, 35, 7, 9, 0]
res = list(filter(lambda son: son % 3 == 0 and son > 5, roy))
print(res)

#2- misol
roy2 = ['tom', 'bob', 'alex', "elle"]
res2 = list(filter(lambda soz: soz[::-1] == soz, roy2))
print(res2)

#3 - misol
roy3 = [1, 2, 'tom', 10, 'bob']
res3 = list(filter(lambda a: roy3.index(a) % 2 != 0, roy3))
print(res3)

#4 - misol
roy4 = ['Tom', 'bob', 'Alex', "elle"]
res4 = list(filter(lambda soz: soz[0] == soz[0].title(), roy4))
print(res4)

#5 - misol
roy5 = [-2, 8, -3, -1, 7, 6]
res5 = list(filter(lambda son: son%2 != 0 and son > 0, roy5))
print(res5)
