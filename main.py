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
    choice = input("Choose between using input or test files: 'I' for input or 'F' for test files: ")
    if choice == 'I':
        text = input("Enter a sequence of brackets: ")
        mismatch = find_mismatch(text)
        print(mismatch)
    elif choice == 'F':
        test_files = ["test/0.a", "test/1.a", "test/2.a", "test/3.a", "test/4.a", "test/5.a"]
        for test_file in test_files:
            with open(test_file + "") as f:
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


if __name__ == "__main__":
    main()