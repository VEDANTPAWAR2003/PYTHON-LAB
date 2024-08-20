def print_patterns(l):
 for i in range(l+1):
   for j in range(i, l+1):
      print(' ', end=' ')
   for j in range(i):
      print('+', end=' ')
      
     #  print ('*', end =' ')
   for j in range(i +1):
     print('+', end=' ')
   print()
   
 for i in range(l):
   for j in range(i+2):
     print(' ', end=' ')
   for j in range(i, l):
     print('-', end=' ')
   for j in range(i, l-1):
    print('-', end=' ')
   print()
   
l = int(input())
if l in [1, 2, 3]:
    print_patterns(l)
else:
    print("Invalid input.")
