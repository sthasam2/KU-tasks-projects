from os import popen

from tabulate import tabulate


class Automata:
    """class to represent an Automata"""

    def __init__(self, language=set(["0", "1"])):
        self.states = set()
        self.startstate = None
        self.finalstates = []
        self.transitions = dict()
        self.language = language

    @staticmethod
    def epsilon():
        return "ε"

    def set_from_state(self, state):
        """Creating the start state from a given state"""

        self.startstate = state
        self.states.add(state)

    def add_final_states(self, state):
        """Adding Final states"""

        if isinstance(state, int):  # check integer
            state = [state]
        for s in state:
            if s not in self.finalstates:
                self.finalstates.append(s)

    def add_transition(self, from_state, to_state, inp):
        """Creating transition from one state to another from-(inp)->to"""

        # check input is string i.e. for regex ab* itll check a, b is string
        if isinstance(inp, str):
            inp = set([inp])  # making set for ease
        # add states
        self.states.add(from_state)
        self.states.add(to_state)
        # check starting state in transitions
        if from_state in self.transitions:
            # check end state in transitions with start state
            if to_state in self.transitions[from_state]:
                # if exists union, eg 1->2 on a present, new transition is 1->2 on b, then it unions
                self.transitions[from_state][to_state] = self.transitions[from_state][
                    to_state
                ].union(inp)
            else:
                # if doesnt exist create new
                self.transitions[from_state][to_state] = inp
        else:
            # if starting state not in transitions create
            self.transitions[from_state] = {to_state: inp}

    def add_transition_dict(self, transitions):
        """Create a transition by making a dict i.e. {1:{0:{a,b}}}"""
        for from_state, to_states in transitions.items():
            for state in to_states:
                self.add_transition(from_state, state, to_states[state])

    def gettransitions(self, state, key):
        """
        Return transitions for a given state,
        eg, state 1 returns set of transitions {2,3}
            so using transitions[2] we get full transition
        """
        # check state is int
        if isinstance(state, int):
            state = [state]
        # create a set for storing transitions
        trstates = set()
        # iteratively finding end states of transitions
        for st in state:
            if st in self.transitions:
                for tns in self.transitions[st]:
                    if key in self.transitions[st][tns]:
                        trstates.add(tns)
        return trstates

    def getEClose(self, findstate):
        """
        Return states with ε closure transitions

        eg, 1-ε->2 then 1->2 ie {2}
        """
        allstates = set()  # set for storing all checked states
        states = set([findstate])  # set for storing states to iteratively check for ε
        while len(states) != 0:
            state = states.pop()
            allstates.add(state)
            # iteratively check for ε closure state and add it to all states
            if state in self.transitions:
                for tns in self.transitions[state]:
                    if (
                        Automata.epsilon() in self.transitions[state][tns]
                        and tns not in allstates
                    ):
                        states.add(tns)
        return allstates

    def display(self):
        """Display the Automata states, transitions"""

        data_to_display = [
            ["States", self.states],
            ["Start State", self.startstate],
            ["Final States", self.finalstates],
        ]
        transitions = ""
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                for char in to_states[state]:
                    transitions += f"{from_state}-({char})->{state}\n"
        data_to_display.append(["Transitions", transitions])
        print(tabulate(data_to_display, tablefmt="grid"))

    def newBuildFromNumber(self, startnum):
        """
        Build new from a given state,
        eg, 2 then build new state 3, 4 whatever
        """

        translations = {}
        for i in list(self.states):
            translations[i] = startnum
            startnum += 1
        rebuild = Automata(self.language)
        rebuild.set_from_state(translations[self.startstate])
        rebuild.add_final_states(translations[self.finalstates[0]])
        # build state {from_state}-({state})->{to_states} i.e 2-(a)->3
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                rebuild.add_transition(
                    translations[from_state], translations[state], to_states[state]
                )
        return [rebuild, startnum]

    def newBuildFromEquivalentStates(self, equivalent, pos):
        """
        Build new automata from old automata by comibining equivalent states
        eg, 1-(a)->2, 3-(a)->2 then {1,3}-(a)->2
        """

        rebuild = Automata(self.language)
        for from_state, to_states in self.transitions.items():
            for state in to_states:
                rebuild.add_transition(pos[from_state], pos[state], to_states[state])
        rebuild.set_from_state(pos[self.startstate])
        for s in self.finalstates:
            rebuild.add_final_states(pos[s])
        return rebuild

    def getDotFile(self):
        """Get the digraph information as a dot file"""

        dotFile = "digraph DFA {\nrankdir=LR\n"
        if len(self.states) != 0:
            dotFile += "root=s1\nstart [shape=point]\nstart->s%d\n" % self.startstate
            for state in self.states:
                if state in self.finalstates:
                    dotFile += "s%d [shape=doublecircle]\n" % state
                else:
                    dotFile += "s%d [shape=circle]\n" % state
            for from_state, to_states in self.transitions.items():
                for state in to_states:
                    for char in to_states[state]:
                        dotFile += 's%d->s%d [label="%s"]\n' % (
                            from_state,
                            state,
                            char,
                        )
        dotFile += "}"
        return dotFile


