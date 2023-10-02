# Path: python_intro.py 

# Function to check if a value exist in a list
def check_value(var,l1):
    if var in l1:
        position = l1.index(var) + 1
        return("exist value in " f"{position} position")
    else:
        return("not exist value in list")
    
list = [1,2,3,4,5,6,7,8,9,10]
list_str = [str(valor) for valor in list]
   
print("Hi")
print(check_value(input("please, Impute value :  "),list_str))


# Function aleatory controller
import random

list_most_use=[6,7,8,9]
list_dont_use=[10,0,1,2,3,4,5]

valor_aleatory = random.randint(1,4)
print(valor_aleatory)

if valor_aleatory == 4:
    valor_final = list_dont_use[random.randint(0,6)]
else:
    valor_final = list_most_use[random.randint(0,3)]

print(valor_final)

