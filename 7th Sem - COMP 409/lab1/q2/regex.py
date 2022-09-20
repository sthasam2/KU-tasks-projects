def is_start(char):
    """checks for start of regex pattern"""
    return char == "^"


def is_end(char):
    """checks for end of regex pattern"""
    return char == "$"


def is_star(char):
    """checks for * which match any 0 or more of the previous"""
    return char == "*"


def is_plus(char):
    """checks for + which matches 1 or more of the previous"""
    return char == "+"


def is_question(char):
    """checks for + which matches 0 or 1 of the previous"""
    return char == "?"


def is_operator(char):
    """checks for whether character is operator"""
    return is_star(char) or is_plus(char) or is_question(char)


def is_dot(char):
    """checks for . i.e. wildcard which matches any character, except newline (\n)"""
    return char == "."


def is_escape_sequence(term):
    """checks for escape sequences like (\n)"""
    return is_escape(term[0])


def is_escape(char):
    """checks for \ which is used for escaping a special character"""
    return char == "\\"


def is_open_alternate(char):
    """checks for ( used for denoting start of a group of characters"""
    return char == "("


def is_close_alternate(char):
    """checks for ) used for denoting end of a group of characters"""
    return char == ")"


def is_open_set(char):
    """checks for [ used for denoting start of a range of characters"""
    return char == "["


def is_close_set(char):
    """checks for ] used for denoting end of a range of characters"""
    return char == "]"


def is_literal(char):
    """checks for letters, digits and some special characters"""
    return char.isalpha() or char.isdigit() or char in "_:/"


def is_alternate(term):
    """checks for a grouping of characters like (xyz)"""
    return is_open_alternate(term[0]) and is_close_alternate(term[-1])


def is_set(term):
    """checks for a range of characters like [xyz]"""
    return is_open_set(term[0]) and is_close_set(term[-1])


def is_unit(term):
    """checks for units i.e patterns like .(dot), a(literal), [a-b](set), \\b(escape sequence)"""
    return (
        is_literal(term[0])
        or is_dot(term[0])
        or is_set(term)
        or is_escape_sequence(term)
    )


def split_alternate(alternate):
    """splits pattern of alternative into individual terms for eg (a|b) splits into a, b"""
    return alternate[1:-1].split("|")


def split_set(set_head):
    """"""
    set_inside = set_head[1:-1]
    set_terms = list(set_inside)
    return set_terms


def split_expr(expr):
    """
    Split expression to head, operator, and rest

    Eg, abc -> (a, None, bc) which is (head, operator, None)
    Eg, [123]bc -> ([123], None, bc)
    Eg, [123]* -> ([123], *, None)
    """
    head = None
    operator = None
    rest = None
    last_expr_pos = 0

    # for open set []
    if is_open_set(expr[0]):
        last_expr_pos = expr.find("]") + 1
        head = expr[:last_expr_pos]

    # for open alternate ()
    elif is_open_alternate(expr[0]):
        last_expr_pos = expr.find(")") + 1
        head = expr[:last_expr_pos]

    # for escape character \\a
    elif is_escape(expr[0]):
        last_expr_pos += 2
        head = expr[:2]

    # for others eg. abc
    else:
        last_expr_pos = 1
        head = expr[0]

    # after head assigned, extracting operator if present from rest of the expression
    if last_expr_pos < len(expr) and is_operator(expr[last_expr_pos]):
        operator = expr[last_expr_pos]
        last_expr_pos += 1

    # assigning rest
    rest = expr[last_expr_pos:]

    return head, operator, rest


def does_unit_match(expr, string):
    """
    check whether a unit matches

    For eg, reg->\\a , string-> abc it matches as \\a is for aplhabet characters and string is alphabet
    """
    head, operator, rest = split_expr(expr)

    # eg,  reg a == null
    if len(string) == 0:
        return False

    # eg, reg a == string a
    if is_literal(head):
        return expr[0] == string[0]

    # eg, reg . == string w, . means doesnt care
    elif is_dot(head):
        return True

    # eg, reg \\a == string abc
    elif is_escape_sequence(head):
        # for aplhabet characters
        if head == "\\a":
            return string[0].isalpha()

        elif head == "\\d":
            return string[0].isdigit()

        else:
            return False

    # eg, reg [abc] string z, checks if z is in [a,b,c]
    elif is_set(head):
        set_terms = split_set(head)
        return string[0] in set_terms

    return False


