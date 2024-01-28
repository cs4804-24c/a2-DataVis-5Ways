% Read the CSV file
data = readtable('https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv');

% Extract variables for plotting
flipper_length = data.flipper_length_mm;
body_mass = data.body_mass_g;
bill_length = data.bill_length_mm;
species = data.species;

% Assign colors based on species
color_map = containers.Map({'Adelie', 'Chinstrap', 'Gentoo'}, ...
                            {[1, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]});

% Assign marker sizes based on bill length, normalized and scaled
marker_size = 100 * (bill_length - min(bill_length)) / (max(bill_length) - min(bill_length)) + 10;

% Create the plot
figure;
hold on;
for i = 1:length(species)
    species_color = color_map(species{i});
    if strcmp(species{i},'Adelie')
            scatter1 = scatter(flipper_length(i), body_mass(i), marker_size(i), ...
            'MarkerEdgeColor', 'none', 'MarkerFaceColor', species_color, ...
            'MarkerFaceAlpha', 0.5);
    elseif strcmp(species{i},'Chinstrap')
            scatter2 = scatter(flipper_length(i), body_mass(i), marker_size(i), ...
            'MarkerEdgeColor', 'none', 'MarkerFaceColor', species_color, ...
            'MarkerFaceAlpha', 0.5);
    else
            scatter3 = scatter(flipper_length(i), body_mass(i), marker_size(i), ...
            'MarkerEdgeColor', 'none', 'MarkerFaceColor', species_color, ...
            'MarkerFaceAlpha', 0.5);
    end
end
hold off;

% Add legend
legend([scatter1(1),scatter2(1),scatter3(1)],'Adelie', 'Chinstrap', 'Gentoo', 'Location', 'northeastoutside');

% Add labels
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
grid on;

% Save the figure
saveas(gcf, 'matlab_plot.png');
