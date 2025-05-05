# shift_string.py
def shift_string(input_str: str, shift_amount: int) -> str:
    if not input_str.isalpha():
        raise ValueError("First input must contain only letters (a-z, A-Z).")
    if not isinstance(shift_amount, int):
        raise ValueError("Second input must be an integer.")
    
    shift_amount = shift_amount % len(input_str)
    return input_str[-shift_amount:] + input_str[:-shift_amount]

if __name__ == "__main__":
    try:
        input_str = input("Enter a string with only letters: ")
        shift_amount = int(input("Enter a number to shift by: "))
        result = shift_string(input_str, shift_amount)
        print("Shifted string:", result)
    except Exception as e:
        print("Error:", e)
