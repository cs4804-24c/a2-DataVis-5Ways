file = readtable('penglings.csv');
Adelie = table2array(file(1:151,4:7));
Gentoo = table2array(file(152:274,4:7));
Chinstrap = table2array(file(275:342,4:7));

b_Adelie = Adelie(:,1);
f_Adelie = Adelie(:,3);
m_Adelie = Adelie(:,4);
b_Gentoo = Gentoo(:,1);
f_Gentoo = Gentoo(:,3);
m_Gentoo = Gentoo(:,4);
b_Chinstrap = Chinstrap(:,1);
f_Chinstrap = Chinstrap(:,3);
m_Chinstrap = Chinstrap(:,4);

clf;
figure = bubblechart(f_Adelie,m_Adelie,b_Adelie-30,'#FF8C00','MarkerFaceAlpha',0.8);
bubblesize([1 30]);
hold on;
figure = bubblechart(f_Gentoo,m_Gentoo,b_Gentoo-30,'#008B8B','MarkerFaceAlpha',0.8);
bubblesize([1 30]);
hold on;
figure = bubblechart(f_Chinstrap,m_Chinstrap,b_Chinstrap-30,'#9932CC','MarkerFaceAlpha',0.8);
bubblesize([1 30]);
xlabel("Flipper Length (mm)");
ylabel("Body Mass (g)");
hold off;