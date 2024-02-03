% Read penguin data
csv = readtable('penglings.csv');

% Extract penguin attributes
species = csv.species;
flipper = csv.flipper_length_mm;
bodyMass = csv.body_mass_g;
billLength = csv.bill_length_mm;

% Define a unique color scheme for each species
speciesColors = containers.Map( ...
    {'Adelie', 'Chinstrap', 'Gentoo'}, ...
    {'#479f9f', '#aa58d2', '#fba044'} ...
);

% Set the scaling factor for point size
scalingFactor = 10;

figure;

% Iterate through each species and plot the data with different colors and sizes
specieTypes = unique(species);
for i = 1:length(specieTypes)
    currentSpecies = specieTypes{i};

    iSpecies = strcmp(species, currentSpecies);
    sFlipperLengths = flipper(iSpecies);
    sBodyMasses = bodyMass(iSpecies);
    sBillLengths = billLength(iSpecies);

    % Adjust point size based on bill length
    pointSizes = sBillLengths * scalingFactor - 250;

    % Plot the data with different colors and sizes
    scatter(sFlipperLengths, sBodyMasses, pointSizes, hex2rgb(speciesColors(currentSpecies)), 'filled', 'MarkerFaceAlpha', 0.8);
    hold on;
end

% Set labels and title
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
title('Penguin Body Mass vs Flipper Length for Different Species');

xlim([min(flipperLengths-5), 235]);

% Add legend to the top left
legend(specieTypes, 'Location', 'Northwest');

grid on;
hold off;

% Function to convert hex color code to RGB
function rgb = hex2rgb(hex)
    rgb = sscanf(hex(2:end), '%2x') / 255;
    rgb = rgb';
end
