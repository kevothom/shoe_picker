# Heading or banner of the online store
print("""        This is an online Shoe store
        that allows the customers to pick
        the shoes they are looking to purchase 
        with extensive detail and precision
############################################################""")
# Prints out the different shoe types
print("Choices of shoes are: Sneakers  Dress  Boots  Casual")
print("                      ##############################")
# Prompts user to input type of shoes desired
shoe_choice=input("What kind of shoes are you looking to purchase?: " )
# Prints out to screen kind of shoes customer types in
print(shoe_choice)
# Prompts user to input shoe brand looking to purchase
shoe_brand = input("What is the desired brand of shoes you are looking for?: ")
# Prints out to screen the customer shoe brand 
print(shoe_brand)
# Prompts user to input shoe size desired    
shoe_size = input("What is the desired shoe size?: ") 
# If/else statement: if shoe size is 10 prints out first 2 print statement
if shoe_size == str("10"):
        print ("We do hava a size ten") 
        print('And it is at a great sales price!')
# else if size is not 10 these 2 print statements are printed
else:
        print("Sorry we only have size ten and up in those shoes")
        print('You will have to choose a different brand')
    
    
      
      
      
      
      
      
      
      
      
    
      
      
      
      
      
      
      
      
      
      
