def XOR(s1, s2, l):
    i=1
    x=""
    for i in range(1,l):
       if int(s1[i]) != int(s2[i]):
          x += "1"
       else:
          x += "0"
    return x
try:
   m = input("Enter the message: ")
   g = input("Enter the Generator: ")
   if len(g) <= 2 or len(g) >= 10**3:
      print("-1")
      exit(1)
   if g[0] == '0'  or g[len(g)-1] == '0':
      print("-1")
      exit(1)
   l = len(g)
   r = l-1  #the power
   s = m + "0"*r  #the message
   temp1 = s[:l]
   temp2 = ""
   if temp1[0] == '1':
      temp2 = g
   else:
      temp2 = "0" * len(g)
   temp1 = XOR(temp1,temp2,l)
   for w in s[l:]:
      temp1 += w
      if temp1[0] == '1':
         temp2 = g
      else:
         temp2 = "0" * len(g)
      temp1 = XOR(temp1, temp2, l)
   s = m + temp1
   print("Message sent is : "+s)
except Exception as e:
    print("Error: "+str(e))