def match_multiple(
    expr, string, match_length, min_match_length=None, max_match_length=None
):
    """Matching multiple instances

    Params
    ------
    expr - str
        the given regex

    string - str
        the inputted string

    match_length - int
        the length of string to match

    min_match_length - int
        minimum number of string to be match

    max_match_length - int
        maximum number of string to be matched
    """

    #  get head, operator, rest from expression
    head, operator, rest = split_expr(expr)

    # defining minimum match, for eg, if * then minimum is 0 so possible min is 0
    if not min_match_length:
        min_match_length = 0

    # for storing the length of expansion, ie if expanded once b*-> bb*, this incremented by 1
    submatch_length = -1

    # expand until max_match_length is obtained or until sub_match_length is less than max (done for *)
    # so if max =5; ab*c then b* will only expand until bbbbb max 5
    # here we expand only the regex expresion for match
    while not max_match_length or (submatch_length < max_match_length):
        [subexpr_matched, subexpr_length] = match_expr(
            (head * (submatch_length + 1)), string, match_length
        )
        # increment until matched ie condition is met
        if subexpr_matched:
            submatch_length += 1
        else:
            break

    # expand until min_match_length is obtained when submatch_length is obtained from above (done for + operator)
    # so if min =2; b* will only expand until bb min
    # here we expand the actual string to be matched and add the remaing
    # ie. min = 2, ab*c then abbc
    # loops until minumum ie + criteria is satisfied
    while submatch_length >= min_match_length:
        [matched, new_match_length] = match_expr(
            (head * submatch_length) + rest, string, match_length
        )
        if matched:
            return (matched, new_match_length)
        submatch_length -= 1

    return (False, None)


def match_star(expr, string, match_length):
    """Match operation of star ie 0 or multiple instances of pprevious term for eg ab* equivalent abbbbb"""
    return match_multiple(expr, string, match_length, None, None)


def match_plus(expr, string, match_length):
    """Match operation of plus ie 1 or multiple instances of pprevious term for eg ab* equivalent abbbbb"""
    return match_multiple(expr, string, match_length, 1, None)


def match_question(expr, string, match_length):
    """Match operation of star ie 0 or 1 instances of pprevious term for eg ab* equivalent abbbbb"""
    return match_multiple(expr, string, match_length, 0, 1)


def match_alternate(expr, string, match_length):
    """
    Match with alternates

    for eg, a(c|d)b and string acb, then matches c with (c|d)
    """
    head, operator, rest = split_expr(expr)
    options = split_alternate(head)

    # checks all available options for matching with regex
    # ie if (c|d) it checks for matching of c and d in the string
    for option in options:
        [matched, new_match_length] = match_expr(option + rest, string, match_length)
        if matched:
            return (matched, new_match_length)

    return (False, None)


def match_expr(expr, string, match_length=0):
    """
    Check whether it is matched, if matched it gives the postion from which matched and length of matched

    For eg, expr->abc, string-> hello abc, it returns (True, 6, 3) ie (matched, position of first match, length of match)
    """
    # if no regex character left for matching
    if len(expr) == 0:
        return (True, match_length)

    # if end of string reached i.e $
    elif is_end(expr[0]):
        # when there is no string left to match
        if len(string) == 0:
            return (True, match_length)
        else:
            return (False, None)

    head, operator, rest = split_expr(expr)

    # check match for *
    if is_star(operator):
        return match_star(expr, string, match_length)
    # check match for +
    elif is_plus(operator):
        return match_plus(expr, string, match_length)
    # check match for ?
    elif is_question(operator):
        return match_question(expr, string, match_length)
    # check match for (|)
    elif is_alternate(head):
        return match_alternate(expr, string, match_length)
    # check match for single character a, b, c etc
    elif is_unit(head):
        if does_unit_match(expr, string):
            return match_expr(rest, string[1:], match_length + 1)
    else:
        print(f"Unknown token in expr {expr}.")

    return (False, None)


def match(expr, string):
    "Match expresion with string"

    match_pos = 0
    matched = False

    # check for ^
    if is_start(expr[0]):
        max_match_pos = 0
        expr = expr[1:]
    # define maximum characteres that can be matched if expr abc then 2
    else:
        max_match_pos = len(string) - 1

    # loop until matching expression is found or end of string
    while not matched and match_pos <= max_match_pos:
        [matched, match_length] = match_expr(expr, string[match_pos:])
        if matched:
            return (matched, match_pos, match_length)
        match_pos += 1

    return (False, None, None)


def main():
    # match a website
    expr = "^http://(\\a|\\d)+.(com|net|org)"
    string = "http://sthasambeg.com.np"
    [matched, match_pos, match_length] = match(expr, string)
    if matched:
        print(
            f"Regex =>{expr}\nString=>{string}\nPortion matched=>{string[match_pos:match_pos + match_length]}\nValid={matched}"
        )
    else:
        print(f"Regex =>{expr}\nString=>{string}\nValid={matched}")

    print(f"\n")

    expr = "c*d*"
    string = "cccccccddddd"
    [matched, match_pos, match_length] = match(expr, string)
    if matched:
        print(f"Regex =>{expr}\nString=>{string}\nValid={matched}")
    else:
        print(f"Regex =>{expr}\nString=>{string}\nValid={matched}")

    print(f"\n")

    expr = "ab*"
    string = "c"
    [matched, match_pos, match_length] = match(expr, string)
    if matched:
        print(f"Regex =>{expr}\nString=>{string}\nValid={matched}")
    else:
        print(f"Regex =>{expr}\nString=>{string}\nValid={matched}")


if __name__ == "__main__":
    main()
