MyDict = {
    "Fast":"In a Quick Manner",
    "Dharm": "the richest",
    "Marks": [1,2,5],
    "anotherdict":{'dharm':'player'},
    1:2
}
print(MyDict['Fast'])
print(MyDict['Dharm'])
MyDict['Marks'] = [45, 78]
print(MyDict['Marks'])
print(MyDict['anotherdict']['dharm'])
print(type(MyDict))
print(list(MyDict.keys()))
print(list(MyDict.values()))
updateDict = {
    "lovish" : "friend",
    "Divya" : "frinend",
    "Dharm" : "Born to be richest"
}
MyDict.update(updateDict)
print(MyDict)
print(MyDict.get("Dharm2"))
#print(MyDict["Dharm2"])

#Important: This syntax will create an empty dictionary and not an empty set
a={}
print(type(a))
#set is collection of non repetetive items and tuple can be added
b=set()
print(type(b))
b.add(4)
b.add(5)
b.add((4,5,6))
print(b)
print(len(b))
b.remove(5)
#b.remove(15)
print(b.pop())