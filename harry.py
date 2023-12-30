def main():
    superscript = {'1': '¹', 'n': 'ⁿ', '-': '⁻'}
    sequence = input("Input sequence (space-separated): ").split()

    if len(sequence) <= 2:
        print("Too few elements in the sequence.")
        return
    a1, a2, a3 = map(int, sequence)
    diff1 = a2 - a1
    diff2 = a3 - a2
    if diff1 == diff2:
        print(f"Arithmetic Sequence: {diff1}n + {a1 - diff1}")
        return
    
    if a1 != 0 and a2 != 0 and a2 / a1 == a3 / a2:
        ratio = a2 / a1
        exponent_expression = "n-1"
        superscript_expression = ''.join(superscript.get(char, char) for char in exponent_expression)
        print(f"Geometric Sequence: {int(ratio)}{superscript_expression} × {int(a1)}")

        return

    print("Neither arithmetic nor geometric sequence detected.")

if __name__ == "__main__":
    main()
