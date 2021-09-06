
num = int(input("Enter a: "))

common_sum = 0
for i  in range(1, num+1):
    common_sum += i
   
i = 1
c = 0
while i < num+1:
    c += i
    i +=1

print(common_sum)     
print(c)

