% Read the data
data = readtable('https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv');
x = data.flipper_length_mm;
y = data.body_mass_g;
species = data.species;
island = data.island;
billlength = data.bill_length_mm;
opacity = 0.65;

% Scale the size based on bill_length_mm
circleSize = 200 * (billlength - min(billlength)) / (max(billlength) - min(billlength)) + 10;

% Create Scatter Plot
scatter(data.flipper_length_mm(strcmp(data.species, 'Adelie')), data.body_mass_g(strcmp(data.species, 'Adelie')), circleSize(strcmp(data.species, 'Adelie')), ...
    'MarkerFaceColor', '#4fb8b6', 'MarkerEdgeColor', 'none', 'MarkerFaceAlpha', opacity, 'DisplayName', 'Adelie');
hold on;

scatter(data.flipper_length_mm(strcmp(data.species, 'Chinstrap')), data.body_mass_g(strcmp(data.species, 'Chinstrap')), circleSize(strcmp(data.species, 'Chinstrap')), ...
    'MarkerFaceColor', '#343483', 'MarkerEdgeColor', 'none', 'MarkerFaceAlpha', opacity, 'DisplayName', 'Chinstrap');

scatter(data.flipper_length_mm(strcmp(data.species, 'Gentoo')), data.body_mass_g(strcmp(data.species, 'Gentoo')), circleSize(strcmp(data.species, 'Gentoo')), ...
    'MarkerFaceColor', '#383b47', 'MarkerEdgeColor', 'none', 'MarkerFaceAlpha', opacity, 'DisplayName', 'Gentoo');

% Add labels and title
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
title('Penguin Flipper Length (mm) vs. Body Mass (g)');

% Add Legends
legend('Adelie', 'Chinstrap', 'Gentoo', 'Location', 'Best');
legend('Location','northeastoutside')
