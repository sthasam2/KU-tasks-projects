%
% lab3
%

f = 2e3; % frequency
T = 1 / f; % time period
dF = 1e6; % minimum freq for continuous

%
% FUNCTIONS
%

t_range = @(sampF, cycles) 0:1 / sampF:T * cycles; % time range
sig1 = @(freq, sampF, times) 5 * sin(2 * pi * freq * times); % signal 1
sig2 = @(freq, sampF, times) 5 * cos(2 * pi * freq * times); % signal 2

% q1
% time ranges used for calculating signals
ct5Cyc = t_range(dF, 5);
s1s1T = t_range(5e3, 5); % discrete time ranges for 5KHz 5 cycles
s1s2T = t_range(10e3, 5); % discrete time ranges for 10KHz 5 cycles
s1s3T = t_range(20e3, 5); % discrete time ranges for 20KHz 5 cycles

% signals
signal1 = sig1(f, dF, ct5Cyc);
s1s1 = sig1(f, 5e3, t_range(5e3, 5)); % signal 1 sample 1
s1s2 = sig1(f, 5e3, t_range(10e3, 5));
s1s3 = sig1(f, 5e3, t_range(20e3, 5));

% q2
% time ranges used for calculating signals
ct3Cyc = t_range(dF, 3);
s2s1T = t_range(5e3, 3); % discrete time ranges for 5KHz 3 cycles
s2s2T = t_range(10e3, 3); % discrete time ranges for 10KHz 3 cycles
s2s3T = t_range(20e3, 3); % discrete time ranges for 20KHz 3 cycles

signal2 = sig2(f, dF, ct3Cyc);
s2s1 = sig2(f, 5e3, s2s1T);
s2s2 = sig2(f, 5e3, s2s2T);
s2s3 = sig2(f, 5e3, s2s3T);

%
% Plot
%
tiledlayout(4, 2)

% % q1

nexttile;
plot(ct5Cyc, signal1);
title('5sin(2\pi ft)', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s1s1T, s1s1);
title('5sin(2\pi ft) | 5HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s1s2T, s1s2);
title('5sin(2\pi ft) | 10HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s1s3T, s1s3);
title('5sin(2\pift) | 20HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

% q2

nexttile;
plot(ct3Cyc, signal2, 'Color', 'red');
title('5cos(2\pi ft)', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s2s1T, s2s1, 'Color', 'red');
title('5cos(2\pi ft) | 5HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s2s2T, s2s2, 'Color', 'red');
title('5cos(2\pi ft) | 10HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");

nexttile;
stem(s2s3T, s2s3, 'Color', 'red');
title('5cos(2\pift) | 20HZ sampling | 5 cycles', 'Interpreter', 'tex');
xlabel('time'); ylabel("amplitude");
