%
% Lab 4
% Author: Sambeg Shrestha
%

clc; clearvars; close all;

syms x;

%
% Even
%
y1 = rectangularPulse(x); %odd signal
a0_1 = find_a0(y1);
sum1 = fourierExpansion(y1);

%
% Odd
%
y2 = x^3; %odd signal
a0_2 = find_a0(y2);
sum2 = fourierExpansion(y2);

%
% plot
%

subplot(2, 1, 1)
fplot(x, y1, [-pi, pi], 'Linewidth', 1.5); %plot the original signa
grid on; hold on;
%plot the fourier expansion
fplot(x, (sum1 + a0_1 / 2) + 0.3, [-pi, pi], 'Color', 'r', 'Linewidth', 1);
legend('Even Signal', 'Fourier Series');

subplot(2, 1, 2)
fplot(x, y2, [-pi, pi], 'Color', 'g', 'Linewidth', 1.5); %plot the original signa
grid on; hold on;
%plot the fourier expansion
fplot(x, (sum2 + a0_2 / 2) + 0.3, [-pi, pi], 'Color', 'm', 'Linewidth', 1);
legend('Odd Signal', 'Fourier Series');

%
% Function
%

function sum = fourierExpansion(y)
    syms x;
    sum = 0;

    for n = 1:20
        an = (1 / pi) * int(y * cos(n * x), x, -pi, pi);
        bn = (1 / pi) * int(y * sin(n * x), x, -pi, pi);
        sum = sum + (an * cos(n * x) + bn * sin(n * x));
    end

end

function a0 = find_a0(y)
    syms x;
    a0 = (1 / pi) * (int(y, x, -pi, pi));

end
