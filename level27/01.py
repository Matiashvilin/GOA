
num1 = int(input("5: "))
num2 = int(input("2: "))


sum_result = 0
product_result = 1


for num in range(num1, num2 + 1):
    sum_result += num          
    product_result *= num      


print(f"რიცხვების {num1} და {num2} შორის ჯამი: {sum_result}")
print(f"რიცხვების {num1} და {num2} შორის ნამრავლი: {product_result}")
