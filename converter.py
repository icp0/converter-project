import os

ROUND_DIGITS = int(os.environ.get('ROUND_DIGITS', 2))

def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == 'km' and to_unit == 'miles': return round(value * 0.621371, ROUND_DIGITS)
    if from_unit == 'miles' and to_unit == 'km': return round(value / 0.621371, ROUND_DIGITS)
    raise ValueError('Unknown unit: ' + str(from_unit) + ' -> ' + str(to_unit))

def convert_mass(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == 'kg' and to_unit == 'pounds': return round(value * 2.20462, ROUND_DIGITS)
    if from_unit == 'pounds' and to_unit == 'kg': return round(value / 2.20462, ROUND_DIGITS)
    raise ValueError('Unknown unit: ' + str(from_unit) + ' -> ' + str(to_unit))

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == 'celsius' and to_unit == 'fahrenheit': return round(value * 9 / 5 + 32, ROUND_DIGITS)
    if from_unit == 'fahrenheit' and to_unit == 'celsius': return round((value - 32) * 5 / 9, ROUND_DIGITS)
    raise ValueError('Unknown unit: ' + str(from_unit) + ' -> ' + str(to_unit))

def batch_convert(filepath):
    results = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) < 3: continue
            val = float(parts[0])
            frm = parts[1]
            to = parts[3] if len(parts) > 3 else parts[2]
            if frm in ('km', 'miles'): results.append(convert_length(val, frm, to))
            elif frm in ('kg', 'pounds'): results.append(convert_mass(val, frm, to))
            elif frm in ('celsius', 'fahrenheit'): results.append(convert_temperature(val, frm, to))
    return results

def main():
    print('Converter v2.0 (ROUND_DIGITS=' + str(ROUND_DIGITS) + ')')
    print(batch_convert('examples.txt'))

if __name__ == '__main__':
    main()
