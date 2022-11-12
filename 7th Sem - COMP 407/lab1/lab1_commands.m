% Getting acquainted with functions

% creating figure
figure('Name', 'Demonstraing Plotting in Matlab');
title('Demonstraing Plotting in Matlab');

% creating values
x = linspace(1, 10, 10);
y = x.^2;
z = y + 10;

% clreating plots
tiledlayout(2, 4);

% 3D subplot
ax1 = nexttile([2 3]);
plot3(ax1, x, y, z);
title(ax1, '3D view');
xlabel('X-axis'); ylabel('Y-axis'); zlabel('Z-axis');

% 2d subplots

ax2 = nexttile;
stem(ax2, x);
title(ax2, 'X values');
xlabel('X-axis'); ylabel('Value');

ax3 = nexttile;
bar(ax3, y);
title(ax3, 'Y values');
xlabel('Y-axis'); ylabel('Value');

ax4 = nexttile;
plot(ax4, z);
title(ax4, 'Z values');
xlabel('Z-axis'); ylabel('Value');
