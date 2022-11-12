%
% Circular Convolution
%

% input sequences

x1 = [1 2 2 0];
x2 = [1 2 3 4];

l = length(x1);
m = length(x2);

x1pad = [x1 zeros(1, m - 1)]; % padding 0 values
x2pad = [x2 zeros(1, l - 1)];

% Calculating convolutions
clin = conv(x1, x2);
ccirc = cconv(x1pad, x2pad);

%
% Plot
%

tiledlayout(5, 2)

nexttile;
stem(x1, 'filled');
title('System Input Sequence x1 ');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(x2, 'filled');
title('Impulse Input Sequence x2');
xlabel('time'); ylabel("amplitude");

nexttile([2, 2]);
stem(clin, 'filled', 'm');
title('Linear convolution x1*x2');
xlabel('time'); ylabel("amplitude");

nexttile([2, 2]);
stem(ccirc, 'filled', 'r');
title('Circular convolution x1*x2');
xlabel('time'); ylabel("amplitude");
