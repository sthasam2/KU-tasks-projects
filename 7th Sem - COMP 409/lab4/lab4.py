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


# calculation of first
# epsilon is denoted by '#' (semi-colon)

# pass rule in first function
def first(rule):
    global rules, nonterm_userdef, term_userdef, diction, firsts
    if len(rule) != 0:
        if rule is not None:
            if rule[0] in term_userdef:
                return rule[0]
            elif rule[0] == "#":
                return "#"

        if rule[0] in list(diction.keys()):
            # fres temporary list of result
            fres = []
            rhs_rules = diction[rule[0]]
            # call first on each rule of RHS
            # fetched (& take union)
            for itr in rhs_rules:
                indivRes = first(itr)
                if type(indivRes) is list:
                    fres.extend(iter(indivRes))
                else:
                    fres.append(indivRes)

            # if no epsilon in result
            # - received return fres
            if "#" in fres:
                # apply epsilon
                # rule => f(ABC)=f(A)-{e} U f(BC)
                newList = []
                fres.remove("#")
                if len(rule) > 1:
                    ansNew = first(rule[1:])
                    if ansNew is None:
                        return fres
                    else:
                        return (
                            fres + ansNew if type(ansNew) is list else fres + [ansNew]
                        )
                # if result is not already returned
                # - control reaches here
                # lastly if eplison still persists
                # - keep it in result of first
                fres.append("#")
            return fres


def follow(nt):
    """
    calculation of follow

    uses 'rules' list, and 'diction' dict from above

    follow function input is the split result on
    - Non-Terminal whose Follow we want to compute
    """

    global start_symbol, rules, nonterm_userdef, term_userdef, diction, firsts, follows
    # for start symbol return $ (recursion base case)

    solset = set()
    if nt == start_symbol:
        # return '$'
        solset.add("$")

    # check all occurrences
    # solset - is result of computed 'follow' so far

    # For input, check in all rules
    for curNT in diction:
        rhs = diction[curNT]
        # go for all productions of NT
        for subrule in rhs:
            if nt in subrule:
                # call for all occurrences on
                # - non-terminal in subrule
                while nt in subrule:
                    index_nt = subrule.index(nt)
                    subrule = subrule[index_nt + 1 :]
                    # empty condition - call follow on LHS
                    if len(subrule) != 0:
                        # compute first if symbols on
                        # - RHS of target Non-Terminal exists
                        res = first(subrule)
                        # if epsilon in result apply rule
                        # - (A->aBX)- follow of -
                        # - follow(B)=(first(X)-{ep}) U follow(A)
                        if "#" in res:
                            res.remove("#")
                            ansNew = follow(curNT)
                            newList = []
                            if ansNew is None:
                                newList = res
                            else:
                                newList = (
                                    res + ansNew
                                    if type(ansNew) is list
                                    else res + [ansNew]
                                )
                            res = newList
                    elif nt != curNT:
                        res = follow(curNT)

                    # add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)


def computeAllFirsts():
    """
    Calculate all Firsts
    """
    global rules, nonterm_userdef, term_userdef, diction, firsts
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

    print("\n")
    print("#" * 35)
    print("\tRules")
    print("#" * 35)

    for y in diction:
        print(f"{y}->{diction[y]}")

    print("\n")
    print("#" * 35)
    print("After elimination of left recursion")
    print("#" * 35)

    diction = remove_left_recursion(diction)
    for y in diction:
        print(f"{y}->{diction[y]}")

    print("\n")
    print("#" * 35)
    print("\tAfter left factoring")
    print("#" * 35)

    diction = left_factoring(diction)
    for y in diction:
        print(f"{y}->{diction[y]}")

    # calculate first for each rule
    # - (call first() on all RHS)
    for y in list(diction.keys()):
        t = set()
        for sub in diction.get(y):
            res = first(sub)
            if res != None:
                if type(res) is list:
                    for u in res:
                        t.add(u)
                else:
                    t.add(res)

        # save result in 'firsts' list
        firsts[y] = t

    print("\n")
    print("#" * 35)
    print("\tCalculated firsts")
    print("#" * 35)

    key_list = list(firsts.keys())
    for index, gg in enumerate(firsts):
        print(f"first({key_list[index]}) " f"=> {firsts.get(gg)}")


def computeAllFollows():
    """
    Calculate Follows
    """
    global start_symbol, rules, nonterm_userdef, term_userdef, diction, firsts, follows
    for NT in diction:
        solset = set()
        sol = follow(NT)
        if sol is not None:
            for g in sol:
                solset.add(g)
        follows[NT] = solset

    print("\n")
    print("#" * 35)
    print("\tCalculated follows")
    print("#" * 35)

    key_list = list(follows.keys())
    for index, gg in enumerate(follows):
        print(f"follow({key_list[index]})" f" => {follows[gg]}")


#
# Main code
#
if __name__ == "__main__":
    sample_input_string = None

    rules = ["S -> A k O", "A -> A d | a B | a C", "C -> c", "B -> b B C | r"]
    nonterm_userdef = ["A", "B", "C"]
    term_userdef = ["k", "O", "d", "a", "c", "b", "r"]
    sample_input_string = "a r k O"

    diction = {}
    firsts = {}
    follows = {}

    computeAllFirsts()
    start_symbol = list(diction.keys())[0]
    computeAllFollows()
