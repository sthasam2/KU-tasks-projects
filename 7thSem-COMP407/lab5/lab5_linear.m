%
% LINEAR CONVOLUTION
%

clc; clearvars; close all;

% x[n]; x[n]_time range; h[n]; h[n]_time range;
xn1 = [1 1 1]; tx1 = -1:1; hn1 = [1 1 1]; th1 = -1:1;
xn2 = [0 1 2 3 4]; tx2 = 0:4; hn2 = [0 2 3 4 5]; th2 = 0:4; % x[n], loer time, upper time, h[n], lower t, upper t

q1 = linearCon(xn1, tx1, hn1, th1);
q2 = linearCon(xn2, tx2, hn2, th2);

%
% Plot
%

tiledlayout(6, 2)

% q1
nexttile;
stem(tx1, xn1, 'filled');
title({'System Input Sequence{x[n]}'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(th1, hn1, 'filled');
title({'Impulse Input Sequence {h[n]}'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

nexttile([2, 2]);
stem(q1(1, :), q1(2, :), 'filled');
title({'Output Sequence x[n]*h[n]'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

% q2
nexttile;
stem(tx2, xn2, 'filled', 'r');
title({'System Input Sequence {x[n]}'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(th2, hn2, 'filled', 'r');
title({'Impulse Input Sequence {h[n]}'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

nexttile([2, 2]);
stem(q2(1, :), q2(2, :), 'filled', 'r');
title({'Output Sequence x[n]*h[n]'}, 'Interpreter', 'latex');
xlabel('time'); ylabel("amplitude");

%
% Function
%

function result = linearCon(xn, tx, hn, th)

    xl = tx(1, 1); xu = tx(1, length(tx));
    hl = th(1, 1); hu = th(1, length(th));

    m = length(xn);
    n = length(hn);

    % output sequence
    t_o = xl + hl:1:xu + hu; % output sequence time limit

    % Linear convolution calculation
    X = [xn, zeros(1, n)]; % padding xn; [1 1 1] to [1 1 1 0 0 0] by adding 0
    H = [hn, zeros(1, m)]; % padding hn

    for i = 1:n + m - 1
        Y(i) = 0; % output

        for j = 1:m

            if ((i - j + 1) > 0)
                Y(i) = Y(i) + (X(j) * H(i - j + 1));
            else
            end

        end

    end

    result = [t_o; Y];

end
