% Load the data from the CSV file
data = readtable('penglings.csv');

% Extract relevant columns
species = data.species;
flipper_length = data.flipper_length_mm;
body_mass = data.body_mass_g;
bill_length = data.bill_length_mm;

% Define colors for each species
colors = containers.Map({'Adelie', 'Chinstrap', 'Gentoo'}, {'#479f9f', '#aa58d2', '#fba044'});

% Define the size scaling factor for the points based on bill length
size_scaling_factor = 10;

% Create a figure
figure;

% Iterate through each species and plot the data with the corresponding color and size
unique_species = unique(species);
for i = 1:length(unique_species)
    current_species = unique_species{i};
    
    % Filter data for the current species
    species_indices = strcmp(species, current_species);
    species_flipper_length = flipper_length(species_indices);
    species_body_mass = body_mass(species_indices);
    species_bill_length = bill_length(species_indices);
    
    % Scale the size based on bill length
    point_size = species_bill_length * size_scaling_factor - 280;
    
    % Plot the data with the corresponding color and size
    scatter(species_flipper_length, species_body_mass, point_size, hex2rgb(colors(current_species)), 'filled', 'MarkerFaceAlpha', 0.8);
    hold on;
end

% Set labels and title
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
title('Body Mass vs Flipper Length for Different Penguin Species');

% Add legend to the top left for the species and colour
% also for bill length corrolated with size of dots
legend(unique_species, 'Location', 'Northwest');



% Show the grid
grid on;

% Display the plot
hold off;

% Function to convert hex color code to RGB
function rgb = hex2rgb(hex)
    rgb = sscanf(hex(2:end), '%2x') / 255;
    rgb = rgb';
end
