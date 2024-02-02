% Load the penguins dataset
url = 'https://raw.githubusercontent.com/Rob-hub-lang/a2-DataVis-5Ways/main/penglings.csv';
data = readtable(url);

% Extract relevant columns
flipperLength = data.flipper_length_mm;
disp(sum(isnan(flipperLength)));
bodyMass = data.body_mass_g;
disp(sum(isnan(bodyMass)));
billLength = data.bill_length_mm;
species = categorical(data.species);

% Set up figure
figure;

% Loop through each species and create a scatter plot
hold on; % Allow multiple plots on the same axes
speciesList = categories(species);
colors = [1 0.647 0; 0.545 0.373 0.694; 0 0.545 0.545]; % RGB values for 'darkorange', 'darkorchid', 'darkgreen'
for i = 1:length(speciesList)
    currentSpecies = speciesList{i};
    indices = species == currentSpecies;
    scatter(flipperLength(indices), bodyMass(indices), billLength(indices)*5, 'MarkerFaceColor', colors(i, :), ...
        'DisplayName', currentSpecies, 'MarkerEdgeAlpha', 0.8, 'MarkerFaceAlpha', 0.8, 'SizeData', billLength(indices)*5);
end
hold off;

% Customize axes
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
title('Scatter Plot of Penguins');
grid on;

% Add legend with explicit entries
legend('Location', 'best');

% Add colorbar for bill length
c = colorbar;
c.Label.String = 'Bill Length (mm)';
caxis([min(billLength), max(billLength)]);

% Adjust figure properties
set(gca, 'FontSize', 12);
set(gcf, 'Position', [100, 100, 800, 600]);

% Save the plot as an image (optional)
saveas(gcf, 'scatter_plot_matlab.png');
