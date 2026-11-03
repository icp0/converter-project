def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == "km" and to_unit == "miles": return value * 0.621371
    if from_unit == "miles" and to_unit == "km": return value / 0.621371
    raise ValueError(f"Неподдерживаемая конвертация: {from_unit} -> {to_unit}")

def main():
    print("Конвертер величин v0.2")
    print(convert_length(10, "km", "miles"))

if __name__ == "__main__":
    main()
