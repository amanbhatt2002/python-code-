with open("practice.txt",'w') as f:
  f.write("solving problems  in file input output\n")


with open("practice.txt","r") as f:
  data=f.read()
  print(data)


with open("practice.txt","a") as f:
  f.write("hello bsdk")




with open("practice.txt","r") as f:
  data=f.read()
  print(data)



with open("practice.txt", "r") as file:
  for line in file:
       print(line.strip())  # Removes extra newline characters
