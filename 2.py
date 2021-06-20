a = "hello word"
print(a[1:4])
print(a.upper())
b =10
c =10
print(b>c)
if a == c:
    print("True")
else:
    print("False")

thislist = ["apple", "orange" , "cherry"]
thislist.append("fang")
thislist.insert(3,"emp")
thislist.remove("apple")
print (thislist) 
thisdict = {
    "brand" : "Fond",
    "model": "mustand",
    "year" : 1964
    }
print(thisdict)

print(thisdict["model"])
print("------------------")
for x in thisdict:
    print(thisdict[x])

print("------------------")
for x in thisdict.values():
    print(x)

print("------------------")
for x, y in thisdict.items():
    print(x, y)


