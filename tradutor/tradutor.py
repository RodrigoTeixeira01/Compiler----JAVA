from os import unlink
a=open("traducoes.txt")
r=open("a_traduzir.txt")
resp=r.read()
traducoes=[]
for b in a.read().split("\n"):
    b="\n".join(b.split("\\n"))
    traducoes.append(b.split("->"))
for b in traducoes:
    resp=resp.replace(b[0],b[1])
try:
    unlink("java\\java.java")
except:
    ''
java=open("java\\java.java","at+")
java.write("import java.util.Scanner;\nclass Java{\n"+resp+"\n}")

