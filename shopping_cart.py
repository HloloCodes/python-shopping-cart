foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    
    else:
        price = float(f"Enter the price of {food}: R")
        foods.append(food)
        prices.append(price)
        
        print("______YOUR CART______")
        
        for food in foods:
            print(food)
            
        for price in prices:
                total += price
                
print("Your total is: R{total}")