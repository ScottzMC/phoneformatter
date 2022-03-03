import pytest
import formatter as fm

class TestFormatter:
    number_list = ['01', '02', '07']
    mobile_number = "+44"
    phone_number = '07'
    test_mobile_number = "07"

    # Test the Check phone number function is valid in the UK
    def test_check_phone_number_for_uk(self):
        assert fm.check_phone_number_for_uk(self.phone_number) in self.number_list

    # Test to Validate mobile number function
    def test_validate_mobile_number(self):
        assert fm.validate_mobile_number(self.phone_number) == self.test_mobile_number

    # Test the Add area code for Uk function
    def test_add_area_code_for_uk(self):
        assert fm.add_area_code_for_uk(self.mobile_number)

if __name__ == '__main__':
    pytest.main()