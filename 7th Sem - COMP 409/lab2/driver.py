import sys
import time

from AutomataTheory import *


def main():
    inp = input("Enter regex. eg, ab*, (1+0)*\n")
    if len(sys.argv) > 1:
        inp = sys.argv[1]
    print("Regular Expression: ", inp)
    # regex -> NFA
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()
    # NFA -> DFA
    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()
    # DFA->min DFA
    minDFA = dfaObj.getMinimisedDFA()

    # DISPLAY
    print("\n\t\t###########\n\t\t   NFA\n\t\t###########")
    nfaObj.displayNFA()
    print("\n\t\t###########\n\t\t   DFA\n\t\t###########")
    dfaObj.displayDFA()
    print("\n\t\t#################\n\t\t  Minimized DFA\n\t\t#################")
    dfaObj.displayMinimisedDFA()

    if isInstalled("dot"):
        drawGraph(dfa, "dfa")
        drawGraph(nfa, "nfa")
        drawGraph(minDFA, "mdfa")
        print("\nGraphs have been created in the code directory using dot file")
        print(minDFA.getDotFile())

    
    for i in range(5):
        check_string = input("\nEnter a test string for the regex\n")
        isValid = dfaObj.acceptsString(check_string)
        print(f"The input string's validity = {isValid}")


if __name__ == "__main__":
    t = time.time()
    try:
        main()
    except BaseException as e:
        print("\nFailure:", e)
    print("\nExecution time: ", time.time() - t, "seconds")
