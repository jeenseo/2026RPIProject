
A = int(input())
B = int(input())

b1 = B % 10           
b10 = (B // 10) % 10  
b100 = B // 100       

print(A * b1)        
print(A * b10)        
print(A * b100)      
print(A * B)          