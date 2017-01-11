a="on iki ada"
print(a.split())
for i in a.split():
    if i[0]=="i":
        a=a.replace("i","İ")
print(a.title())
