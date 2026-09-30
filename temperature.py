# i., ii., iii., & iv. Define the conversion function
def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# v. Ask the user to enter the temperature in Celsius
celsius_input = float(input("Enter temperature in Celsius: "))

# vi. Call the function and display the converted temperature to 2 decimal places
fahrenheit_result = convert_temperature(celsius_input)
print(f"Temperature in Fahrenheit: {fahrenheit_result:.2f}°F")
