f = 2e3;
%Period
T = 1 / f;
tmin = 0;
tmax = 3 * T; % Plot 5 cycles
dt = 1/1e6;
dt1 = 1/5e3;
dt2 = 1/1e4;
dt3 = 1/2e4;
t = tmin:dt:tmax;
t1 = tmin:dt1:tmax;
t2 = tmin:dt2:tmax;
t3 = tmin:dt3:tmax;
%signals
ct = 5 * cos(2 * pi * f * t);
x1 = 5 * cos(2 * pi * f * t1); % sampled at 5khz
x2 = 5 * cos(2 * pi * f * t2); %sampled at 10 Khz
x3 = 5 * cos(2 * pi * f * t3); %sampled at 20 Khz
ax1 = subplot(221);
plot(t, ct);
title('Subplot 1: 5 * cos(2*pi*f*t)');
xlabel("Time in second");
ylabel("Amplitude");
ax2 = subplot(222);
stem(t1, x1);
title('Subplot 2: Sampled at 5KHz');
ax3 = subplot(223);
stem(t2, x2);
title('Subplot 3: Sampled at 10Khz');
ax4 = subplot(224);
stem(t3, x3);
title('Subplot 4: Sampled at 20Khz');
