f = open('sample.txt','r')
print(f.read(10))
print(f.readline())
f.close()
f = open('sample.txt','a')
f.write("JJust chill chill")
f.close() 
with open("sample.txt") as f:
    data = f.read()
data = data.replace("#####","sfFGFGfjbfdj")
data = data.lower()
with open("sample.txt",'w') as f:
    f.write(data) 