from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

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
    choice = input()
    text = input()
    mismatch = find_mismatch(text)
    if choice == "I":
        print(mismatch)
    else:
        print(mismatch)


if __name__ == "__main__":
    main()