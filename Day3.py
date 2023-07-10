#for loop with else
#Even-Odd   
for i in range(1,102):
    if(i%2==0):
     print("Even:",i)
    else:
       print("Odd:",i)



# While loop with else

# Even-Odd  
i =1
while i<=101 :
    if(i%2==0):
      print("Even:",i)
    else:
       print("Odd:",i)
    i+=1


#loop manipulation 

#break using for exit
s ="Sanskruti"
for i in s:
   if i=="k":
      break
   else:
      print(i)

#continue using for skip
s ="Sanskruti"
for i in s:
   if i=="k":
      continue
   else:
      print(i)
      print("cont,")

#pass using for null
s ="Sanskruti"
for i in s:
   if i=="k":
      pass
   else:
      print(i)
      print("pass")

#pass using while loop
# i=1
# while i<=10:
#    if i==5:
#     pass
#    else:
#       print(i)
#       i+=1

#continue using while loop
# i=1
# while i<=10:
#    if i==5:
#       i+=1
#       continue
#    else:
#       print(i)
#       i+=1

#
# s ="Sanskruti"
# for i in s:
#    if i=="k":
#       pass
#    else:
#       print(i)
# else:
#    print("This has pass")

# i=1
# while i<=10:
#    if i==5:
#      i+=1
#      continue
#    else:
#       print(i)
#       i+=1
# else:
#    print("This has continue")

