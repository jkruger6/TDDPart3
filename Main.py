from Invoice1 import Invoice1

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice1().inputNumber("please enter unit price : ")
    qnt = Invoice1().inputNumber("Please enter quantity of product : ")
    discount = Invoice1().inputNumber("discount percent (%) : ")
    repeat = Invoice1().inputAnswer("another product? (y,n) : ")
    result = Invoice1().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice1().totalPurePrice(products)

print("Your total pure price is: ", total_amount)