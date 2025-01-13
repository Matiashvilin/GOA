def check_number_sign(number):
    
    if number > 0:
        return "დადებითი"
    elif number < 0:
        return "უარყოფითი"
    else:
        return "ნული"

result = check_number_sign(-15)
print("რიცხვი არის:", result)

result = check_number_sign(25)
print("რიცხვი არის:", result)

result = check_number_sign(0)
print("რიცხვი არის:", result)
