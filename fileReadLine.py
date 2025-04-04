#  f=open("file.txt")
# prt1=f.readline()

# print(prt1)
# prt2=f.readline()

# print(prt2)
# prt3=f.readline()

# print(prt3)


# prt4=f.readline()

# print(prt4)

# prt5=f.readline()

# print(prt5)

# prt6=f.readline()

# print(prt6)


# f.close()


# f=open("file.txt")
# line=f.readline()
# while(line!=" "):
   
#    print(line)
#    line=f.readline()

# f.close()

f = open("file.txt", "r")  # फ़ाइल खोलो
line = f.readline()  # पहली लाइन पढ़ो

while line:  # जब तक लाइन में कुछ है, तब तक चलाओ
    print(line, end="")  # एक्स्ट्रा newline से बचने के लिए end=""
    line = f.readline()  # अगली लाइन पढ़ो

f.close()  # फ़ाइल बंद करना ज़रूरी है
