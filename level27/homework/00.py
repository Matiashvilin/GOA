
for num in range(101):
   
    addition = num + 10
  
    subtraction = num - 5
   
    multiplication = num * 2
   
    if num != 0:
        division = num / 2
    else:
        division = "undefined"  
        
        
    print(f"რიცხვი: {num}, დამატება 10-ზე: {addition}, გამოკლება 5-ზე: {subtraction}, "
          f"გამრავლება 2-ზე: {multiplication}, გაყოფა 2-ზე: {division}")
