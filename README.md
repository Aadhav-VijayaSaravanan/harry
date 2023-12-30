# harry

The `harry` program analyzes a sequence to determine whether it is an arithmetic sequence, a geometric sequence, or neither.

## Usage

1. Run the program by executing the following command in the terminal:

    ```bash
    python harry.py
    ```

2. Input a sequence when prompted. The sequence should be space-separated.

3. The program will analyze the sequence and provide the result.

## Program Logic

The program follows these steps:

1. Takes a space-separated sequence as input.
2. Checks if the sequence has at least three elements. If not, it prints an error message and exits.
3. Calculates differences between consecutive elements.
4. If the differences are equal, it identifies the sequence as an arithmetic sequence.
5. If not, it checks for a geometric sequence by comparing ratios of consecutive elements.
6. If neither arithmetic nor geometric sequence is detected, it prints a corresponding message.

## Example

For example, if the input sequence is "2 4 8", the program will output:

```bash
Geometric Sequence: 2ⁿ × 2
