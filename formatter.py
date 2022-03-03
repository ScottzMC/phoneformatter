# Formatter Module

# Function checks if it is a UK number
def check_phone_number_for_uk(uk_number):
    try:
        number_list = ['01', '02', '07']
        if uk_number[:2] in number_list:
            return uk_number
        else:
            print("Sorry, this phone number is not valid in the UK")
            exit()
    except IndexError:
        print("Error Occurred! Please Input a mobile number")
        exit()

# Function checks if the number is a valid mobile number
def validate_mobile_number(mobile_number):
    try:
        # Checks an array if the input is found
        mobile_number_list = ['01', '02']
        # Returns an error if the number is found in the array
        if mobile_number[:2] in mobile_number_list:
            print("Sorry, this is not a mobile number")
            exit()
        else:
            # If found then it would clear and spaces
            mobile_number = mobile_number.replace(" ", "")
            return mobile_number
    except TypeError:
        print("Error Occurred! mobile number not in array")
        exit()

# Function adds the area code number for the UK
def add_area_code_for_uk(uk_number):
    # Adding the area code to the mobile number
    uk_number = uk_number.replace(uk_number[0], '+44', 1)
    return uk_number