%
% Lab 2
%

figure("Name", "Different discrete and continuous functions")
tiledlayout(3, 2);

xct = linspace(-5 * pi, 5 * pi, 500); % value range from -5pi to 5pi (for continuous)
xt = -10:10; % value range from -5 to 5 (for discrete)

% Sinusoidal Function
nexttile;
yct = 5 * sin(xct);
plot(xct, yct)
title('continuous sine wave with amp 5');
xticks([-5 * pi -3 * pi -pi 0 pi 3 * pi 5 * pi]); xticklabels({'-5\pi', '-3\pi', '-\pi', '0', '\pi', '3\pi', '5\pi'});
xlabel('time'); ylabel("value");

% Sinc function
nexttile;
yct = sin(xct) ./ xct; y2ct = sinc(xct);
plot(xct, yct); hold on; plot(xct, y2ct)
title('continuous sinc function');
xticks([-5 * pi -3 * pi -pi 0 pi 3 * pi 5 * pi]); xticklabels({'-5\pi', '-3\pi', '-\pi', '0', '\pi', '3\pi', '5\pi'});
xlabel('time'); ylabel("value");
legend('unnormalized', 'normalized')

% unit impulse
nexttile
unitimpluse = xt == 0;
stem(xt, unitimpluse);
xlabel('time'); ylabel("value");
title('Unit Impluse');

% unit impulse
nexttile
unitstep = xt >= 0;
stem(xt, unitstep);
xlabel('time'); ylabel("value");
title('Unit Step');

% unit ranp
nexttile
unitramp = unitstep .* xt;
stem(xt, unitramp);
xlabel('time'); ylabel("value");
title('Unit Ramp');

% exponentially growing
nexttile
ct = 0:20;
exp_growing = ct.^2;
plot(exp_growing)

hold on
ct = 20:-1:0;
exp_decaying = ct.^2;
plot(exp_decaying)

hold off
hold on
dc = zeros(1, 30);

for i = 1:30
    dc(i) = 60;
end

plot(dc)
hold off
title('continuous time (exp grow, exp decay, DC)');
legend('continuous time exponentially increasing', 'continuous time exponentially decaying', 'continuous time DC');
