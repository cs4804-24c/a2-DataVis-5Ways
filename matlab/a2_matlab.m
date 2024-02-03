penguins = readtable("penglings.csv")
flipLength = penguins.flipper_length_mm
bodyMass = penguins.body_mass_g
billLength = (penguins.bill_length_mm * 5) - 150
species = penguins.species
numSpecies = zeros(size(species));
for i = 1:length(species)
    if strcmp(species{i}, 'Adelie')
        numSpecies(i) = 1;
    elseif strcmp(species{i}, 'Chinstrap')
        numSpecies(i) = 2;
    else
        numSpecies(i) = 3;
    end
end

chart = scatter(flipLength,bodyMass,billLength,numSpecies,"filled",MarkerFaceAlpha=0.8)
