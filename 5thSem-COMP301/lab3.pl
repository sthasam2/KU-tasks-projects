/*
# Arithmetic operators in Prolog-lang
*/

/*

Arithmetic operators available in Prolog

A + B                                    sum of A and B   
A - B                                    difference of A and B   
A * B                                    product of A and B   
A / B                                    quotient of A and B   
A // B                                  'Integer quotient' of A and B   
A ^ B                                    A to the power of B   
- A                                      negative of A  
sin(A)                                   sine of A  
cos(A)                                   cosine of A  
abs(A)                                   absolute value of A  
sqrt(A)                                  square root of A  
max(A, B)                                larger of A and B 

*/

/* 
## QUERIES


GNU Prolog 1.4.5 (64 bits)
Compiled Feb 23 2020, 20:14:50 with gcc
By Daniel Diaz
Copyright (C) 1999-2020 Daniel Diaz
| ?- A is 69, B is 420, C is A+B.

A = 69
B = 420
C = 489

yes
| ?- A is 420, B is 69, C is A-B.

A = 420
B = 69
C = 351

yes
| ?- A is 007, B is 18, C is A*B.

A = 7
B = 18
C = 126

yes
| ?- A is 007, B is 126, C is B/A.

A = 7
B = 126
C = 18.0

yes

*/


% fibonacci_first_second_end([],_X,_Y,0):-
% fibonacci_first_second_end([X|As],X,Y,End):-
%     C>0,
%     X is 