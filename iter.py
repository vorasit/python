#Iterator vs Iterable
'''
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ('apple','banana','cherry')
for x in mytuple:
    print(x)
'''

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

m1 = MyNumbers()
myiter = iter(m1)
#print(next(myiter))
print(next(myiter))