def print_pattern(array):
	n = len(array)
	
	for i in range(2*n + 1):
		for j in range ( 2*n+1):
			if(i + j == n or j - i == n or i + j == 3*n or i -j == n):
				print("*",end="")
			
			elif(i == n and j == n):
				print(n,end="")
			
			elif(i == 2*n or i == 2*n +1):
				print("*",end="")
			else:
				print(" ",end="")
				
		
		print()
	


def main():
    size = int(input("Enter the size of the array: "))
    
    array = [0] * size
    
    print_pattern(array)

if _name_ == "_main_":
    main()
