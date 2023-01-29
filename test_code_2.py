import os,sys
from mock_input_tests import *
from code_2 import main
import random
def check_if_file_exists():
    try:
        exists = os.path.exists("code_2.py")
        assert exists == True
    except:
        sys.exit()

def get_temperature_in_celsius(temperature):
    return (temperature -32)*.5556

def test_celcius_conversion():
    check_if_file_exists()

    temperature = random.randint(32,70)
    
    conversion = get_temperature_in_celsius(temperature)

    set_keyboard_input([temperature,"a"])
    main()
    output = get_display_output()

    assert output == [
        "\nWelcome to the temperature conversion program",
        "Please enter the temperature in F you want to convert: ",
        "Please select the unit of temperature you want to convert to",
        "\na) Celsius",
        "b) Kelvin",
        "\nPlease enter your option: ",
        f"\n{temperature} in Fahrenheit is {conversion} in Celsius"
    ]

def test_kelvin_conversion():
    check_if_file_exists()
    temperature = random.randint(32,70)
    
    conversion = get_temperature_in_celsius(temperature)+273.15

    set_keyboard_input([temperature,"b"])
    main()
    output = get_display_output()

    assert output == [
        "\nWelcome to the temperature conversion program",
        "Please enter the temperature in F you want to convert: ",
        "Please select the unit of temperature you want to convert to",
        "\na) Celsius",
        "b) Kelvin",
        "\nPlease enter your option: ",
        f"\n{temperature} in Fahrenheit is {conversion} in Kelvin"
    ]

def test_invalid_option():
    check_if_file_exists
    temperature = random.randint(32,70)
    invalid_option = random.randint(3,7)

    set_keyboard_input([temperature,str(invalid_option)])
    main()
    output = get_display_output()
    assert output == [
        "\nWelcome to the temperature conversion program",
        "Please enter the temperature in F you want to convert: ",
        "Please select the unit of temperature you want to convert to",
        "\na) Celsius",
        "b) Kelvin",
        "\nPlease enter your option: ",
        f"\nSorry, unfortunately {invalid_option} option is not valid"
    ]

