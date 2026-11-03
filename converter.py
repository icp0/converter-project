def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == "km" and to_unit == "miles": return value * 0.621371
    if from_unit == "miles" and to_unit == "km": return value / 0.621371
    raise ValueError(f"Неподдерживаемая конвертация: {from_unit} -> {to_unit}")

def convert_mass(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == "kg" and to_unit == "pounds": return value * 2.20462
    if from_unit == "pounds" and to_unit == "kg": return value / 2.20462
    raise ValueError(f"Неподдерживаемая конвертация: {from_unit} -> {to_unit}")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == "celsius" and to_unit == "fahrenheit": return value * 9 / 5 + 32
    if from_unit == "fahrenheit" and to_unit == "celsius": return (value - 32) * 5 / 9
    raise ValueError(f"Неподдерживаемая конвертация: {from_unit} -> {to_unit}")

def main():
    print("Конвертер величин v0.4")
    print(convert_length(10, "km", "miles"))
    print(convert_mass(5, "kg", "pounds"))
    print(convert_temperature(100, "celsius", "fahrenheit"))

if __name__ == "__main__":
    main()
