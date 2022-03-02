import formatter as fm
try:
    input_number = input("Enter your mobile number: ")
    # Validates to ensure it is a mobile number
    number = fm.validate_number(input_number)
    # Trims any whitespace in the phone number
    mobile_number = fm.area_code_for_gb(number)
    # Limit the mobile number to 11 digits
    print('UK Mobile number: ' + mobile_number[:13])
except (ImportError, NameError, TypeError):
    print("Error Occurred!")
    exit()