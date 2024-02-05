% https://www.mathworks.com/matlabcentral/answers/699325-scatter-with-different-colors-based-on-id-column
% https://www.mathworks.com/help/matlab/ref/scatter.html
data = readmatrix('/home/taya/Downloads/penglings.csv'); 


% Extract columns from the data matrix
x = data(:, 6); % flipper length
y = data(:, 7); % body mass
sizes = data(:, 4); % sizes of points based on bill length
c = linspace(1,10,length(x));

s = scatter(x, y, sizes *10, c, 'filled'); % Multiply by 10 to adjust the point sizes

% Set the opacity of the markers to 80%
s.MarkerFaceAlpha = 0.8;

xlabel('Flipper Length');
ylabel('Body Mass');
title('Flipper Length vs Body Mass');
grid on; % Add grid lines to the plot