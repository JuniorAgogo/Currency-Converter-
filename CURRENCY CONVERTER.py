def currency_converter():
    conversion_rate = 15.50
    error_message = "Error: your input should be a positive number"
     
    isnotnumber = True
    while isnotnumber:
        try:
            # checks if the input can be converted to float
            # input imports string variable even if you input a number
            # so if it can be changed to float it will calculate GHS
            # if not, so the input is not number and with while
            # it will continously ask for a number
            USD = float(input("Enter a value in USD to be converted to GHS: "))
            GHS = USD * conversion_rate
            isnotnumber = False
            print("Your input is equal to {output} GHS".format(output=GHS))
            return(GHS)
        
        except:
            print(error_message)
            USD = input("Enter a value in USD to be converted to GHS: ")

currency_converter()