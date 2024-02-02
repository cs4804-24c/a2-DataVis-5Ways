% prepare data
[species,island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex,year] = readvars('penglings.csv');
species = categorical(species);

% map colors to species
map = [ 0.850 0.325 0.098
        0.000 0.447 0.741
        0.929 0.694 0.125 ];

% make the circles
scatter(flipper_length_mm, body_mass_g, bill_length_mm, species, 'filled','MarkerFaceAlpha', 0.7);

% color the circles correctly
colormap(map);

% grid, legend, axis labels
grid on;
colorbar('Ticks',[1.33,2,2.66],'TickLabels',{'Adelie','Chinstrap','Gentoo'})
xlabel('Flipper Length (mm)');
ylabel('Body Mass (g)');
