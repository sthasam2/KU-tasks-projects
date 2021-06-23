% # Lists

/*
MEMBERSHIP
*/
list_member(X, [X|_]).

list_member(X, [_|Tail]):-
    list_member(X, Tail).

%  query 
% list_member(c, [a,b,c,d,e]).

/*
LENGTH
*/
list_length([],0).

list_length([_|Tail], N):-
    list_length(Tail, N_1),
    N is N_1 + 1.

%  query
% list_length([1,2,4,6,8,9],N).

/*
CONCATENATION
*/
concat([],List, List).

concat([Head|Tail], List, [Head|Rest]):-
    concat(Tail, List, Rest).

% query
% concat([1,2,3],[a,b,c], Result).