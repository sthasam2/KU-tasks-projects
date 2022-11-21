# LL(1) parser code in python


def remove_left_recursion(rules_diction):
    """
    Remove left recursion by separating into alpha beta rules

    alphaRules stores subrules with left-recursion
    betaRules stores subrules without left-recursion

    Eg,
    for rule: A->Aa|b
    result: A->bA',A'->aA'|#
    """

    # 'store' has new rules to be added
    store = {}
    # traverse over rules
    for lhs in rules_diction:
        # alphaRules stores subrules with left-recursion
        # betaRules stores subrules without left-recursion
        alphaRules = []
        betaRules = []
        # get rhs for current lhs
        allrhs = rules_diction[lhs]
        for subrhs in allrhs:
            if subrhs[0] == lhs:
                alphaRules.append(subrhs[1:])
            else:
                betaRules.append(subrhs)
        # alpha and beta containing subrules are separated
        # now form two new rules
        if alphaRules:
            # to generate new unique symbol
            # add ' till unique not generated
            lhs_ = lhs + "'"
            while lhs_ in rules_diction.keys() or lhs_ in store:
                lhs_ += "'"
            # make beta rule
            for betaRule in betaRules:
                betaRule.append(lhs_)
            rules_diction[lhs] = betaRules
            # make alpha rule
            for alphaRule in alphaRules:
                alphaRule.append(lhs_)
            alphaRules.append(["#"])
            # store in temp dict, append to
            # - rules_diction at end of traversal
            store[lhs_] = alphaRules
    # add newly generated rules generated
    # - after removing left recursion
    for left in store:
        rules_diction[left] = store[left]

    return rules_diction


def left_factoring(rules_diction):
    """
    Perform Left factoring

    E.g,
    for rule: A->aDF|aCV|k
    result: A->aA'|k, A'->DF|CV
    """

    newDict = {}

    for lhs in rules_diction:
        # get rhs for given lhs
        allrhs = rules_diction[lhs]
        # temp dictionary helps detect left factoring
        temp = {}
        for subrhs in allrhs:
            if subrhs[0] not in list(temp.keys()):
                temp[subrhs[0]] = [subrhs]
            else:
                temp[subrhs[0]].append(subrhs)
        # if value list count for any key in temp is > 1,
        # - it has left factoring
        # new_rule stores new subrules for current LHS symbol
        new_rule = []
        # temp_dict stores new subrules for left factoring
        tempo_dict = {}
        for term_key, allStartingWithTermKey in temp.items():
            if len(allStartingWithTermKey) > 1:
                # left factoring required
                # to generate new unique symbol
                # - add ' till unique not generated
                lhs_ = lhs + "'"
                while lhs_ in rules_diction.keys() or lhs_ in tempo_dict:
                    lhs_ += "'"
                # append the left factored result
                new_rule.append([term_key, lhs_])
                # add expanded rules to tempo_dict
                ex_rules = [g[1:] for g in allStartingWithTermKey]
                tempo_dict[lhs_] = ex_rules
            else:
                # no left factoring required
                new_rule.append(allStartingWithTermKey[0])
        # add original rule
        newDict[lhs] = new_rule
        # add newly generated rules after left factoring
        for key in tempo_dict:
            newDict[key] = tempo_dict[key]
    return newDict


def compute_left_factoring():
    """
    Compute necessary items and then left factoring
    """
    global rules, non_terminals, terminals, diction

    for rule in rules:
        k = rule.split("->")
        # remove un-necessary spaces
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multirhs = rhs.split("|")
        # remove un-necessary spaces
        for i in range(len(multirhs)):
            multirhs[i] = multirhs[i].strip()
            multirhs[i] = multirhs[i].split()
        diction[k[0]] = multirhs

    # RULES
    display_map("\t\tRules", grammar_list_to_string(diction))

    # LEFT RECURSION
    diction = remove_left_recursion(diction)
    display_map("After elimination of left recursion", grammar_list_to_string(diction))

    # LEFT REFACTORING
    diction = left_factoring(diction)
    display_map("\tAfter left factoring", grammar_list_to_string(diction))


def grammar_list_to_string(map):
    """"""

    final = {}
    for key, val in map.items():
        string = ""
        for items in val:
            for item in items:
                string += f"{item} "
            string += " | " if items != val[-1] else ""
        final[key] = f"{string}"

    return final


def display_map(message, map):
    """"""
    print("\n")
    print("#" * 35)
    print(message)
    print("#" * 35)
    for key, val in map.items():
        print(key, " -> ", val)


#
# Main code
#
if __name__ == "__main__":

    rules = ["S -> k O A", "A -> a d | a B | a C", "C -> c", "B -> B a b | b B C | r"]
    non_terminals = ["A", "B", "C"]
    terminals = ["k", "O", "d", "a", "c", "b", "r"]

    diction = {}

    compute_left_factoring()
