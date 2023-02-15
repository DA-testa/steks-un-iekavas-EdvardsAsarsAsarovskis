# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))
            # Process opening bracket, write your code here
           

        if next in ")]}": 
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position
    else:
        return "Success"
            # Process closing bracket, write your code here
            


def main():
    choice = input("Izvēle starp failiem: 'I' input or 'F' test files: ")
    if choice == 'I':
        text = input("Enter a sequence of brackets: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    elif choice == 'F':
        test_files = ["tests/01", "tests/02", "tests/03", "tests/04", "tests/05", "tests/06", "tests/07", "tests/08", "tests/09", "tests/10"]
        for test_file in test_files:
            with open(test_file + ".a") as f:
                expected_output = f.readline().strip()

            with open(test_file) as f:
                text = f.readline().strip()

            output = find_mismatch(text)
            if output == expected_output:
                print(f"{test_file}: OK")
            else:
                print(f"{test_file}: Failed. Expected {expected_output}, but got {output}")
    else:
        print("Invalid choice. Please choose 'I' or 'F'.")
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
