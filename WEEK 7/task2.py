def fruit_price(**kwargs):

   for fruit in kwargs.keys():
       print(fruit)
fruit_price(mango=10, appple=5, orange=15)