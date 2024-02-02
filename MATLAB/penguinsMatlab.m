data = readtable('penglings.csv');

flipper_length_mm = data.flipper_length_mm;
body_mass_g = data.body_mass_g;
bill_length_mm = data.bill_length_mm;
species = data.species;


figure;

% Create a scatter plot for each species
% use strcmp to sort the data by species for each data catagory
hold on;
scatter(flipper_length_mm(strcmp(species, 'Adelie')), body_mass_g(strcmp(species, 'Adelie')), bill_length_mm(strcmp(species, 'Adelie')), [1, 0.55, 0], 'filled', 'MarkerFaceAlpha', 0.5);
scatter(flipper_length_mm(strcmp(species, 'Chinstrap')), body_mass_g(strcmp(species, 'Chinstrap')), bill_length_mm(strcmp(species, 'Chinstrap')), [0.5, 0, 0.5], 'filled', 'MarkerFaceAlpha', 0.5);
scatter(flipper_length_mm(strcmp(species, 'Gentoo')), body_mass_g(strcmp(species, 'Gentoo')), bill_length_mm(strcmp(species, 'Gentoo')), [0, 1, 1], 'filled', 'MarkerFaceAlpha', 0.5);
hold off;


xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
legend('Adelie', 'Chinstrap', 'Gentoo');
title('Penguin Scatter Plot(Size of dot relates to bill length mm)');
grid on;
