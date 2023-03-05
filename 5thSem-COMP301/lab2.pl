/*
FACTS
*/

% Relationships
parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).


%  Gender

female(pam).
male(tom).
male(bob).
female(pat).
male(jim).
female(liz).
female(ann).


/*
RULES
*/

offspring(CHILD,PARENT):- 
    parent(PARENT, CHILD).

mother(PARENT,CHILD):- 
    parent(PARENT,CHILD), female(PARENT).

father(PARENT,CHILD):- 
    parent(PARENT,CHILD), male(PARENT).

grandparent(GRANDPARENT,CHILD):- 
    parent(GRANDPARENT,PARENT), 
    parent(PARENT,CHILD).

grandfather(GRANDPARENT,CHILD):- 
    grandparent(GRANDPARENT,CHILD), 
    male(GRANDPARENT).

grandmother(GRANDPARENT,CHILD):- 
    grandparent(GRANDPARENT,CHILD), 
    female(GRANDPARENT).

sibbling(CHILD1, CHILD2):- 
    parent(PARENT, CHILD1), 
    parent(PARENT, CHILD2), 
    CHILD1 @> CHILD2.

sister(CHILD1, CHILD2):- 
    sibbling(CHILD1, CHILD2), 
    female(CHILD1).

brother(CHILD1, CHILD2):- 
    sibbling(CHILD1, CHILD2), 
    male(CHILD1).

predecessor(PREDECESSOR,PERSON):- 
    parent(PREDECESSOR, PERSON); 
    parent(PARENT, PERSON), 
    predecessor(PREDECESSOR, PARENT).