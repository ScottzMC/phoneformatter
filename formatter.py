# Formatter Module

# Function checks if it is a UK mobile number
def area_code_for_gb(mobile_number):
    try:
        if mobile_number[0] == "0":
            # Checks if there are any letters found in the user input
            for char in mobile_number:
                # Returns an error if a letter is found
                if char.isalpha():
                    print("Mobile number is incorrect, has invalid characters")
                    exit()
            # Adding the area code to the mobile number
            mobile_number = mobile_number.replace(mobile_number[0], '+44', 1)
            return mobile_number
        else:
            print("Sorry, this number is not valid in the UK")
            exit()
    except IndexError:
        print("Error Occurred! Please Input a mobile number")
        exit()

# Function checks if the number is a valid mobile number
def validate_number(mobile_number):
    mobile_number_list = ['01', '02', '03', '04', '05', '06', '08', '09']
    # Checks an array if the input is a mobile number
    try:
        if mobile_number[:2] in mobile_number_list:
            print("Sorry, this is not a mobile number")
            exit()
        else:
            mobile_number = mobile_number.replace(" ", "")
            return mobile_number
    except TypeError:
        print("Error Occurred! mobile number not in array")
        exit()