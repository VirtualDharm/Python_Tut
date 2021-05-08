import os
print(os.listdir())
sentence = " and ".join(os.listdir())
print(sentence)
name = "dharm"
channel = "youtube/dharm"
a = "{1} has channel by name {0}".format(name,channel)
print(a)