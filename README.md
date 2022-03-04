# Phone formatter

## Description
This is a project that takes in the user input and validates it to ensure it is a United Kingdom Mobile number. The project is built on Python 3.

## Libraries used
Pytest -> Unit testing framework for Python

## Installation
This project can be installed either by downloading the file from the Github repository or by doing a pull from this project. 
The necessary library that would need to be installed as well would be pytest. 
### Running
    pip install pytest

## Files
### main
This is the main file that runs the project and takes input from the client or user. The file can be run automatically if the Developer uses PyCharm or IDE that is specifically built for Python.
### Running the file
    python main.py

### formatter
This is the module that carries out the checks on the following user input:
  1. Checks if the input is a valid phone number in the UK
  2. Checks if the input is a valid mobile number
  3. Trims the input to ensure spaces are removed from the mobile number
  4. Adds the UK area code (+44) to the mobile number

### test_formatter
This class or files carries out test from the pytest library on the various functions imported and used by the formatter module. This class checks if those functions passes or failes the objective of what they are to achieve. The file can be run automatically if the Developer uses PyCharm or IDE that is specifically built for Python.
### Running the file
    python test_formatter.py
