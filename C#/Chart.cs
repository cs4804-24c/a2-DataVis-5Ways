using CSharp.Properties;
using Microsoft.VisualBasic.FileIO;
using System;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace CSharp
{
    public partial class Chart : Form
    {
        public Chart()
        {
            InitializeComponent();
        }

        private void Chart_Load(object sender, EventArgs e)
        {
            var path = "./penglings.csv";
            using (TextFieldParser csvParser = new TextFieldParser(path))
            {
                csvParser.CommentTokens = new string[] { "#" };
                csvParser.SetDelimiters(new string[] { "," });
                csvParser.HasFieldsEnclosedInQuotes = true;

                // Skip the row with the column names
                csvParser.ReadLine();

                var adelie = new Series();
                var chinstrap = new Series();
                var gentoo = new Series();
                while (!csvParser.EndOfData)
                {
                    // Read current line fields, pointer moves to the next line.
                    string[] fields = csvParser.ReadFields();
                    string species = fields[1];
                    int bill_length_mm, flipper_length_mm, body_mass_g;
                    try
                    {
                        bill_length_mm = (int)Math.Round(double.Parse(fields[3]));
                        flipper_length_mm = int.Parse(fields[5]);
                        body_mass_g = int.Parse(fields[6]);
                    }
                    catch (Exception)
                    {
                        continue;
                    }

                    switch (species)
                    {
                        case "Adelie":
                            adelie.Points.Add(new DataPoint(flipper_length_mm, body_mass_g) { MarkerSize = bill_length_mm / 2 });
                            break;
                        case "Chinstrap":
                            chinstrap.Points.Add(new DataPoint(flipper_length_mm, body_mass_g) { MarkerSize = bill_length_mm / 2 });
                            break;
                        case "Gentoo":
                            gentoo.Points.Add(new DataPoint(flipper_length_mm, body_mass_g) { MarkerSize = bill_length_mm / 2 });
                            break;
                    }
                }

                chart1.Series.Clear(); //Remove default series

                InitializeChart(adelie, Color.FromArgb(253, 162, 70), "Adelie");
                InitializeChart(chinstrap, Color.FromArgb(172, 90, 212), "Chinstrap");
                InitializeChart(gentoo, Color.FromArgb(73, 161, 161), "Gentoo");

                var area = new ChartArea();
                area.AxisX.IsStartedFromZero = false;
                area.AxisY.IsStartedFromZero = false;
                area.AxisX.Title = "Flipper Length(mm)";
                area.AxisX.TitleAlignment = StringAlignment.Center;
                area.AxisY.Title = "Body Mass (g)";
                area.AxisY.TitleAlignment = StringAlignment.Center;
                area.Name = "Scatter";

                var sizeLegend = new Legend()
                {
                    Name = "bill_length_mm",
                    Title = "bill_length_mm",
                    TitleAlignment = StringAlignment.Center
                };
                sizeLegend.CustomItems.Add(new LegendItem()
                {
                    MarkerSize = 8,
                    MarkerStyle = MarkerStyle.Circle,
                    Color = Color.DimGray,
                    Name = "40",
                    ImageStyle = LegendImageStyle.Marker
                });
                sizeLegend.CustomItems.Add(new LegendItem()
                {
                    MarkerSize = 10,
                    MarkerStyle = MarkerStyle.Circle,
                    Color = Color.DimGray,
                    Name = "50",
                    ImageStyle = LegendImageStyle.Marker
                });

                var speciesLegend = new Legend()
                {
                    Name = "species",
                    Title = "species",
                    TitleAlignment = StringAlignment.Center
                };

                chart1.Series.Add(adelie);
                chart1.Series.Add(chinstrap);
                chart1.Series.Add(gentoo);

                chart1.ChartAreas.Clear(); //Remove default area
                chart1.ChartAreas.Add(area);

                chart1.Legends.Add(speciesLegend);
                chart1.Legends.Add(sizeLegend);
            }
        }

        private void InitializeChart(Series s, Color c, string name)
        {
            var transColor = Color.FromArgb((int)Math.Round(c.A * 0.8), c.R, c.G, c.B);
            s.ChartType = SeriesChartType.Point;
            s.Color = c;
            s.IsVisibleInLegend = true;
            s.Legend = "species";
            s.LegendText = name;
            s.MarkerStyle = MarkerStyle.Circle;
            s.MarkerColor = transColor;
            s.MarkerBorderColor = c;
            s.ChartArea = "Scatter";
        }

        private void chart1_Click(object sender, EventArgs e)
        {

        }
    }
}
