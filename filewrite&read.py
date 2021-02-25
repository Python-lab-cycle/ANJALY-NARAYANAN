line="anjaly narayanan"
f1=open("test2.txt","w")
f1.write(line)
f1.close()
f1=open("test2.txt","r")
line=f1.read()
print("line",line)
f1.close()
