data = readtable("C:\Users\joshj\Downloads\a2-DataVis-5Ways-main\penglings.csv");

species = data.species;
flipperLength = data.flipper_length_mm;
bodyMass = data.body_mass_g;
billLength = data.bill_length_mm;

uniqueSpecies = unique(species);

colors = lines(length(uniqueSpecies));

figure;

for i = 1:length(uniqueSpecies)
    idx = strcmp(species, uniqueSpecies{i});
    
    scatter(flipperLength(idx), bodyMass(idx), billLength(idx)*2, 'filled', ...
        'MarkerFaceColor', colors(i,:), 'DisplayName', uniqueSpecies{i}, ...
        'MarkerFaceAlpha', 0.65);
    hold on;
end

xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
legend('Location', 'best');

hold off;
