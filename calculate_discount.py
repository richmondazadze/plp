def calculate_discount(price, discount_percent):
    
    if discount_percent > 20:
        price = price*(discount_percent/100)
        print(f' The price is {price}')
    else:
        print(f' The price is {price}')


calculate_discount((int(input("Enter the price: "))), (int(input("Enter the discount percent: "))))
