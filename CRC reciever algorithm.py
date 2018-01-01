def XOR(s1, s2):
    x=""
    for i in range(1,len(s1)):
       if int(s1[i]) != int(s2[i]):
          x += "1"
       else:
          x += "0"
    return x
try:
   m = input()
   g = input()
   if len(g) <= 2 or len(g) >= 10**3:
      print("-1")
      exit(0)
   if g[0] == '0'  or g[len(g)-1] == '0':
      print("-1")
      exit(0)
   if len(g) > len(m):
    print("-1")
    exit(0)
   l = len(g)
   temp1 = m[:l]
   print(temp1)
   temp2 = ""
   if temp1[0] == '1':
      temp2 = g
   else:
      temp2 = "0" * len(g)
   temp1 = XOR(temp1,temp2)
   print(temp1)
   for w in m[l:]:
      temp1 += w
      print(temp1)
      if temp1[0] == '1':
         temp2 = g
      else:
         temp2 = "0" * len(g)
      temp1 = XOR(temp1, temp2)
   x=temp1.find("1")
   if x != -1:
       print("-1")
       exit(0)
   else:
       m = m[:len(m)-len(temp1)]
       print(m)
except Exception as e:
    print("Error: "+str(e))