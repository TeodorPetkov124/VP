num = int(input("How many numbers of Fibonacci? "))

n1, n2 = 0, 1
count = 0

if num <= 0:
   print("Enter a positive ")

elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1