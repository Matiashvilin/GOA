my_list = [10, 15, 20, 25, 30, 35, 40, 45, 50]


even_sum = 0
odd_sum = 0


for number in my_list:
    if number % 2 == 0:  
        even_sum += number
    else: 
        odd_sum += number


print("ლუწი რიცხვების ჯამი:", even_sum)
print("კენტი რიცხვების ჯამი:", odd_sum)
