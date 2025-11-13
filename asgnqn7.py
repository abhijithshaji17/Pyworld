#Predicting Output

#Q7.
text = "datascience"
res = ""
for i in range(len(text)):
   if i % 2 == 0:
       res += text[i].upper()
   else:
       res += text[i].lower()
print (res)
  