class BuildAutomata:
    """class for building e-nfa basic structures"""

    @staticmethod
    def basicstruct(inp):
        """Build basic structures like for ab => q1-a->q2-ε->q3-b->q4"""
        state1 = 1
        state2 = 2
        basic = Automata()
        basic.set_from_state(state1)
        basic.add_final_states(state2)
        basic.add_transition(1, 2, inp)
        return basic

    @staticmethod
    def plusstruct(a, b):
        """
        Build + operator structures like for (a+b)
        => q1-ε->q2-a->q3-ε->q6
           \_ε->q4-b->q5-ε--^
        """
        [a, m1] = a.newBuildFromNumber(2)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2
        plus = Automata()
        plus.set_from_state(state1)
        plus.add_final_states(state2)
        plus.add_transition(plus.startstate, a.startstate, Automata.epsilon())
        plus.add_transition(plus.startstate, b.startstate, Automata.epsilon())
        plus.add_transition(a.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.add_transition(b.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.add_transition_dict(a.transitions)
        plus.add_transition_dict(b.transitions)
        return plus

    @staticmethod
    def dotstruct(a, b):
        """Build . operator structures like for a."""
        [a, m1] = a.newBuildFromNumber(1)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2 - 1
        dot = Automata()
        dot.set_from_state(state1)
        dot.add_final_states(state2)
        dot.add_transition(a.finalstates[0], b.startstate, Automata.epsilon())
        dot.add_transition_dict(a.transitions)
        dot.add_transition_dict(b.transitions)
        return dot

    @staticmethod
    def starstruct(a):
        """
        Build * structures like for ab*
                        |---------ε------v
        => q1-ε->q2-a->q3-ε->q4-b->q5-ε->q6
                              ^_ε_/
        """
        [a, m1] = a.newBuildFromNumber(2)
        state1 = 1
        state2 = m1
        star = Automata()
        star.set_from_state(state1)
        star.add_final_states(state2)
        star.add_transition(star.startstate, a.startstate, Automata.epsilon())
        star.add_transition(star.startstate, star.finalstates[0], Automata.epsilon())
        star.add_transition(a.finalstates[0], star.finalstates[0], Automata.epsilon())
        star.add_transition(a.finalstates[0], a.startstate, Automata.epsilon())
        star.add_transition_dict(a.transitions)
        return star


class DFAfromNFA:
    """class for building dfa from e-nfa and minimise it"""

    def __init__(self, nfa):
        self.buildDFA(nfa)
        self.minimise()

    def getDFA(self):
        """Get DFA"""
        return self.dfa

    def getMinimisedDFA(self):
        """Get DFA after minimizing"""
        return self.minDFA

    def displayDFA(self):
        """Display the DFA in table"""
        self.dfa.display()

    def displayMinimisedDFA(self):
        """Display minimized DFA"""
        self.minDFA.display()

    def buildDFA(self, nfa):
        """
        Build DFA from NFA

        see theory from https://www.javatpoint.com/automata-conversion-from-nfa-to-dfa
        """
        allstates = dict()
        eclose = dict()
        count = 1  # for tracking state count starting from 1
        state1 = nfa.getEClose(nfa.startstate)  # a-ε->b then get a->b
        eclose[nfa.startstate] = state1

        dfa = Automata(nfa.language)  # initialize
        dfa.set_from_state(count)  # get start state
        states = [[state1, count]]
        allstates[count] = state1
        count += 1
        while len(states) != 0:
            [state, fromindex] = states.pop()
            for char in dfa.language:
                trstates = nfa.gettransitions(state, char)
                for s in list(trstates)[:]:
                    if s not in eclose:
                        eclose[s] = nfa.getEClose(s)
                    trstates = trstates.union(eclose[s])
                if len(trstates) != 0:
                    if trstates not in allstates.values():
                        states.append([trstates, count])
                        allstates[count] = trstates
                        toindex = count
                        count += 1
                    else:
                        toindex = [k for k, v in allstates.items() if v == trstates][0]
                    dfa.add_transition(fromindex, toindex, char)
        for value, state in allstates.items():
            if nfa.finalstates[0] in state:
                dfa.add_final_states(value)
        self.dfa = dfa

    def acceptsString(self, string):
        """Check if string valid by going passing through states"""

        currentstate = self.dfa.startstate
        for ch in string:
            if ch == "ε":
                continue
            st = list(self.dfa.gettransitions(currentstate, ch))
            if len(st) == 0:
                return False
            currentstate = st[0]
        if currentstate in self.dfa.finalstates:
            return True
        return False

    def minimise(self):
        """
        Minimize a DFA

        see for theory,
        https://www.geeksforgeeks.org/minimization-of-dfa/
        """
        states = list(self.dfa.states)
        n = len(states)
        unchecked = dict()
        count = 1  # keeping tract of number of states
        distinguished = []
        equivalent = dict(zip(range(len(states)), [{s} for s in states]))
        pos = dict(zip(states, range(len(states))))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not (
                    [states[i], states[j]] in distinguished
                    or [states[j], states[i]] in distinguished
                ):
                    eq = 1
                    toappend = []
                    for char in self.dfa.language:
                        s1 = self.dfa.gettransitions(states[i], char)
                        s2 = self.dfa.gettransitions(states[j], char)
                        if len(s1) != len(s2):
                            eq = 0
                            break
                        if len(s1) > 1:
                            raise BaseException("Multiple transitions detected in DFA")
                        elif len(s1) == 0:
                            continue
                        s1 = s1.pop()
                        s2 = s2.pop()
                        if s1 != s2:
                            if [s1, s2] in distinguished or [s2, s1] in distinguished:
                                eq = 0
                                break
                            else:
                                toappend.append([s1, s2, char])
                                eq = -1
                    if eq == 0:
                        distinguished.append([states[i], states[j]])
                    elif eq == -1:
                        s = [states[i], states[j]]
                        s.extend(toappend)
                        unchecked[count] = s
                        count += 1
                    else:
                        p1 = pos[states[i]]
                        p2 = pos[states[j]]
                        if p1 != p2:
                            st = equivalent.pop(p2)
                            for s in st:
                                pos[s] = p1
                            equivalent[p1] = equivalent[p1].union(st)
        newFound = True
        checked = dict()
        while newFound and len(unchecked) > 0:
            newFound = False
            toremove = set()
            for p, pair in unchecked.copy().items():
                for tr in pair[2:]:
                    if [tr[0], tr[1]] in distinguished or [
                        tr[1],
                        tr[0],
                    ] in distinguished:
                        unchecked.pop(p)
                        distinguished.append([pair[0], pair[1]])
                        newFound = True
                        break
        for pair in unchecked.values():
            p1 = pos[pair[0]]
            p2 = pos[pair[1]]
            if p1 != p2:
                st = equivalent.pop(p2)
                for s in st:
                    pos[s] = p1
                equivalent[p1] = equivalent[p1].union(st)
        if len(equivalent) == len(states):
            self.minDFA = self.dfa
        else:
            self.minDFA = self.dfa.newBuildFromEquivalentStates(equivalent, pos)


class NFAfromRegex:
    """
    class for building e-nfa from regular expressions
    """

    def __init__(self, regex):
        self.star = "*"
        self.plus = "+"
        self.dot = "."
        self.openingBracket = "("
        self.closingBracket = ")"
        self.operators = [self.plus, self.dot]
        self.regex = regex
        self.alphabet = [chr(i) for i in range(65, 91)]
        self.alphabet.extend([chr(i) for i in range(97, 123)])
        self.alphabet.extend([chr(i) for i in range(48, 58)])
        self.buildNFA()

    def getNFA(self):
        return self.nfa

    def displayNFA(self):
        self.nfa.display()

    def buildNFA(self):
        """
        Build NFA from regex

        See theory from
        https://www.tutorialspoint.com/what-is-the-conversion-of-a-regular-expression-to-finite-automata-nfa
        """

        language = set()
        self.stack = []
        self.automata = []
        previous = "ε"
        # extract each character and build eNFA considering operators
        for char in self.regex:
            # for alphanumeric char
            if char in self.alphabet:
                language.add(char)
                if previous != self.dot and (
                    previous in self.alphabet
                    or previous in [self.closingBracket, self.star]
                ):
                    self.addOperatorToStack(self.dot)
                self.automata.append(BuildAutomata.basicstruct(char))
            # for start of group
            elif char == self.openingBracket:
                if previous != self.dot and (
                    previous in self.alphabet
                    or previous in [self.closingBracket, self.star]
                ):
                    self.addOperatorToStack(self.dot)
                self.stack.append(char)
            # for end of group
            elif char == self.closingBracket:
                if previous in self.operators:
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous)
                    )
                while 1:
                    if len(self.stack) == 0:
                        raise BaseException("Error processing '%s'. Empty stack" % char)
                    o = self.stack.pop()
                    if o == self.openingBracket:
                        break
                    elif o in self.operators:
                        self.processOperator(o)
            # for * operation
            elif char == self.star:
                if (
                    previous in self.operators
                    or previous == self.openingBracket
                    or previous == self.star
                ):
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous)
                    )
                self.processOperator(char)
            # for + and .
            elif char in self.operators:
                if previous in self.operators or previous == self.openingBracket:
                    raise BaseException(
                        "Error processing '%s' after '%s'" % (char, previous)
                    )
                else:
                    self.addOperatorToStack(char)
            # for invalid characters
            else:
                raise BaseException("Symbol '%s' is not allowed" % char)
            previous = char
        while len(self.stack) != 0:
            op = self.stack.pop()
            self.processOperator(op)
        if len(self.automata) > 1:
            print(self.automata)
            raise BaseException("Regex could not be parsed successfully")
        self.nfa = self.automata.pop()
        self.nfa.language = language

    def addOperatorToStack(self, char):
        """Adding operator to stack"""
        while 1:
            if len(self.stack) == 0:
                break
            top = self.stack[len(self.stack) - 1]
            if top == self.openingBracket:
                break
            if top == char or top == self.dot:
                op = self.stack.pop()
                self.processOperator(op)
            else:
                break
        self.stack.append(char)

    def processOperator(self, operator):
        """Process the operator"""
        if len(self.automata) == 0:
            raise BaseException(
                "Error processing operator '%s'. Stack is empty" % operator
            )
        if operator == self.star:
            a = self.automata.pop()
            self.automata.append(BuildAutomata.starstruct(a))
        elif operator in self.operators:
            if len(self.automata) < 2:
                raise BaseException(
                    "Error processing operator '%s'. Inadequate operands" % operator
                )
            a = self.automata.pop()
            b = self.automata.pop()
            if operator == self.plus:
                self.automata.append(BuildAutomata.plusstruct(b, a))
            elif operator == self.dot:
                self.automata.append(BuildAutomata.dotstruct(b, a))


def drawGraph(automata, file=""):
    """
    Draw graphs from dot file

    From https://github.com/max99x/automata-editor/blob/master/util.py
    """
    f = popen(r"dot -Tpng -o graph-%s.png" % file, "w")
    try:
        f.write(automata.getDotFile())
    except:
        raise BaseException("Error creating graph")
    finally:
        f.close()


def isInstalled(program):
    """
    Check progarm installed or not

    From http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
    """

    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program) or is_exe(program + ".exe"):
            return True
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file) or is_exe(exe_file + ".exe"):
                return True
    return False
