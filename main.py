import formatter

try:
    phone_number = input("Enter your mobile number: ")
    # Checks if the Phone number is valid in the UK
    mobile_number = formatter.check_phone_number_for_uk(phone_number)
    # Validates to ensure it is a mobile number
    mobile_number = formatter.validate_mobile_number(mobile_number)
    # Adds the area code for the mobile number
    mobile_number = formatter.add_area_code_for_uk(mobile_number)
    # Limit the mobile number to 11 digits
    print('UK Mobile number: ' + mobile_number[:13])

except (ImportError, NameError, TypeError):
    print("Error Occurred!")
    exit()