% Familiarization with Matrix
A = [1 5 7 11; 2 6 4 8; 2 0 4 4]; % 3 x 4 matrix
B = [1 2 4; 5 9 0; 2 8 9; 5 6 4]; % 4 * 3 matrix

disp('Matrix A:');
disp(A);
disp('Matrix B:');
disp(B);

% Matrix Operations
% Addition
disp("Addition: A + B");

try
    add = A + B;
    disp(add)
catch ME
    disp(ME)
end

% Subtractions
disp("Subrtraction: B - A");

try
    sub = B - A;
    disp(sub)
catch ME
    disp(ME)
end

% Multiplication

disp("Multiplication: A * B");

try
    mul = A * B;
    disp(mul)
catch ME
    disp(ME)
end

disp("Multiplication: B * A");

try
    mul = B * A;
    disp(mul)
catch ME
    disp(ME)
end

% Transpose
A_t = A.';
B_t = B.';

disp("Multiplication: transpose A * transpose B");

try
    mul = A_t * B_t;
    disp(mul)
catch ME
    disp(ME)
end
