def main():
    global a1, a2, a3, ratio, wantNum
    superscript = {'1': '¹', 'n': 'ⁿ', '-': '⁻'}
    sequence = input("Input sequence (space-separated):     ").split()

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
        want = input("Would you like to get the first 5 values of the given sequence? (y/n):    ")
        
        if want == "y":
            wantNum = int(input("Enter the n amount of time you would like to get the values for:    "))
            wanted()
        return

    print("Neither arithmetic nor geometric sequence detected.")

def wanted():
    global a1, ratio, wantNum
    print(f"First {wantNum} term(s):    ", end=" ")
    sequence_terms = [str(int(ratio) ** (i - 1) * a1) for i in range(1, wantNum)]
    print(" ".join(sequence_terms))

main()
