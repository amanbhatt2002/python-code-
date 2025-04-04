f=open("poem.txt")
data=f.read()
if("twinkle" in data):
  print("present")

else:
  print("not present")


f.close()