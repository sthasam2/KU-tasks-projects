import re

# Grammars
grammar1: str = """
S -> X Y
X -> X x | y
Y -> z
"""

grammar2: str = """
E -> E - T | T
T -> T / F | F
F -> (E) | id
"""

grammar3: str = """
S -> x X | y
X -> x
"""


def left_recursion_removal(grammar: str) -> None:
    """
    Remove left recursion
    """

    grammar = grammar.strip()
    print("\nGrammar:")
    print(grammar)

    form_1 = re.split("\n", grammar)
    form_2 = [re.split(r"->|\|", _) for _ in form_1]
    form_3 = [[side.strip() for side in _] for _ in form_2]

    whole_flag = False

    for count, element in enumerate(form_3):
        flag = False
        recursive = []
        non_recursive = []

        for i in range(1, len(element)):
            if element[i].startswith(f"{element[0]} "):
                recursive.append(element[i][len(element[0]) :].strip())
                flag = True
                if not whole_flag:
                    whole_flag = True
            else:
                non_recursive.append(element[i])

        if flag:
            form_3[count] = form_3[count][:1]
            new_variable = element[0]
            repeat = True

            while repeat:
                if any(new_variable in _ for _ in form_3):
                    new_variable = f"{new_variable}'"
                else:
                    repeat = False

            for production in non_recursive:
                form_3[count].append(f"{production} {new_variable}")

            new = [f"{new_variable}"]
            new.extend(f"{production} {new_variable}" for production in recursive)
            new.append("ε")
            form_3.append(new)

    if whole_flag:
        print("\nThe grammar after removing left recursion is:")

        for element in form_3:
            joined = " | ".join(str(_) for _ in element[1:])
            print(f"{element[0]} -> {joined}")

    else:
        print("\nThe grammar is not left recursive.")


if __name__ == "__main__":
    for grammar in [grammar1, grammar2, grammar3]:
        left_recursion_removal(grammar)
        print("-" * 25)
