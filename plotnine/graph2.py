import pandas as pd
import plotnine as p9

df = pd.read_csv("..\penglings.csv")

plot = (p9.ggplot(data=df,
        mapping=p9.aes(x='flipper_length_mm', y='body_mass_g'))
        + p9.geom_point(p9.aes(color='species', size='bill_length_mm'), alpha=0.8)
        + p9.scale_color_manual(values=["#FF8C01", "#9933CB", "#128E8E"]))

print(plot)
