def find_sequence(sequence):
    superscript = {'1': '¹', 'n': 'ⁿ', '-': '⁻'}

    try:
        a1, a2, a3 = map(float, sequence)
    except ValueError:
        return "Invalid input. Please enter numeric values."

    if len(sequence) <= 2:
        return "Too few elements in the sequence."

    diff1 = a2 - a1
    diff2 = a3 - a2

    if diff1 == diff2:
        return f"Arithmetic Sequence: {int(diff1)}n + {int(a1 - diff1)}"
    elif a1 != 0 and a2 != 0 and a2 / a1 == a3 / a2 and a2 / a1 != 0:
        ratio = a2 / a1
        exponent_expression = "n-1"
        superscript_expression = ''.join(superscript.get(char, char) for char in exponent_expression)
        return f"Geometric Sequence: {int(ratio)}{superscript_expression} × {int(a1)}"
    else:
        return "Neither arithmetic nor geometric sequence detected. Please check the input."

if __name__ == "__main__":
    sequence_input = input("Input sequence (space-separated): ").split()
    result = find_sequence(sequence_input)
    print(result)
