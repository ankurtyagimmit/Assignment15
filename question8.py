#8. Write a python script to check if a string contains only numbers.
str1 = 'ankur189'
 
print(str(str1))

result =any(chr.isdigit() for chr in str1)
     
print(str(result))
