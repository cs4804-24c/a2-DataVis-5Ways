% Assuming you have the penguins data loaded or created

% Create the scatter plot with color mapping and smaller marker size
figure('Position', [100, 100, 800, 500]);
gscatter(penguins.flipper_length_mm, penguins.body_mass_g, penguins.species, ...
    [1, 0.549, 0; 0.545, 0.169, 0.871; 0, 1, 1], '.', 1 * penguins.bill_length_mm, 'off');

% Create a colorbar
%c = colorbar('Ticks', 1:3, 'TickLabels', {'Adelie', 'Gentoo', 'Chinstrap'});
%c.Label.String = 'Species';

xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
title('Scatter Plot of Penguins');
grid on;

legend('Adelie','Gentoo','Chinstrap')
